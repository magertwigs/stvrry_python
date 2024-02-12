# Data Types
number = 45  # int
num = 56.78  # float
greeting = "Hello there"  # str
isPythonInteresting = True  # bool

# Variable storing multiple values
languages = ["python", "php", "java"] # list
fruits = ("apple", "banana", "pineapple") # tuple
countries = {"Kenya", "China", "USA"} # set

# Dictionary
details = {
    "firstname" : "Roy",
    "age" : 15,
    "course" : "MIT",
    "nationality" : "Russian"
}

print(number)
print(greeting)
print(countries)
print(isPythonInteresting)
print(details)
print(details["course"])
print(details["nationality"])

# Determining the data type
print(type(details))
print(type(countries))

# Type casting - Converting one data type to another
print(float(number))
print(int(num))



