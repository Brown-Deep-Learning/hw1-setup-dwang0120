# Task: 
# Write up a Python class for a Square 
# whose constructor (the __init__ method) 
# takes in a string name and numeric length field.

class Square:
    def __init__(self, name, length):
        self.name = name
        self.length = length
    def __str__(self):
        return f"{self.name}, {self.length}"
square1 = Square("square1", 5)
square1.name == "square1"
square1.length == 5
#print(square1)


# Task: 
# Write up a Python class Multiplier 
# which, when called on two integers, 
# returns the product of the two integers
class Multiplier:
    def __call__(self, num1, num2):
        return num1 * num2
multer = Multiplier()
multer(5, 10)

# Task: Make a parent class named Logger
# and then
# In LoggingTape's constructor, 
# make an empty list called logs. 
# We'll store strings as messages of logs of whatever happened
# Then, in __enter__, 
# set Logger.logging_tape = self and return self. 
# We're setting a class level variable!
# Next, in __exit__, set Logger.logging_tape = None
# In add_to_log, append new_log to the end of logs.

class LoggingTape:
    def __init__(self):
        self.logs = [] # instance variable called logs
        
    def __enter__(self):
        Logger.logging_tape = self
        return self
        
    def __exit__(self, *args):
        Logger.logging_tape = None
    def add_to_log(self, new_log):
        self.logs.append(new_log)
    def print_logs(self):
        for log in self.logs: 
            print(log)
class Logger:
    logging_tape: LoggingTape | None = None

with LoggingTape() as tape: #runs LoggingTape's __enter__()
    #Logger.logging_tape is now defined as tape (from line 1)!
    tape.add_to_log("Hi!")
#runs LoggingTape's __exit__()
#Now Logger.logging_tape is defined as None
class Car(Logger):
    def travel(self, distance):
        self.logging_tape.add_to_log(f"Traveled Distance {distance}")
car = Car()
with LoggingTape() as tape: 
    car.travel(5)
tape.print_logs()