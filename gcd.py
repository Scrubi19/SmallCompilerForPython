#!/usr/bin/python
a=22
b=10

while a!=0 and b!=0:
	if a>b:
		a%=b
	else:
		b%=a
		
print('Func Result =', a+b)