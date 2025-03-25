my_list = []

my_list.extend([10, 20, 30, 40])

my_list.insert(1, 15)

my_list.extend([50, 60, 70])

my_list.pop()

my_list.sort()

index_found = my_list.index(30)
print(f"The index of {30} in my_list is {index_found}.")