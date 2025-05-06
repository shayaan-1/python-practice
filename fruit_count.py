def fruit_count(list):
    map = {}
    for fruit in list:
        if fruit in map:
            map[fruit] += 1
        else:
            map[fruit] = 1
    return map

print(fruit_count(['apple', 'banana', 'orange', 'apple', 'banana', 'banana']))