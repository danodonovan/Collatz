import numpy
import pylab as p

def collatz( v ):
 nv = 0
 while v != 1:
  if v % 2 == 0:
   v /= 2
  else:
   v = ( 3 * v ) + 1
  nv += 1
 return nv

visits = []

for v in range( 1, 99999 ):
 visits.append( [v, collatz(v)] )

visits = numpy.array( visits )

p.scatter( visits[:,0], visits[:,1], marker='+' )
p.savefig('Fig1.png')
p.show()

