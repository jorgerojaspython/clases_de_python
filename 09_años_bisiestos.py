################################################ to detect si es año bisiesto
def isYearLeap(year): 
    if (year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)):
        return True
    else:
        return False
 ################################################ to detect dias y mes del año
def daysInMonth(year, month):  
    n=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if month>12:
        return None
    if isYearLeap(year):
        n=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    return n[month]

######################################### probar funcioes
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
 ################################################ to detect dias y mes del año
