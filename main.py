from random import randint


def bubble_sort(array):
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                sort = array[j]
                array[j] = array[j+1]
                array[j+1] = sort


N = 10
a = []
for i in range(N):
    a.append(randint(1, 1000))

print(a)
bubble_sort(a)
print(a)


def binary_search(N_list, number):
    N = 1000
    first = 0
    last = N_list - 1
    while first < last:
        middle = (first + last) // 2
        if N_list[middle] == number:
            return middle
        elif N_list[middle] < number:
            first = middle + 1
        else:
            last = middle - 1
            return -1
        N_list = sorted([345, 23, 567, 8, 95, 956, 12, 45, 634, 713])
        number = 5
        print(binary_search(N_list, number))