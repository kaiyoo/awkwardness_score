# awkwardness_score
dynamic programming tree



1.
##########  CASE -62

                0     <----- root
        -20           -1
     20      40    -1     1
  !-15  0  !-45  10
  
  
        
PRINT STAEMENT:        
================================DATA:  20 ================================
LEFT:  -15
RIGHT:  0
graindchild:  0
child + SELF:  5
root.sums:  0
Left.sums:  -15
Right.sums:  0
================================DATA:  40 ================================
LEFT:  -45
RIGHT:  10
graindchild:  0
child + SELF:  -5
root.sums:  -5
Left.sums:  -45
Right.sums:  0
================================DATA:  -20 ================================
LEFT:  20
RIGHT:  40
graindchild:  -60
child + SELF:  -25
root.sums:  -60
Left.sums:  0
Right.sums:  -5
================================DATA:  -1 ================================
LEFT:  -1
RIGHT:  1
graindchild:  0
child + SELF:  -2
root.sums:  -2
Left.sums:  -1
Right.sums:  0
================================DATA:  0 ================================
LEFT:  -20
RIGHT:  -1
graindchild:  -6
child + SELF:  -62
root.sums:  -62
Left.sums:  -60
Right.sums:  -2


minimum awkwardness score:  -62




2. 
###########  CASE -16
                    0     <----- root
           -2                -1
      2           4       -1     1
   -3   0    -5       1
            2   3   4    0
                      -2  -4

PRINT STAEMENT:
================================DATA:  2 ================================
LEFT:  -3
RIGHT:  0
graindchild:  0
child + SELF:  -1
root.sums:  -1
Left.sums:  -3
Right.sums:  0
================================DATA:  -5 ================================
LEFT:  2
RIGHT:  3
graindchild:  0
child + SELF:  -5
root.sums:  -5
Left.sums:  0
Right.sums:  0
================================DATA:  0 ================================
LEFT:  -2
RIGHT:  -4
graindchild:  0
child + SELF:  -6
root.sums:  -6
Left.sums:  -2
Right.sums:  -4
================================DATA:  1 ================================
LEFT:  4
RIGHT:  0
graindchild:  -6
child + SELF:  -5
root.sums:  -6
Left.sums:  0
Right.sums:  -6
================================DATA:  4 ================================
LEFT:  -5
RIGHT:  1
graindchild:  -6
child + SELF:  -7
root.sums:  -7
Left.sums:  -5
Right.sums:  -6
================================DATA:  -2 ================================
LEFT:  2
RIGHT:  4
graindchild:  -14
child + SELF:  -10
root.sums:  -14
Left.sums:  -1
Right.sums:  -7
================================DATA:  -1 ================================
LEFT:  -1
RIGHT:  1
graindchild:  0
child + SELF:  -2
root.sums:  -2
Left.sums:  -1
Right.sums:  0
================================DATA:  0 ================================
LEFT:  -2
RIGHT:  -1
graindchild:  -9
child + SELF:  -16
root.sums:  -16
Left.sums:  -14
Right.sums:  -2


minimum awkwardness score:  -16





3. 
###########  CASE -11
                      0      <----- root
            -2                -1
       2         -1       -1      1
   -3    0    -5     20
                   4    -4
               

PRINT STAEMENT:
================================DATA:  2 ================================
LEFT:  -3
RIGHT:  0
graindchild:  0
child + SELF:  -1
root.sums:  -1
Left.sums:  -3
Right.sums:  0
================================DATA:  20 ================================
LEFT:  4
RIGHT:  -4
graindchild:  0
child + SELF:  16
root.sums:  0
Left.sums:  0
Right.sums:  -4
================================DATA:  -1 ================================
LEFT:  -5
RIGHT:  20
graindchild:  -4
child + SELF:  -6
root.sums:  -6
Left.sums:  -5
Right.sums:  0
================================DATA:  -2 ================================
LEFT:  2
RIGHT:  -1
graindchild:  -8
child + SELF:  -9
root.sums:  -9
Left.sums:  -1
Right.sums:  -6
================================DATA:  -1 ================================
LEFT:  -1
RIGHT:  1
graindchild:  0
child + SELF:  -2
root.sums:  -2
Left.sums:  -1
Right.sums:  0
================================DATA:  0 ================================
LEFT:  -2
RIGHT:  -1
graindchild:  -8
child + SELF:  -11
root.sums:  -11
Left.sums:  -9
Right.sums:  -2


minimum awkwardness score:  -11


