numbers = []

for i in range(9):
    numbers.append(int(input()))

max_value = max(numbers)
max_position = numbers.index(max_value) + 1

print(max_value)
print(max_position)