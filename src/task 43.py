
# -----------------------------------------------------------------------------------------------------------------------
#   Exercise 43 - Lists
# -----------------------------------------------------------------------------------------------------------------------

# Given the code below, use the correct method on line 10 in order to find out how many times does the element 20 occur in my_list.
"""
my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

howmany = my_list.

print(howmany)
"""

# -----------------------------------------------------------------------------------------------------------------------
#   Solution Implementation
# -----------------------------------------------------------------------------------------------------------------------

my_list = [10, 10.5, 20, 30, 'Python', 'Java', 'Ruby']

howmany = my_list.count(20)

print(howmany)