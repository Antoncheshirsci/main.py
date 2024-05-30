a='254754'
print(a)
print(len(a))

first,second=100,250
print(first+second,first-second)
summa,diff=first+second,first-second
print(summa,diff)

import statistics
first,second,third=3,7,9
numbers=first,second,third
average=statistics.mean(numbers)
print(average)

first_string,second_string='вторник','понедельник'
print(second_string+","+first_string)


a,b,c=7,9,4
f=((((a*b)+(a*c))**3)//2)
print(f)