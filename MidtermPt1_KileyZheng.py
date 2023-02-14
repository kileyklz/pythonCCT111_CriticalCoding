# CCT111 Critical Coding
# Mid-term - Coding Questions (Part 1 of Test)
# Winter 2023

# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing the results when each function is correct.
# Include comments to describe your logic.

# ONLY WRITE CODE IN THE SECTION OF EACH QUESTION
# THAT SAYS     # WRITE YOUR CODE HERE

# Note! Changing the test harness or writing an if else statement to return the
# test case answers will not earn any marks!

# If you don't know how to write the code, write comments describing the logic you'd use for part marks.

#######################################
# QUESTION 1
#######################################
'''
Phone numbers in North America are 10 digits excluding the 1 at the start,
so a valid phone number is 613-555-1212 (entered into your program as 6135551212).
The original area codes in Ottawa is 613, London is 519, and Toronto is 416.
Please write a python function that takes in a 10-digit phone number
(assume no input of any dashes or brackets), and returns the string "Ottawa" if
the phone number is Ottawa, "London" if the number is London, or "Toronto" if the number is
Toronto. It should return "Another City" if the number is outside these 3 regions.
Assume the user enters in a valid input without any dashes. Include comments in your code.
'''

def identify_city(phone_number):
    """
    This function takes in a 10-digit phone number and returns the city the number is from.
    If the phone number starts with 613, the function returns "Ottawa".
    If the phone number starts with 519, the function returns "London".
    If the phone number starts with 416, the function returns "Toronto".
    Otherwise, the function returns "Another City".

    Parameters:
    phone_number (str): A string representation of a 10-digit phone number without dashes or brackets.

    Returns:
    str: The city the phone number is from.
    """

    ##############
    # WRITE YOUR CODE HERE
    # asks user to input a valid phone number
    phone_number = str(input("Please enter a 10 digit phone number:"))
    # takes the first three numbers, the area code from the inputted phone number
    area_code = phone_number[:3]
    # tests the area code and returns the corresponding city
    if (area_code == "613"):
        return("Ottawa")
    elif (area_code == "519"):
        return("London")
    elif (area_code == "416"):
        return("Toronto")
    else:
        return("Another City")
    ##############



#######################################
# QUESTION 2
#######################################
'''
write a function shift_upper that takes two strings as input (s1 and s2) 
and returns a string containing the uppercase letters of s1 followed by the 
uppercase letters of s2 followed by the lowercase letters of s1 followed by the 
lowercase letters of s2. The order of the letters should be preserved 
as they appear in the input strings.
Hint: consider isupper() or islower()
'''


def shift_upper(s1,s2):
    """shift_upper. This function must return a string containing the
    uppercase letters of s1 followed by the uppercase letters of s2
    followed by the lowercase letters of s1 followed by the lowercase
    letters of s2. Do not otherwise change the order of the letters
    (see the test cases below for examples).

    Parameters:
    s1 (str): A string of characters, potentially including non-letters that should be ignored
    s2 (str): A string of characters, potentially including non-letters that should be ignored

    Returns:
    s (str): A string of letters or "" as per the description above.
    """
    ##############
    # WRITE YOUR CODE HERE
    # loops to find the uppercase letters in s1
    for x in s1:
        upper_s1 = x.isupper()
    # loops to find the uppercase letters in s2
    for x in s2:
        upper_s2 = x.isupper()
    # loops to find the lowercase letters in s1
    for x in s1:
        lower_s1 = x.islower()
    # loops to find the lowercase letters in s2
    for x in s2:
        lower_s2 = x.islower()
    ##############
# returns a string
    return str(upper_s1 + upper_s2 + lower_s1 + lower_s2)


###########################
# Question 3
###########################

'''
Write a function sum_even_digits that takes an integer 
as input and returns the sum of all even digits in that integer.

For example, sum_even_digits(123456) should return 12 
because 2 + 4 + 6 = 12. If the input integer does not 
contain any even digits, the function should return 0
'''


def sum_even_digits(num):
    """
    This function takes an integer n as input and returns the sum of the even digits of n.

    Parameters:
    n (int): An integer whose even digits are to be summed

    Returns:
    int: The sum of the even digits of n
    """
    ##############
    # WRITE YOUR CODE HERE
    # convert num into a string to loop
    num_str = str(num)
    # created a variable to store even numbers
    sum_even = 0
    # check for even digits in n and add them together
    for n in num_str:
        # convert num back into int
        num_int = int(num)
        if num_int % 2 == 0:
            # if num is even, add it to the sum
            sum_even += num_int
    # return the sum of even digits
    return sum_even

    #############




##################
# Question 4
##################
'''
Write a function called compound_interest that takes in three positive float parameters: principal, rate, and time. The function should calculate the amount of compound interest that would be added to the principal at the given rate after the indicated time using the following formula:

A = P(1 + R/100)^T, where:

A is the amount
P is the principal amount
R is the rate
T is the time span
The function should then return the amount of interest earned, rounded to 2 decimal places.
'''


