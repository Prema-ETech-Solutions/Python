# Escape Characters
"""
Add / 
Code	    Result
'	        Single Quote	
\	        Backslash	
n	        New Line	
r	        Carriage Return	
t	        Tab	
b	        Backspace	
f	        Form Feed	
ooo	        Octal value	
xhh	        Hex value
"""

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

