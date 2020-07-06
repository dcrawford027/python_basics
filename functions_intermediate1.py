import random

def randInt(min=0, max=100):
    if max < min:
        return "your high limit is less than your lower limit"
    elif min < 0:
        return "the low number cannot be negative"
    num = random.random() * (max - min) + min
    return round(num)

# print(randInt())                   # should print a random integer between 0 to 100
# print(randInt(max=50)) 	         # should print a random integer between 0 to 50
# print(randInt(min=50)) 	         # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500