Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> string = 'python is a great language and i am learning the Regular Expressions in python. so this might help developing the new websites '
>>> re.search('.+',string)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    re.search('.+',string)
NameError: name 're' is not defined
>>> import re
>>> re.search('.+',string)
<_sre.SRE_Match object; span=(0, 127), match='python is a great language and i am learning the >
>>> re.search('.+',string, flags=re.DOTALL).group()
'python is a great language and i am learning the Regular Expressions in python. so this might help developing the new websites '
>>> string = 'Hello ,There , How , Are ,You'
>>> re.findall('[A-Z]',string)
['H', 'T', 'H', 'A', 'Y']
>>> re.findall('[a-z]',string)
['e', 'l', 'l', 'o', 'h', 'e', 'r', 'e', 'o', 'w', 'r', 'e', 'o', 'u']
>>> re.findall('[A-Z,]',string)
['H', ',', 'T', ',', 'H', ',', 'A', ',', 'Y']
>>> re.findall('[A-Z,.]',string)
['H', ',', 'T', ',', 'H', ',', 'A', ',', 'Y']
>>> string = 'Hello ,There , How... , Are ,You......'
>>> re.findall('[A-Z,.]',string)
['H', ',', 'T', ',', 'H', '.', '.', '.', ',', 'A', ',', 'Y', '.', '.', '.', '.', '.', '.']
>>> re.findall('[A-Za-z,\s.]',string)
['H', 'e', 'l', 'l', 'o', ' ', ',', 'T', 'h', 'e', 'r', 'e', ' ', ',', ' ', 'H', 'o', 'w', '.', '.', '.', ' ', ',', ' ', 'A', 'r', 'e', ' ', ',', 'Y', 'o', 'u', '.', '.', '.', '.', '.', '.']
>>> re.search('[A-Z]+',string)
<_sre.SRE_Match object; span=(0, 1), match='H'>
>>> re.findall('[A-Z]+',string)
['H', 'T', 'H', 'A', 'Y']
>>> re.search('[A-Z]{2,}',string)
>>> re.findall('[A-Z]{2,}',string)
[]
>>> re.search('[A-Za-z\s,]',string)
<_sre.SRE_Match object; span=(0, 1), match='H'>
>>> re.search('[A-Za-z\s,]',string).group()
'H'
>>> re.search('[A-Za-z\s,]+',string)
<_sre.SRE_Match object; span=(0, 18), match='Hello ,There , How'>
>>> re.search('[A-Za-z\s,]+',string).group()
'Hello ,There , How'
>>> re.search('[^A-Za-z\s,]+',string).group()
'...'
>>> re.findall('[^A_Z]+',string)
['Hello ,There , How... , ', 're ,You......']
>>> re.findall('[^A-Z]+',string)
['ello ,', 'here , ', 'ow... , ', 're ,', 'ou......']
>>> 
