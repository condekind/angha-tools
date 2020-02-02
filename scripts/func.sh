

setvars() {

  # These will be overwritten if they're defined in an info.sh file
  BENCH_NAME=$(basename $(pwd))
  SRC_FILES=($(find $(pwd) -name '*.c' -printf '%p\n' | sort -u ))
  COMPILE_FLAGS=" -I. "

  # variables specific to each benchmark, set on /suite/.../bench/.../info.sh
  [[ -f info.sh ]] && echo "Sourcing info.sh from $(pwd)" && source info.sh

  # BENCH_NAME comes either from provided info.sh or the 'else' block above
  lnk_name="$BENCH_NAME.rbc"
  if [[ -n $CPU2006 && $CPU2006 -eq 1 ]]; then
    if [[ $(uname -s) == "Linux" ]]; then
      rbc_name="$BENCH_NAME.linux"
    else
      rbc_name="$BENCH_NAME.llvm"
    fi
  fi

  # cpu specific stuff
  [[ ${bench} =~ "cpu2006" ]] && CPU2006=1
  # sometimes we need to use clang++
  [[ -n $COMPILER   ]] || COMPILER="clang"
  # We can specify STDIN to something other than /dev/stdin
  [[ -n $STDIN      ]] || STDIN=/dev/null
  # And STDOUT default is /dev/null. 
  [[ -n $STDOUT     ]] || STDOUT=/dev/null
  # removes math library linking flag, which isn't used with clang's -c param
  COMPILE_FLAGS="${COMPILE_FLAGS/\-lm/}"

  echo "SRC_FILES: ${SRC_FILES[@]}"
  return 0
}


cleanup() { rm -f *{.bc,.rbc,.txt} ; }


compile() {

  # csmith requires extra args
  [[ ${SUITE##*/} == "csmith_kernels_largest_10k" ]] && EXTRA_FLAGS=" -I../runtime -Wno-everything "
  
  # ---------------------------- source to bytecode ----------------------------
  if [[ -n $CPU2006 && $CPU2006 -eq 1 ]]; then $LLVM_PATH/opt -S $rbc_name -o $lnk_name
  else  # SRC_FILES is the variable with all the files we're gonna compile
    [[ -n $SRC_FILES ]] || return 2
    parallel --tty --jobs=${JOBS} $LLVM_PATH/$COMPILER $COMPILE_FLAGS $EXTRA_FLAGS -Xclang \
    -disable-O0-optnone -S -c -emit-llvm {} -o {.}.bc ::: "${SRC_FILES[@]}" # 2>>$ERRFILE
    
    parallel --tty --jobs=${JOBS} $LLVM_PATH/opt -S {.}.bc -o {.}.rbc ::: "${SRC_FILES[@]}" # 2>>$ERRFILE
  
    # Merge all the rbcs into a big rbc:
    $LLVM_PATH/llvm-link -S *.rbc -o $lnk_name
  fi
  return 0
}


bcstats() {
  # ---------------------------- bytecode to stats -----------------------------
  OUTBUFFER="${BASEDIR}/.__OUTPUTBUFFER.tmp"
  echo "header://${SUITE##*/};${BENCH_NAME}" >> "$OUTBUFFER"
  $LLVM_PATH/opt                    \
        -mem2reg                    \
        -O3                         \
        ${USERPASSES[@]}            \
        -instcount                  \
        -stats                      \
        -S                          \
        ${lnk_name}                 \
        -disable-output 2>> "$OUTBUFFER"
  [[ $? -ne 0 ]]                   &&
    cat "$OUTBUFFER" >> "$ERRFILE" ||
    cat "$OUTBUFFER" >> "$OUTFILE"
  [[ -f $OUTBUFFER ]] && rm $OUTBUFFER
  unset OUTBUFFER
  return 0
}


delvars() { unset {COMPILER,STDIN,STDOUT,RUN_OPTIONS,BENCH_NAME,SRC_FILES,CPU2006} ; }

