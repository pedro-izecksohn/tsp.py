'''tsp2g.py - Travelling Salesman Program Second Generation.
   By: Pedro Izecksohn, izecksohn@yahoo.com
   License: Gnu General Public License version 3 as published by the Free Software Foundation.
   You should know that I wrote a similar program for Google more than 10 years ago and our contract expired more than 5 years ago.
'''

from math import inf

class Point:
    def __init__ (self, x, y):
        self.x=x
        self.y=y

def read_Point () -> Point:
    ret = Point(0,0)
    s=input("Enter a point: ")
    if not s:
        return None
    l=s.split(',')
    if len(l)!=2:
        print("A point must have 2 dimensions separated by ,")
        exit()
    ret.x=float(l[0])
    ret.y=float(l[1])
    return ret

def read_all_Points ()->list:
    ret=[]
    while True:
        p=read_Point()
        if not p:
            return ret
        ret.append(p)

def print_PointsVector (pv:list):
    for p in pv:
        print (f"{p.x},{p.y}")

def distance (a:Point, b:Point)->float:
  xd = a.x-b.x
  yd = a.y-b.y
  return ((xd*xd)+(yd*yd))**0.5

def total_distance (pv:list)->float:
  ret = 0.0
  u = 0
  while (u<(len(pv)-1)):
    d = distance (pv[u], pv[u+1])
    #print ("d = %f"%d)
    ret += d
    u+=1
  d = distance (pv[-1],pv[0])
  #print ("d = %f"%d)
  ret += d
  return ret

def main ():
  original = read_all_Points()
  if (len(original)<4):
    print_PointsVector (original)
    exit()
  orig_dist = total_distance (original)
  print ("orig_dist = %f"%orig_dist)
  copy = original[:]
  sl=[None]*len(original)
  sl[0] = copy[0]
  del copy[0]
  u = 1
  while (u<len(sl)):
    d = inf
    tbr = 0
    w = 0
    while (w<len(copy)):
      cd = distance (sl[u-1], copy[w])
      if (cd < d):
        d = cd
        tbr = w
      w+=1
    sl[u] = copy[tbr]
    del copy[tbr]
    u+=1
  #print ("len(copy)=%u\n"%len(copy))
  del copy
  sorted_dist = total_distance (sl)
  print ("sorted_dist = %f"%sorted_dist)
  if (sorted_dist<orig_dist):
    #print ("sorted_dist = %f"%sorted_dist)
    original = sl
  else:
    print ("I could not short your path.")
    del sl
  print_PointsVector (original)

main()
