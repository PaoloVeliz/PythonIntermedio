#Estructure of a lambda function
#lambda arguments: expression
from functools import reduce

#Exmaple
palindrome = lambda string: string == string[::-1]
#identificator|--argument--|---expression---------|
print(palindrome('ana'))

#HIGH ORDER FUNCTIONS: filter, map and reduce
my_list = [1,2,3,4,5,6,7,8,9,1,10,11,12,13,14,15]
#filter
odd = list(filter(lambda x: x%2 != 0,my_list))

#map
#challenge using list comprehension
challenge = [i**2 for i in my_list]
#using map
squares = list(map(lambda x: x**2,my_list))

#reduce

# if u want to use the "reduce" function, u need to put this line in the beginning of your file <from functools import reduce>
# variable a is going to be the first element of our list
# variable b is going to be the next element of our list
elements_multiplication = reduce(lambda a, b: a * b, my_list)
