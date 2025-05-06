# Write a program that takes a list of fruits (e.g. ["apple", "banana", "apple", "mango"]) and counts how many times each fruit appears.

# Store results in a dictionary like:
# {"apple": 2, "banana": 1, "mango": 1}

def fruit_count(list):
    map = {}
    for fruit in list:
        if fruit in map:
            map[fruit] += 1
        else:
            map[fruit] = 1
    return map

print(fruit_count(['apple', 'banana', 'orange', 'apple', 'banana', 'banana']))