def compound_interest(principal, rate, time):
    """compound_interest. This function must return the amount of compound interest
    that would be added to the principal at the given interest rate after the indicated
    time.
    Parameters:
        principal (float): The initial amount of currency in dollars and cents (2 decimal places)
        rate (float): The annual interest rate (assume the interest is compounded annually as per the formula above)
        time (float): The number of years, as a decimal. e.g. 1.5 = 18 months.
    Returns:
        compound_interest (float): The amount of interest earned in dollars and cents (2 decimal places)
    """

    ##############
    # WRITE YOUR CODE HERE
    # calculates the amount
    amount = float(principal * (1 + rate/100) ** time)
    # rounds answer to two decimal places
    compound_interest = round(amount - principal, 2)
    return "$" + compound_interest

    ##############

    return


###########################################################
###########################################################
### DO NOT EDIT ANY CODE BELOW HERE. IT TESTS YOUR CODE
###########################################################
###########################################################


def test_sum_even_digits():
    # Test case 1: Check if the function returns the expected result for a positive integer with even digits
    num = 1234
    expected = 6
    result = sum_even_digits(num)
    print(f"For the number {num}, expected: {expected}, but got: {result}")

    # Test case 2: Check if the function returns the expected result for a positive integer with odd digits
    num = 12345
    expected = 2
    result = sum_even_digits(num)
    print(f"For the number {num}, expected: {expected}, but got: {result}")

    # Test case 3: Check if the function returns the expected result for a positive integer with a mix of even and odd digits
    num = 123456
    expected = 12
    result = sum_even_digits(num)
    print(f"For the number {num}, expected: {expected}, but got: {result}")

    # Test case 4: Check if the function returns the expected result for zero
    num = 0
    expected = 0
    result = sum_even_digits(num)
    print(f"For the number {num}, expected: {expected}, but got: {result}")

    # Test case 5: Check if the function returns the expected result for a negative integer with even digits
    num = -1234
    expected = 6
    result = sum_even_digits(num)
    print(f"For the number {num}, expected: {expected}, but got: {result}")

    # Test case 6: Check if the function returns the expected result for a negative integer with odd digits
    num = -12345
    expected = 2
    result = sum_even_digits(num)
    print(f"For the number {num}, expected: {expected}, but got: {result}")

    # Test case 7: Check if the function returns the expected result for a negative integer with a mix of even and odd digits
    num = -123456
    expected = 12
    result = sum_even_digits(num)
    print(f"For the number {num}, expected: {expected}, but got: {result}")


def test_phone_number():
    test_cases = [
        # Ottawa
        ('6135551212', "Ottawa"),
        ('6139555121', "Ottawa"),
        ('6135551213', "Ottawa"),
        # London
        ('5195551212', "London"),
        # Toronto
        ('4165551212', "Toronto"),
        # Another City
        ('9055551212', "Another City"),
    ]
    for x in test_cases:
        output = identify_city(x[0])
        print(f"identify_city({x[0]}) = {output}\nExpected output? {output == x[1]}")


def test_shift_upper():
    # Test case 1: Check if the function returns the expected result for two simple strings
    result = shift_upper("Hello", "World")
    expected = "HWelloorld"
    print(f"Test case 1: Expected {expected}, got {result}")

    # Test case 2: Check if the function handles strings with non-letter characters
    result = shift_upper("Hello!", "World?")
    expected = "HWelloorld"
    print(f"Test case 2: Expected {expected}, got {result}")

    # Test case 3: Check if the function handles only uppercase characters
    result = shift_upper("HELLO", "WORLD")
    expected = "HELLOWORLD"
    print(f"Test case 3: Expected {expected}, got {result}")

    # Test case 4: Check if the function handles only lowercase characters
    result = shift_upper("hello", "world")
    expected = "helloworld"
    print(f"Test case 4: Expected {expected}, got {result}")

    # Test case 5: Check if the function handles empty strings
    result = shift_upper("", "")
    expected = ""
    print(f"Test case 5: Expected {expected}, got {result}")

    # Test case 6: Check if the function handles strings with a mix of uppercase, lowercase, and non-letter characters
    result = shift_upper("H3llo!", "WoRlD?")
    expected = "HWRDllool"
    print(f"Test case 6: Expected {expected}, got {result}")


def test_compound_interest():
    # test case 1
    principal = 1000
    rate = 5
    time = 2
    expected = 102.50
    actual = compound_interest(principal, rate, time)
    print("For the test case principal=", principal, ", rate=", rate, ", time=", time, ":")
    print("Expected Output:", expected)
    print("Actual Output:", actual)
    print()
    # test case 2
    principal = 1000
    rate = 5
    time = 5
    expected = 276.28
    actual = compound_interest(principal, rate, time)
    print("For the test case principal=", principal, ", rate=", rate, ", time=", time, ":")
    print("Expected Output:", expected)
    print("Actual Output:", actual)
    print()

    # test case 3
    principal = 500
    rate = 8
    time = 3
    expected = 129.86
    actual = compound_interest(principal, rate, time)
    print("For the test case principal=", principal, ", rate=", rate, ", time=", time, ":")
    print("Expected Output:", expected)
    print("Actual Output:", actual)
    print()


def main():
    print("\n")
    print("Testing Question 1")
    test_phone_number()

    print("\n")
    print("Testing Question 2")
    test_shift_upper()

    print("\n")
    print("Testing Question 3")
    test_sum_even_digits()

    print("\n")
    print("Testing Question 4")
    test_compound_interest()


if __name__ == '__main__':
    main()
