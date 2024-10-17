'''
The program takes a number from the user and generates a dictionary that contains numbers (between 1 and n) in the form (x,x*x). 
Problem Solution:
1. Take a number from the user and store it in a separate variable.
2. Declare a dictionary and using dictionary comprehension initialize it to values keeping the number between 1 to n as the key and the square of the number as their values.
3. Print the final dictionary.
4. Exit.
Sample I/O:
5
Sample O/P:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
# Take a number from the user
n = int(input("Enter a number: "))

# Generate the dictionary using dictionary comprehension
squares_dict = {x: x * x for x in range(1, n + 1)}

# Print the final dictionary
print(squares_dict)

