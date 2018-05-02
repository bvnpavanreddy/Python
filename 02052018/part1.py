"""ab =open('abc.txt','w+')
print('name of the file is :',ab.name)

ab=open('abc.txt','w+')
ab.write('python is a great language.\n and all big websites using this language to develope\n')

ab=open('abc.txt','r')
ac=ab.readlines()
print('read line:%s'%(ac))
ab.close()"""

"""ab=open('abc.txt','r+')
print('name of the file is :',ab.name)

str='this is new line adding to the existing file'
ab.seek(0,2)
line = ab.write(str)

ab.seek(0,0)
for index in range(7):
    line = next(ab)
    print('line no %d-%s'% (index,line))


ab.close()"""

"""ab=open('abc.txt','r+')
seq=['this is the 9th line\n','this is 10th line\n']
ab.seek(0,2)
line=ab.writelines(seq)
ab.seek(0,0)
for index in range(9):
    line=next(ab)
    print('line no %d - %s'% (index,line))

ab.close()"""

"""def tempr(Temperature):
    assert(Temperature >=0,'colder than absolute zero')
    return ((Temperature-273)*1.8)+32

print(tempr(273))
print(int(tempr(505.78)))
print(tempr(-5))"""


"""try:
    ab=open('abc.txt','w')
    ab.write('i am trying to do the exception handling')
except IOError:
    print("Error:can\'t find file or read data")
else:
    print("written content in the file successfully")
    ab.close()"""


"""try:
    ab=open('abc3','r')
    ab.write('i am trying here the exception handling')
except IOError:
    print("error: can\'t find the file to read data")
else:
    print('written the data successfully ')
    ab.close()"""

"""try:
    ab=open('abc111.txt','w')
    try:
        ab.write('addming one more line tho the file')

    finally:
        print('closing the file')
        ab.close()
except IOError:
    print("error:can'\t find the file to read data")"""

"""def temp_convert(var):
    try:
        returnint(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n",Argument)

temp_convert("xyz")"""

