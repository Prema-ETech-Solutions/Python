""" 
Identity operators are used to compare the objects, 
not if they are equal, 
but if they are actually the same object, 
with the same memory location 
"""
"""
Operator	Description	                                                Example  
is 	        Returns True if both variables are the same object.	        x is y	
is not	    Returns True if both variables are not the same object.	    x is not y
"""
Cars = ["BMW","VOLVO"]
Company = ["BMW","VOLVO"]
Data = Cars
# is
print(Cars is Data)

# returns True because Data is the same object as Cars

print(Cars is Company)

# returns False because Cars is not the same object as Company, 
# even if they have the same content

print(Cars == Company)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because Cars is equal to DATA

# is not
print(Cars is not Data)

# returns False because Data is the same object as Cars

print(Cars is not Company)

# returns True because Cars is not the same object as Company,
# even if they have the same content

print(Cars != Company)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False 
# because Cars is equal to Company




