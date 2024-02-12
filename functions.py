# Inbuilt functions
number = max(89, 56, 34, 78, 45)
print(number)

x = min(56, 87, 46, 23, 90, 12)
print(x)

z = pow(2, 3)
print(z)


# User defined functions
def details():
    print("IMIL")


details()  # Calling a function


def student():
    name = "Roy"
    age = 18
    course = "MIT"
    print(name, age, course)


student()


# Parameters/variables and arguments/values
def students(name, age, course):
    print(name, age, course)


students("Roy", 17, "MIT")
students("Jack", 18, "Machine learning")
students("Pat", 19, "Cyber security")
students("Fri", 18, "Machine learning")
students("Jack", 18, "Machine learning")
students("Jack", 18, "Machine learning")
students("Jack", 18, "Machine learning")


# Create a user defined function called employees.
# It should display details of five employees.
# Parameters are fullname, age, gender, position, salary

def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)


employees("Ahmed Mahmoud", "34", "male", "CEO", "Ksh.500,000")
employees("Leandra Makuto", "27", "female", "Director", "Ksh.400,000")
employees("Jeremy Bizoo", "38", "male", "Supervisor", "Ksh.350,000")
employees("Alice Bernice", "24", "female", "Secretary", "Ksh.200,000")
employees("Sandra Kaggie", "17", "female", "Intern", "Ksh.150,000")
