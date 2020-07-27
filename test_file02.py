#!/usr/bin/env python

import os
import re
import sys
from pprint import pprint

#reg=sys.argv[1]

#pprint(re.findall(r'reg[a-z]+',str(dir(os))))
pprint(re.findall(r'get[a-z]+',str(dir(os))))

print("Here is some modification to the previous version")
