#Q1

l1=[]
x=int(input("Enter how many integers you want to enter\n"))
print("Enter elements")
for i in range(x):
    a=int(input())
    l1.append(a)
print(l1)

#Q2

l2 = ['google', 'apple', 'facebook', 'microsoft', 'tesla']
l1.append(l2)
print(l1)

#Q3
l3 = []
y=int(input("Enter how many integers you want to enter\n"))
print("Enter elements")
for i in range(x):
    b=int(input())
    l3.append(b)
print(l3.count(4))

#Q4

l3.sort()
print(l3)

#Q5

l4=[4,5,9,8,2,6,78,56,23,45]
l3.extend(l4)
l3.sort()
print(l3)

#Q6
a=[10,42,65,23,78]
even=0
odd=0
for x in a:
    if(x%2==0):
        even+=1
    else:
        odd+=1
print('No. of even elements are %d\nNo. of odd elements are %d\n'%(even,odd))


#Tuples

#Q1

t1=(4,5,6,8)
print(t1[::-1])


#Q2

max=t1[0]
min=t1[0]
for x in t1:
    if(max<x):
        max=x
    if(min>x):
        min=x
print('Max=%d\n Min=%d'%(max,min))


#Strings

#Q1

print('Enter a string\n')
a=input()
print(a.upper())

#Q2

print('Enter')
a=input()
print(a.isnumeric())

#Q3

a='Hello World'
print(a.replace('World','Rachit'))
