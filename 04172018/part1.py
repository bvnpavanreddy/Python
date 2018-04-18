Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> import re
phone = "my number is 425-324-5656"
phonenumberRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phonenumberRegex.search(phone)
mo.group()
SyntaxError: multiple statements found while compiling a single statement
>>> import re
phone = "my number is 425-324-5656"
phonenumberRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phonenumberRegex.search(phone)
mo.group()import re
phone = "my number is 425-324-5656"
phonenumberRegex= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phonenumberRegex.search(phone)
mo.group()
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> import re
>>> phone = "my number is 222-333-4444"
>>> phoneRegex= re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
>>> mo = phoneRegex.search(phone)
>>> mo.group()
'222-333-4444'
>>> 

>>> mo.group(1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    mo.group(1)
IndexError: no such group
>>> mo.group(2)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    mo.group(2)
IndexError: no such group
>>> mo.group(0)
'222-333-4444'
>>> words = "i like fruits and i love dryfruits and i love mangos also"
>>> fruitRegex=re.compile(r'fruits|dryfruits|mangos')
>>> mo=fruitRegex.search(words)
>>>  mo.group()
 
SyntaxError: unexpected indent
>>> mo.group()
'fruits'
>>> mo.fruitRejex.compile("dryfruits and mangos")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    mo.fruitRejex.compile("dryfruits and mangos")
AttributeError: '_sre.SRE_Match' object has no attribute 'fruitRejex'
>>> mo.fruitRegex.compile("dryfruits and mangos")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    mo.fruitRegex.compile("dryfruits and mangos")
AttributeError: '_sre.SRE_Match' object has no attribute 'fruitRegex'
>>> mo.fruitRegex.search("dryfruits and mangos")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    mo.fruitRegex.search("dryfruits and mangos")
AttributeError: '_sre.SRE_Match' object has no attribute 'fruitRegex'
>>> mo=fruitRegex.search("dryfruits and mangos")
>>> mo.group()
'dryfruits'
>>> phoneRegex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> mo = phoneRegex.search('this is my phone number 333-4444')
>>> mo.group()
'333-4444'
>>> phoneRegex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')#here ? work as a optional so it will allow you to choose the 7 digit number also as your phone number

>>> phoneRegex=re.compile (r'Bat(wo)+man')
>>> mo=phoneRegex.search('i am batman')
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo = phoneRegex.serach('i am batwoman')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    mo = phoneRegex.serach('i am batwoman')
AttributeError: '_sre.SRE_Pattern' object has no attribute 'serach'
>>> mo = phoneRegex.search('i am batwoman')
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo = phoneRegex.search('i am Batwoman')
>>> mo.group()
'Batwoman'
>>> 
phoneRegex=re.compile (r'Bat(wo)*man')
>>> # if wo exists or batman it will give us the result
>>> phoneRegex=re.compile (r'Bat(wo)+man')
>>> # this time batman wont work as it has to have wo in the given string
