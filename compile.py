import sys
import json
from pathlib import Path
from pprint import pprint


if __name__ == '__main__':

  # if len(sys.argv) < 2:
  #   print('Usage: {}, "/path/to/stats/file" "output"'.format(sys.argv[0]))
  # exit(1)

  basedir = Path(infile)+'/page-angha'
  print(basedir)