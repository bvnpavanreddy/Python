Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.match('a','abdnsa').group()
'a'
>>> re.search('a','anananan')
<_sre.SRE_Match object; span=(0, 1), match='a'>
>>> re.search('n.+','abcndessa abdjs').group()
'ndessa abdjs'
>>> re.search('c','abbd\nc').start()
5
>>> re.search('c','abbd\nc').end()
6
>>> re.search('ca','abbd\nc')
>>> re.search('c/a','abbd\nc')
>>> re.search('c/a','abbd\nc').group()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    re.search('c/a','abbd\nc').group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> re.search('c/a','abbdnc')
>>> re.search('c|a','abbdnc')
<_sre.SRE_Match object; span=(0, 1), match='a'>
>>> re.search('c|a|d','candjndk')
<_sre.SRE_Match object; span=(0, 1), match='c'>
>>> re.findall('a|b|g','abdggnsj andi')
['a', 'b', 'g', 'g', 'a']
>>> re.search('abcd','abcdgnsj abcd')
<_sre.SRE_Match object; span=(0, 4), match='abcd'>
>>> re.findall('abcd','abcdgnsj abcd')
['abcd', 'abcd']
>>> re.searh(r'\w\w\w\w','abcdgnsj abcd')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    re.searh(r'\w\w\w\w','abcdgnsj abcd')
AttributeError: module 're' has no attribute 'searh'
>>> re.search(r'\w\w\w\w','abcdgnsj abcd')
<_sre.SRE_Match object; span=(0, 4), match='abcd'>
>>> re.search('\w\w\w\w','abcdgnsj abcd')
<_sre.SRE_Match object; span=(0, 4), match='abcd'>
>>> re.search('\w\w\w','ab_cdfr ksitv')
<_sre.SRE_Match object; span=(0, 3), match='ab_'>
>>> re.search('\w\w\w','ab!!cdfr ksitv')
<_sre.SRE_Match object; span=(4, 7), match='cdf'>
>>> re.search('\w\w\w','ab!!cdr ksitv')
<_sre.SRE_Match object; span=(4, 7), match='cdr'>
>>> re.search('\w\w\w','ab!!cd+ks#tv')
>>> re.search('\w\w\W','ab!!cd+ks#tv')
