#Different string manipulations in python

#Quotations
course = "Python's Course for Beginners"
course2 = 'Python for "Beginneers"'
print(course)
print(course2)



#Multiple Line comments or string
email = '''

Hi, Esther

This is our fisrt email to you.
Hope this reaches you well.

Thank You!
The support team


'''
print(email)


#Indexing
name = 'Esther Gabriel Idang'
print(name[0])
print(name[-3])
print(name[0:9])
print(name[3:])
print(name[:8] + ',' + name[1:-1])


name2= name[:] + ' Exclusive Package'
print(name2)


#Formatted strings
name = 'Esther'
last = 'Idang'
bus = name + ' [ ' + last + ' ] is a coder'
msg = f'{name} [{last}] is a coder'
print(bus)
print(msg)
