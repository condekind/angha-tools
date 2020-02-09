#!/bin/bash

#-------------------------------------------------------------------------------

# load vars
COMPILE_FLAGS=" -I. "
EXTRA_FLAGS=""
llvm_path="${llvm_path:-/home/condekind/LLVM/10/build/bin}"

pass_file="../info/passes.txt"
readarray -t custom_passes < "$pass_file"

command -v "$llvm_path"/clang &>/dev/null || exit 2
command -v "$llvm_path"/opt &>/dev/null   || exit 2

# compile user program
"$llvm_path"/clang    \
  $COMPILE_FLAGS      \
  $EXTRA_FLAGS        \
  -x c                \
  -Xclang             \
  -disable-O0-optnone \
  -emit-llvm          \
  -S                  \
  -o /dev/stdout - 2>/dev/null |
"$llvm_path"/opt      \
  -mem2reg            \
  -O0                 \
  -instcount          \
  ${custom_passes[@]} \
  -stats              \
  -S                  \
  -disable-output - 


#-------------------------------------------------------------------------------
