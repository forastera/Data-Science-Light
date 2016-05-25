#!/usr/bin/env python
import sys;
import re;


args = len(sys.argv);
a = [];

if(args > 1):
  a = re.split(",(?:\s+)?",sys.argv[1]);
  for i in range(0,len(a)):
    a[i] = float(a[i]);


def avg(arr):
  sum = 0.0;
  total = len(a);
  if(total == 0): return 0;
  for v in arr:
    sum += float(v);

  return float(sum / float(total));

print avg(a);

#how to use  python avg.py "2,3,4,5,6.3333"
