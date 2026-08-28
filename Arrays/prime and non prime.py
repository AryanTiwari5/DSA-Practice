array = [1, 2, 5, 8, 9, 4]

odd_count = 0
even_count = 0

for num in array:
    if num%2 == 0:
        even_count += 1
    else:
        odd_count+= 1

print(odd_count)
print(even_count)