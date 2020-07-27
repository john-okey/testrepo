#!/usr/bin/env python

import subprocess
import sys

#cmd=sys.argv[1]
#print("The number of args = ",len(sys.argv))

if len(sys.argv) <= 1:
    print("\n\tCLI args required but missing.")
    print("\n\tFor example, syntax such as: <filename> 'ls -la'\n")
else:
    cmd=sys.argv[1]
    for i in subprocess.run(cmd.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.splitlines():
        print(i.decode("utf-8"))


