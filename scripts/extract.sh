#!/bin/bash

source func.sh

#---------------------------------- Variables ----------------------------------

# Parallel *execution* (not compilation)
[[ -n $JOBS ]]        || JOBS=8

# Set the lib SUFFIX according to OS
[[ $(uname -s) == "Linux" ]] && SUFFIX="so" || SUFFIX="dylib"

[[ -n $BASEDIR ]]     || BASEDIR="$(pwd)"
[[ -n $SUITESDIR ]]   || SUITESDIR="$BASEDIR/suites/"

# Output from passes ran in comp.sh
[[ -n $OUTFILE ]]     || OUTFILE="$(pwd)/output/stats.txt"

# Error from passes ran in comp.sh
[[ -n $ERRFILE ]]     || ERRFILE="$(pwd)/output/error.txt"

# Custom user passes file
[[ -n $PASSFILE ]]    || PASSFILE="$(pwd)/info/passes.txt"

# Custom user passes array
[[ -n $USERPASSES ]]  || readarray -t USERPASSES < $PASSFILE

# LLVM_PATH  => The place where I have all the LLVM tools
[[ -n $LLVM_PATH ]]   || LLVM_PATH="/home/condekind/LLVM/10/build/bin"
[[ -d $LLVM_PATH ]]   || echo "invalid LLVM_PATH: $LLVM_PATH"

#-------------------------------------------------------------------------------

echo "--------------------------------------"
echo "JOBS        is set to $JOBS"
echo "SUFFIX      is set to $SUFFIX"
echo "BASEDIR     is set to $BASEDIR"
echo "SUITESDIR   is set to $SUITESDIR"
echo "LLVM_PATH   is set to $LLVM_PATH"
echo "USERPASSES  is set to ${USERPASSES[@]}"
echo "--------------------------------------"

#-------------------------------- Main Loop ------------------------------------

[[ -n $SUITES ]]      || SUITES=($( find ${SUITESDIR} -mindepth 1 -maxdepth 1 -type d ))
echo "suites: $SUITES"
for suite in "${SUITES[@]}"; do
  cd $suite
  BENCHS=($( find $(pwd) -name '*.c' -printf '%h\n' | sort -u ))
  echo "benchs: $BENCHS"
  for bench in "${BENCHS[@]}"; do
    cd $bench && echo "Starting $bench"
    setvars || continue
    cleanup
    compile || continue
    bcstats || continue
    delvars
  done
done
cd $BASEDIR

<<<<<<< Updated upstream
#-------------------------------------------------------------------------------
=======

>>>>>>> Stashed changes
