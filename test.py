"""

 ---- Tasks ----
        
    1) Write a program that receives numbers from user until the character 'q' 
    is received. print the avarge numbers.

    2) Write a program that receives list of numbers and another number.
    The function will change the list itself so that it doesn't contain numbers
    that are divisible by the additional number. 

    3) Write a program that receives a String from user and prints if 
    it is a palindrome or not.

    4) Write a program that simulates a lottery. The program reccive from the user
    three numbers between 1 to 9. The program will then randomly select three different 
    numbers from the range(1-9). If the selectd numbers are the same as those guessed 
    by the user we will print "You Win" otherwise we will print "You Lose".

    5) Write a program that receive name of file as first argument.
    The file consisting rows of numbers. Sum all the numbers and write it in the end
    of the file.

    6) Write a function that receive list of numbers between 0 to 9. The function 
    return new list that counts a separate amount for each digit.

"""



# // ------ task 1 ------
"""
num= 0
counter= 0
sum = 0 

while num != 'q':
    num = input('Enter a number: ')
    if num != 'q':
        num = int(num)
        counter+= 1
        sum += num
        
print('The AVG is: ', (sum/counter))

"""



# // ------ task 2 ------
"""
def orderList(numList, numZ):
    i = 0
    while i < len(numList):
        if numList[i] % numZ == 0:
            numList.pop(i)
            i+=1
        else:
            i+=1

"""


# // ------ task 3 ------
'''
str = input('Enter your word: ')
size = int(len(str)/2)
i=0
bool = True

while i < size:
    if str[i] != str[len(str)-i-1]:
        bool = False
        break
    else:
        i+=1

if bool == True:
    print('The word is a palindrome')
else:
    print('The word isnt a palindrome')
'''


# // ------ task 4 ------
'''
from random import randint

arr=[0,0,0]
brr=[0,0,0]
crr=['first','second','third']
x=0

while x < len(arr):
    arr[x] = int(input('Enter the '+str(crr[x])+' number: '))
    brr[x] = randint(1,9)
    x+=1

print('Result: ',brr)

if arr == brr:
    print("You Win")
else:
    print("You Lose")
'''


# // ------ task 5 ------
'''
sum=0
file = open("c.txt", "r+")

for line in file:
    sum += int(line)


file.write("\n"+format(str(sum)))
file.close()
'''

# // ------ task 6 ------
'''
arr = [2,4,5,6,1,2,4,1,1,1]

def sum_numbers(arr):
    brr = [0]*10
    for num in arr:
        brr[num] +=1
    print(brr)
    
sum_numbers(arr)
'''