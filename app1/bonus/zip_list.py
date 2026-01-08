fruits = ["apple", "banana", "cherry"]
weights = [10, 20, 30]

weight_fruit = zip(fruits, weights)  # will return a tuple by default
for item in weight_fruit:
    print(item)
