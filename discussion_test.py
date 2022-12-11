class Person:
    "This is a person class"
    age = 25

    def greet(self):
        print('Hello')


# create a new object of Person class
michael = Person()

# Output: <function Person.greet>
print(Person.greet)

# Output: <bound method Person.greet of <__main__.Person object>>
print(michael.greet)

# Calling object's greet() method
# Output: Hello
michael.greet()