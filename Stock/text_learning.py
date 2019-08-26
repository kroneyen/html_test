#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
"""
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)

benfit = 1 * random.randint(1,100)

if  benfit <= 10 : 
     reward ='10%'
elif  benfit >10 and benfit < 20 :
    reward = '7.5%'
elif  benfit >20 and benfit < 40 : 
    reward = '5%'                 
elif  benfit >40 and benfit < 60 : 
    reward = '3%'                 
elif  benfit >60 and benfit < 100 : 
    reward = '1.5%'                 
else  :
    reward = '1%'
   

print('benfit:',benfit , 'reward:',reward)


class Parent(object):
    x = 1


class Child1(Parent):

   pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)


def  div1 (x,y) :
    print( "%s/%s = %s" % (x, y, x/y)) ## float

def  div2 (x,y) :
    print( "%s//%s = %s" % (x, y, x//y)) ##整除

div1( 5 , 2 )
div1( 5. , 2 )
div2( 5 , 2 )
div2( 5. , 2. )

5/2 = 2.5
5/2 = 2.5
5/2 = 2
5/2 = 2.0
"""


def multipliers():
    return [lambda x: i * x for i in range(4)]
    ### def fun(x) :
    #    for i in range(4)
    #        a = i * x
    #    return a


print([m(2) for m in multipliers()])