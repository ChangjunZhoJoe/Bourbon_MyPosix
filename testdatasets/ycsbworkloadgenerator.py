import random
import string

# number_of_keys = 30000 # 300, -n 57
# number_of_keys = 3000000 # 3 million, -n 2920
number_of_keys = 100000000 # 100 million, -n 97500
# number_of_keys = 10000000 # 10 million, -n 19531
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
ycsbops = []
existingKeys = []
for i in range(1,number_of_keys-1):
    if(i < 1000 or i%2 == 0):
        ycsbops.append("1 "+ str(i) + "\n")
        existingKeys.append(str(i))
    else:
        ycsbops.append("0 "+random.choice(existingKeys)+"\n")
    

print("total operations: ", len(ycsbops))
f.writelines(ycsbops)
f.close()