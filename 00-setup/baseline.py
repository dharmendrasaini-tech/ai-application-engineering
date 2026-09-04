# These 5 are better:

# 1. Even or Odd

# Write a function:

# def is_even(number):
#     ...

# Return True if the number is even, otherwise False.

# Examples:

# 4 → True
# 7 → False


def is_even(number):
    return True if number % 2 == 0 else False


print(is_even(7))












# 2. Count Vowels

# Write:

# def count_vowels(text):
#     ...

# Return the number of vowels in the string.

# Example:

# "Hello" → 2


def count_vowels(text):

    count = 0

    vowels = set('aeiouAEIOU')

    for ch in text:
        if ch in vowels:
            count += 1


    return count



print(count_vowels("Hello"))









# 3. What will this print, and why?



# a = [1, 2, 3]
# b = a

# b.append(4)

# print(a)
# print(b)
# print(a is b)


# Answers
# print(a) = [1,2,3,4]
# print(b) = [1,2,3,4]
# print(a is b) = True 






















# 4. Safe Integer Conversion

# Write:

# def safe_int(value):
#     ...

# Rules:

# convert a valid numeric string to int
# if conversion fails, return None

# Examples:

# "42" → 42
# "abc" → None

def safe_int(value):

    try:
        value = int(value)
        

    except ValueError:
        return None

    else:
        return value


print(safe_int("42"))
print(safe_int("abc"))



















# 5. Safe Dictionary Lookup

# Write:

# def get_score(scores, name):
#     ...

# Example dictionary:

# scores = {
#     "Aman": 80,
#     "Riya": 92
# }

# Rules:

# return the student's score if the name exists
# return "Not found" if it does not


scores = {
    "Aman": 80,
    "Riya": 92
}



def get_score(scores,name):

    if name in scores:
        return scores[name]

    return "Not found"


print(get_score(scores,"dharm"))

