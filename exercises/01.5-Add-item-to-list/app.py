# Remember to import random function here
import random

my_list = [4, 5, 734, 43, 45]

# The magic goes below

for x in range(0,10):
    n = random.randint(0,20)
    my_list.append(n)

print(my_list)