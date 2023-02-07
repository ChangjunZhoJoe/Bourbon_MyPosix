import random
import string


number_of_keys = 3000000
number_of_operation_multiplier = 4
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str


f = open("keyfile.txt", "a")
keys = []
for i in range(number_of_keys):
    keys.append(get_random_string(16)+"\n")

f.writelines(keys)
f.close()

f = open("ycsbworkload.txt", "a")
whichKey = []
for i in range(1,number_of_keys-1):
    whichKey.append("1 "+ str(i) + "\n")

print(len(whichKey))
for i in range(number_of_operation_multiplier):
    f.writelines(whichKey)
f.close()