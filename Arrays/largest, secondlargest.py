array = [1, 2, 4, 5, 6]
largest = array[0]
for i in range(1, len(array)):
    if array[i] > largest:
        largest = array[i]

print(largest)
slargest = -1
for j in range(1, len(array)):
    if array[j]>slargest and array[j] != largest:
        slargest = array[j]

print(slargest)
