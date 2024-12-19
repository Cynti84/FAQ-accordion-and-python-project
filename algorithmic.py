def capitalize_words(input_string):
    # a function to split the string into words based on spaces: split("")
    words = input_string.split(" ")

    # this python funciton 'capitalize()' capitalizes the first word in a string of words
    capitalized_words = [word.capitalize() for word in words]

    # this funcion " ".join() joins the words back together into a single string
    return " ".join(capitalized_words)

# prompt user to enter a string of words
myString = input("Enter a string: ")

# call the funciton and assign the output to result then print the result
result = capitalize_words(myString)
print("Capitalized String:", result)
