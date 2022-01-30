"""
Operator	        Description	                            Example  
in 	                Returns True if a sequence 
                    with the specified value is present     x in y
                    in the object	                         	
not in	            Returns True if a sequence with the     x not in y
                    specified value is not present 
                    in the object		
"""
# in
x = ["apple", "banana"]

print("apple" in x)

# returns True because a sequence with the value "banana" is in the list

# not in
print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list
