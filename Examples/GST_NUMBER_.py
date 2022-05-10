# Python3 program to validate
# GST (Goods and Services Tax) number
# using regular expression
import re

# Function to validate GST
# (Goods and Services Tax) number.
def isValidMasterCardNo(str):

	# Regex to check valid
	# GST (Goods and Services Tax) number
	regex = "^[0-9]{2}[A-Z]{5}[0-9]{4}"+"[A-Z]{1}[1-9A-Z]{1}"+"Z[0-9A-Z]{1}$"
	
	# Compile the ReGex
	p = re.compile(regex)

	# If the string is empty
	# return false
	if (str == None):
		return False

	# Return if the string
	# matched the ReGex
	if(re.search(p, str)):
		return True
	else:
		return False

# Driver code

# Test Case 1:
str1 = "06BZAHM6385P6Z2"
print(isValidMasterCardNo(str1))

# Test Case 2:
str2 = "06BZAF67"
print(isValidMasterCardNo(str2))

# Test Case 3:
str3 = "AZBZAHM6385P6Z2"
print(isValidMasterCardNo(str3))

# Test Case 4:
str4 = "06BZ63AHM85P6Z2"
print(isValidMasterCardNo(str4))

# Test Case 5:
str5 = "06BZAHM6385P6F2"
print(isValidMasterCardNo(str5))

# This code is contributed by avanitrachhadiya2155
