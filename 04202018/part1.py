import random
"""print ("randrange(1,366,2):",random.randrange(1,366,2))"""
"""print("random():",random.random())"""
"""list = [22,3,35,4,58,69,788]
random.shuffle(list)
print ("shuffled list is :",list)"""

"""var1 = "hello world"
print ("updating string :",var1[:6]+"Python")"""

"""str1='python is great language'
print('the string contains:', min(str1))"""


"""srt1='you have nine girfriends'
str1.replace ('you have nine girfriends','you have a wife')
print('the new string is:', srt1)"""


"""str="this is going to conver into upper case letters"
print ("the string which is converted to upper case is :",srt.capitalize())"""

"""str="thispppp ish aptheopphlksapfjppppa"

sub ='p'

print ("str.count('p'):",str.count(sub))

sub = 'ap'

print ("this is 2nd example:",str.count(sub))"""



"""list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print(list1[0])
print(list2[1:3])
list2[1]=11111
print(list2[1:3])
del list2[2]
print(list2)"""



"""list1 = ['physics', 'chemistry', 'maths']
list2=list(range(5))
list1.extend(list2)
print (list1)"""


"""list1 = ['physics', 'chemistry', 'maths']
list1.insert(1, 'art')
print ('Final list : ', list1)"""



"""list1 = ['art', 'abc', 'bot', 'bycycle']
list1.reverse()
print ("list now : ", list1)"""


"""tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

tup3=tup1+tup2
print("tup3:",tup3)"""


"""list1= ['pav', 'che', 'phy', 'bio']
tuple1=tuple(list1)
print ("tuple elements : ", tuple1)"""


"""dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
print ("Equivalent String :%s"  %str (dict))"""


"""import time
import calendar"""
"""t= time.time()
print('todays time is :',t)
print(time.localtime())

localtime1=time.asctime(time.localtime(time.time()))
print ("date and time is :",localtime1)"""

"""cal=calendar.month(2018,4)
print ("This month Calender follows")
print(cal)"""

"""cal = calendar.month(2018, 4)
print ("Here is the calendar:")
print (cal)"""


num = 113


if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")


