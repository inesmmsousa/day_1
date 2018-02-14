'''
Created on 05/02/2018

@author: Utilizador
''' 
a = 5
print(a)
a = a + 10
print(a)
b = a
print(a + b)
c = 10
print( a + b + c)
c ='xpto'
print(c)
d = [1,2,3,4]
print(d)
d.append(5)
print(a)
d.remove(1)
del d[2]
print(d)

message = """
Portugal is the best!
"""

name = input('Where are you from?')
for i in name:
    if i == 'Portugal':
        print(message.format(name))

        


