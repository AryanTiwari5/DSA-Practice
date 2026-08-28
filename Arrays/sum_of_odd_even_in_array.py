array = [1, 4, 5, 6, 9, 0]

even_sum = 0
odd_sum = 0

for num in array:
    if num%2 == 0:
        even_sum += num
    else:
        odd_sum+=num

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)