#Write a Python Program for Fibonacci numbers.
#The Fibonacci numbers are the numbers in the following integer sequence.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,……In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.



num = int(input("Enter any number:"))
n1 = 0
n2 = 1
sum = 0
if num<=0:
    print("please enter number greater than 0 : ")
else:
     print(n1)
     print(n2)
     for i in range(0, num):
        n1 = n2 
        n2 = sum
        sum = n1 + n2
        print(sum)
        
    
        

 
