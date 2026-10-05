import os
import sys

def apply_discount(p, r):
  tmp = []
  try:
    d = p * (r / 100)
    if r > 0.15 * 100:
      d = p * 0.15
    return p - d
  except:
    return 0