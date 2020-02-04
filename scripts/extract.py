#!/usr/bin/env python
# coding: utf-8

import re, sys, subprocess
from pprint import pprint

n = 10
inputstr = ''.join(sys.stdin.readlines())

llvm_path = '/home/condekind/LLVM/10/build/bin/'

def llvm_stat_clean(stat_line):
    result = [_ for _ in stat_line.strip().split(maxsplit=3)]
    return result[1], result[3], result[0]

user_stats = subprocess.run('extract.sh',
                              input=inputstr,
                              capture_output=True,
                              text=True)
pprint([
    llvm_stat_clean(line)
    for line in
        user_stats.stderr.split('\n')
    if
        re.search('^ *\d+\s+\S+\s+-\s+.*', line) != None
])
