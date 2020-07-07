def selectionSort(list):
    # iterate through the list and initialize the lowest value and index
    for i in range(len(list)):
        min = list[i]
        minIndex = i
        # iterate through the list from the point of the first for loop
        for j in range(i, len(list)):
            # find the minimum value and index and store them
            if list[j] < min:
                min = list[j]
                minIndex = j
        # swap the values of the lowest available index in order with the index of the lowest value
        list[i], list[minIndex] = list[minIndex], list[i]
        print(list)

newList = [8,5,2,6,9,3,1,4,0,7]
selectionSort(newList)