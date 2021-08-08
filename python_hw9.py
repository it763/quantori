#Решить несколько задач из projecteuler.net

#Решения должны быть максимально лаконичными, и использовать list comprehensions.

#problem9 - list comprehension : one line
#problem6 - list comprehension : one line
#problem48 - list comprehension : one line
#problem40 - list comprehension

from functools import reduce
solution9=[a*b*c for a in range(1000) for b in range(a+1,999) for c in range(b+1,998) if a+b+c ==1000 and a**2+b**2==c**2][0]
#solve9_1=[(a, b, c)  for a in range(1000) for b in range(a+1,999) for c in range(b+1,998) if a+b+c ==1000 and a**2+b**2==c**2]  #Вывод самих a,b,c
solution6=sum([i**2 for i in range(1,101)])-(sum([i for i in range(1,101)]))**2
solution48=str([sum((i**i) for i in range(1,1001))])[-11:-1]
solution40=reduce(lambda x,y:x*y,[int("".join([str(i) for i in range(1, 10000001)])[j]) for j in [0,9,99,999,9999,99999,999999]])

print('Solution fo problem 9 is: ',solution9)
print('Solution fo problem 6 is: ',solution6)
print ('Solution fo problem 48 is: ',solution48)
print ('Solution fo problem 40 is: ',solution40)