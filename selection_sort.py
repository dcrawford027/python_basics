def selectionSort(list):
    for i in range(len(list)):
        min = list[i]
        minIndex = i
        for j in range(i, len(list)):
            if list[j] < min:
                min = list[j]
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
        print(list)

newList = [8,5,2,6,9,3,1,4,0,7]
selectionSort(newList)