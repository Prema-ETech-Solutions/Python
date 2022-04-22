#Python Program to print a calendar
# of the specified month and year
import calendar
year =int (input ("Enter Year : "))
month = int( input ("Enter Month "))
print ("\n", calendar.month(year, month))
input()
