################################################ 
def isYearLeap(a): 
    if (a % 4 == 0 and (a % 100 !=0 or a % 400 == 0)):
        return True
    else:
        return False
 ################################################ 
def daysInMonth(a, m):  
    n=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if m>12:
        return None
    elif isYearLeap(a):
        n=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    return n[m]
################################################ SUMAR LOS AÑOS DEL AÑO 
a=1999+1
m=2
d=19
isYearLeap(a)
daysInMonth(a, m)
dayOfYear(a, m, d)
 sum(n[1:(m-1)])+d



def dayOfYear(a, m, d):
    if daysInMonth(a, m): 
        return d
    else:
        return False

def daysInMonth(a, m):  
    n=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if m>12:
        return None
    elif isYearLeap(a):
        n=[0,31,29,31,30,31,30,31,31,30,31,30,31]
        
    return n[m]
while True:
    print(y)
    y=y+1
    if y>x:
        break

########################### P R O F E S O R ### SUMAR LOS AÑOS DEL AÑO 
       def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		md = daysInMonth(year, m)
		if md == None:
			return None
		days += md
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(dayOfYear(2019, 12, 31)) 
    
    

