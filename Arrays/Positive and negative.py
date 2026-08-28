array = [1, -9, 2, 4, 9, -8, -4]

positive = []
negative = []


for num in array:
    if num>=0:
        positive.append(num)

    else:
        negative.append(num)

print(positive + negative)