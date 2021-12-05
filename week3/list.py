#write a program that prints out all the elements of the list that are less than 5.
listofintegers =    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbers =  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(min(numbers))
#>>> 5
for x in range(0,len(numbers)):
    if (numbers[x]<5):
        print(numbers[x])
        



