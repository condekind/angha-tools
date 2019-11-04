import sys
import json
from pathlib import Path
from pprint import pprint


if __name__ == '__main__':

  # if len(sys.argv) < 2:
  #   print('Usage: {}, "/path/to/stats/file" "output"'.format(sys.argv[0]))
  # exit(1)
  ## args: input, output, passes, llvm-path
  LLVM_PATH = Path('/home/condekind/LLVM/10/build/bin')

  basedir   = Path.cwd() / 'page-angha'
  suitesdir = basedir    / 'suites'
  suites    = [ x for x in suitesdir.iterdir() if x.isdir() ]

  #