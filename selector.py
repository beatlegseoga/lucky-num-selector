import random

num_list = []
while len(num_list) <= 6:
    num = random.randint(1,45)
    if num not in num_list:
        num_list.append(num)

print(num_list)
