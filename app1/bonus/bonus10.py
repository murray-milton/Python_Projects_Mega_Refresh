import time

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))


# Sample data
set1 = set(range(1000))
set2 = set(range(500, 1500))
list1 = list(set1)
list2 = list(set2)

# Union
start_time = time.time()
union_set = set1.union(set2)
print("Set Union Time:", time.time() - start_time)

start_time = time.time()
union_list = list(set(list1 + list2))
print("List Union Time:", time.time() - start_time)

# Intersection
start_time = time.time()
intersection_set = set1.intersection(set2)
print("Set Intersection Time:", time.time() - start_time)

start_time = time.time()
intersection_list = [x for x in list1 if x in set2]
print("List Intersection Time:", time.time() - start_time)

# Difference
start_time = time.time()
difference_set = set1.difference(set2)
print("Set Difference Time:", time.time() - start_time)

start_time = time.time()
difference_list = [x for x in list1 if x not in set2]
print("List Difference Time:", time.time() - start_time)

dictionary_types = {"list": list, "set": set, "tuple": tuple}
