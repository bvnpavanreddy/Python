"""def functionName(level):
    if level <1:
        raise exception(level)
    return level
try:
    l=functionName(-10)
    print("level=",l)
except Exception as e:
    print("error in level argument",e.args[0])"""

"""class networkerror(RuntimeError):
    def __init__(self,arg):
        self.arg=arg

try:
    raise networkerror("Bad hostname")
except networkerror ,e:
    
    print e.args"""


"""import re

line = 'cats are smarter than dogs'
matchobj=re.match(r'(.*)are (.*?).*',line,re.M|re.I)
if matchobj:
    print("matchobj.group():",matchobj.group())
    print("matchobj.group(1):",matchobj.group(1))
    print("matchobj.group(2):",matchobj.group(2))

else:
    print('no match')"""


import re

#re.search ('n','\\n')

#re.search('n', r'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

#re.search(r'\n','\n\n')

#re.search(r'\n',r'\n\n')

#bool(re.match('c','abcdfrc'))

#re.search('c','abcdefr')

#re.match('c','cbahcou').group()

re.search('n','abnchenskeln njduen').group()
re.search('n.+','abcndessa abdjs').group()
re.search('c','abbd\nc').start()
re.search('c','abbd\nc').end()
re.search('ca','abbd\nc')
re.search('c/a','abbd\nc').group()
re.search('c|a','abbdnc')
re.search('c|a|d','candjndk')

re.findall('a|b|g','abdggnsj andi')
re.search('abcd','abcdgnsj abcd')
re.findall('abcd','abcdgnsj abcd')
