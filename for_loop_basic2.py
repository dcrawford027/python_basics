# Given a list, write a function that changes all positive numbers in the list to "big". Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggieSize(list):
    for i in range(len(list) - 1):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggieSize([-1, 3, 5, -5]))

# Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number). Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def countPositives(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
    list[len(list) - 1] = count
    return list
print(countPositives([-1,1,1,1]))

# Create a function that takes a list and returns the sum of all the values in the list. Example: sum_total([1,2,3,4]) should return 10 Example: sum_total([6,3,-2]) should return 7
def sumTotal(list):
    sum = 0
    for i in list:
        sum += i
    return sum
print(sumTotal([6,3,-2]))

# Create a function that takes a list and returns the average of all the values.x Example: average([1,2,3,4]) should return 2.5
def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)
print(average([1,2,3,4]))

# Create a function that takes a list and returns the length of the list. Example: length([37,2,1,-9]) should return 4 Example: length([]) should return 0
def length(list):
    return len(list)
print(length([37,2,1,-9]))

# Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False. Example: minimum([37,2,1,-9]) should return -9 Example: minimum([]) should return False
def minimum(list):
    if len(list) == 0:
        return False
    else:
        min = list[0]
        for i in list:
            if i < min:
                min = i
    return min
print(minimum([37,2,1,-9]))

# Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False. Example: maximum([37,2,1,-9]) should return 37 Example: maximum([]) should return False
def maximum(list):
    if len(list) == 0:
        return False
    else:
        max = list[0]
        for i in list:
            if i > max:
                max = i
    return max
print(maximum([37,2,1,-9]))

# Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list. Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimateAnalysis(list):
    newDict = {}
    sumTotal = 0
    minimum = list[0]
    maximum = list[0]
    for i in list:
        sumTotal += i
        if i < minimum:
            minimum = i
        elif i > maximum:
            maximum = i
    newDict['sumTotal'] = sumTotal
    newDict['average']  = sumTotal / len(list)
    newDict['minimum']= minimum
    newDict['maximum'] = maximum
    newDict['length'] = len(list)
    return newDict
print(ultimateAnalysis([37,2,1,-9]))

# Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.) Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverseList(list):
    for i in range(len(list)//2):
        temp = list[i]
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 -i] = temp    
    return list
print(reverseList([37,2,1,-9]))