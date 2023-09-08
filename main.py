def isLeapYear(year):
     if   (year % 4==0 and year % 100!=0) or year % 400 ==0: 
  return true
  else:
    return False

year = 2050

if isLeapYear  (year) :
 Print('{} is a leap year.'. format(year)) 
else:
    Print('{} is not a leap year.'. format (year))