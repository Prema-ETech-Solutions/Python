"""
Operator  Name	        Description
&         AND	        Sets each bit to 1 if both bits are 1
|	      OR	        Sets each bit to 1 if one of two bits is 1
^	      XOR	        Sets each bit to 1 if only one of two bits is 1
~ 	      NOT	        Inverts all the bits
<<	      Zero          fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	      Signed        right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""

A = 20
B = 20
print(A&B)
print(A|B)
print(A^B)
print(~A)
print(1<<1)
print(1>>1)
