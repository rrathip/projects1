#sum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#hi john
b = input()
print('Hi '+ b)

#Square
b = int(input())
print(b**2)

#area
a = int(input())
b = int(input())

a*b*0.5 
print(a*b*0.5)

#Hello, harry
name = input()


print('Hello, ' + name + '!')

#apple sharing

d = int(input())
n = int(input())

print(n // d)
print(n % d)

#previous and next
a = int(input())
b = a-1 
c = a+1 
print('The next number for the number',a, 'is',c) 
print('The previous number for the number',a, 'is',b) 

#Timestamps
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

x = d - a
y = e - b
z = f - c

t = (3600 * x) + (60 * y) + (z)

print(t)

#schooldesks
a = int(input())
b = int(input())
c = int(input())

x = a//2 + a%2
y = b//2 + b%2
z = c//2 + c%2

print(x+y+z)

#last digit of integer
x = int(input())
print(x%10)

#Tens digits
x = int(input())
y = x//10
print(y%10)

#Sum of digits
x = int(input())
a = x%10
y = x//10
b = y%10
c = x//100

print(a+b+c)

#Fractional Part
from math import floor

a = float(input())
b = floor(a)
int(b)
c = (a - b)
print(c)

#First Digit after decimal point
x = float(input())
b = int(x)
c = x-b
d = int(c/0.1)
print(d)

#Car Route 
from math import ceil
a = int(input())
b = int(input())

c = b/a

x= ceil(c*1)

print(x)

#Digital Clock
n = int(input())
h = n//60
m = n%60

print(h)
print(m)

#Total Cost
A = int(input())
B = int(input())
C = int(input())

x = A*100
y = B
z = x + B


print(((z*C)//100), (z*C%100))


#Clock Face 1
h =int(input())
m =int(input())
s =int(input())

x = (h*3600)+(m*60)+s

print(x*0.00833333)

#Clock Face 2
a = float(input())

x = a%30

print(x*12)
