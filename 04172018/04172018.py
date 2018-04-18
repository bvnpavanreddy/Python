Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/pavan.badveli/Desktop/canarabank docs/PYTHON/4162018/part3.py 
Traceback (most recent call last):
  File "C:/Users/pavan.badveli/Desktop/canarabank docs/PYTHON/4162018/part3.py", line 17, in <module>
    c.skills()
  File "C:/Users/pavan.badveli/Desktop/canarabank docs/PYTHON/4162018/part3.py", line 12, in skills
    father.skills()
TypeError: skills() missing 1 required positional argument: 'self'
>>> 
 RESTART: C:/Users/pavan.badveli/Desktop/canarabank docs/PYTHON/4162018/part3.py 
i enjoy gardening and programming 
i enjoy cooking and painting
i love sports
>>> import os
>>> os.getcwd()
'C:\\Users\\pavan.badveli\\Desktop\\canarabank docs\\PYTHON\\4162018'
>>> os.chdir('C:\\Users\\pavan.badveli\\Desktop\\canarabank docs\\PYTHON\\04172018')
>>> os.getcwd()
'C:\\Users\\pavan.badveli\\Desktop\\canarabank docs\\PYTHON\\04172018'
>>> myfile=open(a.txt)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    myfile=open(a.txt)
NameError: name 'a' is not defined
>>> myFile=open('a.txt')
>>> print (myFile.read())
this file contains the below content and it ais vey secret
>>> myFile.close()
>>> print (myFile.read())
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print (myFile.read())
ValueError: I/O operation on closed file.
>>> myFile=('a.txt')
>>> print(myfile.read())
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(myfile.read())
NameError: name 'myfile' is not defined
>>> print(myFile.read())
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(myFile.read())
AttributeError: 'str' object has no attribute 'read'
>>> myFile=open('a.txt')
>>> print (myFile.read())
this file contains the below content and it ais vey secret
>>> myFile.close()
>>> myfile=open('a.txt')
>>> myfile.close ()
>>> myfile=open('a.txt','a')
>>> myfile.write('this is second line i am adding '\n)
SyntaxError: unexpected character after line continuation character
>>> myfile.write('this isthe second line in the file \n')
36
>>> myfile.close()
>>> 
