'''
The program takes a dictionary and prints the sum of all the items in the dictionary.
Problem Solution:
1. Declare and initialize the n number of dictionary values from the user.
2. Find the sum of all the values in the dictionary.
3. Print the total sum.
4. Exit.
Sample Input:
3
100
540
239
Sample Output :
879
'''
# Take the number of items in the dictionary from the user
n = int(input("Enter the number of items in the dictionary: "))

# Initialize an empty dictionary
my_dict = {}

# Input values and store them in the dictionary
for i in range(n):
    key = i + 1  # Using consecutive integers as keys
    value = int(input(f"Enter value for item {key}: "))
    my_dict[key] = value

# Calculate the sum of all values in the dictionary
total_sum = sum(my_dict.values())

# Print the total sum
print(total_sum)
