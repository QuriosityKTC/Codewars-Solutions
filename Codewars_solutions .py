#CODEWARS ASSIGNMENT 1

def get_count(string): # Function to count vowels in a given string
    return sum(1 for char in string if char in 'aeiouAEIOU')

print(get_count("today is a great day for Python!!"))



def no_space(x): # Defines a function "no_space." This function takes a string input (x) and removes all spaces from it.
    return x.replace(" ", "") # Return the string (x) and replace all spaces (" ") with no spaces ("")
# Test Results
print(no_space("Hello World"))



def number_to_string(num): # defines the function as "number to string" and takes a given number and returns it as a string
    return str(num) # returns the string form of whatever number is put inside the paren
# Example usage/Test Input:
print(number_to_string(123))  # Output: "123"
print(number_to_string(45.67))  # Output: "45.67"



def even_or_odd(number): # defines the function and names it even or odd. Function takes a number as input and returns whether the number is even or odd.
    if number % 2 == 0: # if the number is divisible by 2 
        return "Even" # if divisible by 2 it is 
    else: # if not divisible by 2 evenly
        return "Odd" # display odd
    
print(even_or_odd(5)) # print even or odd based off the number 5... output - odd
print(even_or_odd(8))  # print even or odd based off the number 8... output - even