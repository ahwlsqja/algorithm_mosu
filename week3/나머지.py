my_list = []
for i in range(0, 10):
    n = int(input())
    aa = n % 42

    my_list.append(aa)

print(len(set(my_list)))