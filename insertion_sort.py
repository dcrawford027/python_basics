# iterate through array once, starting at location [1]
def insertionSort(list):
    for i in range(1, len(list)):
        # if the value of [i] is lower than the value before it, move values over until the one before [i] is less than [i] 
        temp = list[i]
        j = i
        while temp < list[j - 1]:
            # do not reference an index out of range
            if j == 0:
                break
            list[j] = list[j-1]
            j -= 1
        # and insert [i]
        list[j] = temp
        print(list)
# if the value of [i] is greater than the value before it, move on to the next iteration

insertionSort([6,5,3,1,8,7,2,4])