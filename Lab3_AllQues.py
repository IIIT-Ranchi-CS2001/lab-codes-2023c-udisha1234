# Write a python script to find the squares of first n natural numbers. Display both the number and the square as shown below. Use while loop
# Number    	Square
# 1              	1
# 2               	4
# …		…
# n		n


# Write a python script to find the sum of the digits of the given number using a while loop. Display the number and the sum.


# Write a python script to print the first n terms of the Fibonacci series using while loop.


# Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.


# Write a python script to check whether all the characters present in a string are alphanumeric (uppercase letters, lowercase letters or digits) using for. Print True if all characters are alphanumeric. Otherwise print False.


# Write a python script to find the number of occurrences of a particular character present in the given string using a loop. (Don’t use string methods).




a = int(input("1.Enter the no. : "))
print("Number --- Square ")
for i in range(1,a+1):
    print(i,i**2,sep="             ")

print('\n\n')

b = int(input("2.Enter the no. : "))
n = 0 
print(b,end=" : ")
while(b):
    n+=b%10
    b=b//10
print("sum of digits of the given no is : ",n)

print('\n\n')

x = int(input("3.Enter the no. : "))
print(0,end=" ")
r=0
s=1
while(x):
    x-=1
    print(s,end=" ")
    t=r
    r=s
    s+=t

print('\n\n')

m = int(input("4.Enter the no. : "))
n = int(input("Enter the limit : "))
for i in range(1,n+1):
    print(m,"x",i,"=",m*i)

print('\n\n')

f = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
w = input("5.Enter the word : ")
flag = True
for i in w :
    if i not in f :
        flag = False
        break
print(flag)

print('\n\n')

a = input("6.Enter the no. : ")
b = input("Enter the char to be counted : ")
n = 0 
for i in a :
    if i.lower() == b :
        n+=1
print("The occ of",b,"in",a,"is",n)
