Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> string = 'john has 6 cats but I think my friend Susan has 3 dogs and Mike'
>>> string = 'john has 6 cats but I think my friend Susan has 3 dogs and Mike has 2 fishes'
>>> re.findall('[A-Za-z]+ \w+ \d+ \w+',string)
['john has 6 cats', 'Susan has 3 dogs', 'Mike has 2 fishes']
>>> re.findall('([A-Za-z]+) \w+ \d+ \w+',string)
['john', 'Susan', 'Mike']
>>> re.findall('[A-Za-z]+ \w+ \d+ (\w+)',string)
['cats', 'dogs', 'fishes']
>>> re.findall('([A-Za-z]+) (\w+) (\d+) (\w+)',string)
[('john', 'has', '6', 'cats'), ('Susan', 'has', '3', 'dogs'), ('Mike', 'has', '2', 'fishes')]
>>> re.findall('([A-Za-z]+) \w+(\d+) (\w+)',string)
[]
>>> re.findall('([A-Za-z]+) \w+ (\d+) (\w+)',string)
[('john', '6', 'cats'), ('Susan', '3', 'dogs'), ('Mike', '2', 'fishes')]
>>> re.search('([A-Za-z]+) \w+ (\d+) (\w+)',string)
<_sre.SRE_Match object; span=(0, 15), match='john has 6 cats'>
>>> match = re.search('([A-Za-z]+) \w+ (\d+) (\w+)',string)
>>> match
<_sre.SRE_Match object; span=(0, 15), match='john has 6 cats'>
>>> match.group()
'john has 6 cats'
>>> match.groups()
('john', '6', 'cats')
>>> match.group(1)
'john'
>>> match.span()
(0, 15)
>>> match span(2)
SyntaxError: invalid syntax
>>> match.span(2)
(9, 10)
>>> match.start(3)
11
>>> re.findall('([A-Za-z]+) \w+ (\d+) (\w+)',string).group(1)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    re.findall('([A-Za-z]+) \w+ (\d+) (\w+)',string).group(1)
AttributeError: 'list' object has no attribute 'group'
>>> data = re.findall('(([A-Za-z]+) \w+ (\d+) (\w+))',string)
>>> data
[('john has 6 cats', 'john', '6', 'cats'), ('Susan has 3 dogs', 'Susan', '3', 'dogs'), ('Mike has 2 fishes', 'Mike', '2', 'fishes')]
>>> for i in data:
	print(i[0])

	
john has 6 cats
Susan has 3 dogs
Mike has 2 fishes
>>> for i in data:
	print(i[3])

	
cats
dogs
fishes
>>> it = re.finditer('[A-Za-z]+ \w (\d+) (\w+)', string)
>>> it
<callable_iterator object at 0x03E69FD0>
>>> next(it).group()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    next(it).group()
StopIteration
>>> for element in it:
	print (element.group(1,2,3))

	
>>> string = 'New York, New york 11369'
>>> match = re.search('([A-Za-z\s]+),([A-Za-z\s]+) (\d+)',string)
>>> match.group(1)
'New York'
>>> pattern = re.compile ('(?P<city>[A-Za-z\s]+),(?P<State>[A-Za-z\s]+),(?P<ZipCode>\d+)')
>>> match = re.search(pattern,string)
>>> match
>>> match.group('city'),match.group('State'),match.group('ZipCode')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    match.group('city'),match.group('State'),match.group('ZipCode')
AttributeError: 'NoneType' object has no attribute 'group'
>>> match.group('city'),match.group('State'),match.group('ZipCode')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    match.group('city'),match.group('State'),match.group('ZipCode')
AttributeError: 'NoneType' object has no attribute 'group'
>>> match.groups()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    match.groups()
AttributeError: 'NoneType' object has no attribute 'groups'
>>> string = '123456789'
>>> re.search('\d+',string)
<_sre.SRE_Match object; span=(0, 9), match='123456789'>
>>> re.search('(\d)+',string)
<_sre.SRE_Match object; span=(0, 9), match='123456789'>
>>> re.findall('(?:\d)+',string)
['123456789']
>>> string = '1234 56789'
>>> re.findall('(?:\d)+',string)
['1234', '56789']
>>> re.split('(\.)', 'today is sunny. i wanted to go to park. and have a icecream')
['today is sunny', '.', ' i wanted to go to park', '.', ' and have a icecream']
>>> def square(x):
	return (x**2)
square(12)
SyntaxError: invalid syntax
>>> 
