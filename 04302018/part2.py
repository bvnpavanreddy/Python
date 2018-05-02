"""ab=open('abc.txt','w')
ab.write('python is a great language.\n yeah it is great!!!\n')
ab.close()"""

"""ab=open('abc.txt','r+')
str=ab.read()

print('the content in the file is :',str)
ab.close()"""


"""ab=open('abc.txt','r+')
str=ab.read(15)
print('read the string:',str)

position =ab.tell()
print('the postion of the file is :',position)


str1=ab.read(10)
print('read the next 10 words in the file is :',str1)

# now i am going to reposition the pointer in the begining again

position = ab.seek(0,0)
print('above stateent is going to reposition the pointer to staring ')
str2=ab.read(15)
print('read the strings in the file :',str2)
ab.close()"""

import os
#os.rename('abc.txt','abc1.txt')

#os.remove('abc2.txt')

#os.mkdir('new')
#os.chdir('C:/Users/pavan.badveli/Desktop/canarabank docs/PYTHON/Python/04302018/new')

#os.getcwd()

#os.chdir('C:/Users/pavan.badveli/Desktop/canarabank docs/PYTHON/Python/04302018')

#os.rmdir('new')

"""ab=open('abc3.txt','w')
print('name of the file:',ab.name)
ab.write('this is new file and i am adding some data to it\n this is going to print in the next line')
#ab.close()
ab=open('abc3.txt','r+')
str2=ab.read(17)
print('the first 17 characters in the file is :',str2)
#ab.close()

fno=ab.fileno()
print('the file number is :',fno)
ret=ab.isatty()
print('return valuse is:',ret)"""

"""ab=open('abc4.txt','w')
ab.write('c++ \n Java \n Python \n Perl \nPHP\n')
ab=open('abc4.txt','r')
print("name of the file :",ab.name)
for index in range (5):
    line= next(ab)
    print('Line no %d-%s ' %(index,line))
ab.close()"""

ab=open('abc4.txt','r')
line= ab.readlines()
print("read lines: %s" %(line))
ab.seek(0,0)
line=ab.readline()
print('read lines:%s'%(line))
pos=ab.tell()
print('the positioning of the pointer is :',pos)



