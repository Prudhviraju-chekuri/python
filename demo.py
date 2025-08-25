empty_set ={}
print(type(empty_set))

empty_set = set()
print(type(empty_set))

set_nums = {10,20,30,40,50,10,20}
list_num = [10,20,30,40,50]
tuple_num = (910,20,30,40,50)
print(set_nums)

print(hasattr(print(set_nums), '__getitem__'))
print(hasattr(print(list_num), '__getitem__'))
print(hasattr(print(tuple_num), '__getitem__'))

set_nums.update([80,90])
print(set_nums)

set_nums.update({100,110})
print(set_nums)

set_nums.remove(100)
print(set_nums)
set_nums.discard(60)
print(set_nums)

set_nums.clear()
print(set_nums)

set_nums = {10,20,30,40,50}
print(set_nums)
x = set_nums.pop()
print(set_nums)
set_nums.add(x)
print(set_nums)

set_copy = set_nums.copy()
print(set_nums)
print(set_copy)

s1= {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1)
print(s2)

s3 = s1.union(s2)
print(s3)
s1= {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.intersection(s2)
print(s3)
print(s1.intersection_update(s2))
print(s1)
print(s2)

s1= {1,2,3,4,5}
s2 = {4,5,6,7,8}
#s3 = s1 -s2
s3 = s1.difference(s2)
s4 = s2.difference(s1)
print(s3)
print(s4)

s3 = s1.difference_update(s2)
print(s1)
print(s2)
print(s3)

s1= {1,2,3,4,5}
s2 = {4,5,6,7,8}

s3 = s1.symmetric_difference(s2)
print(s3)
s1.symmetric_difference_update(s2)
print(s1)
print(s2)

s1= {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1.isdisjoint(s2))

s1= {1,2,3,4,5}
s2 = {6,7,8,9,10}

print(s1.isdisjoint(s2))

s1= {1,2,3,4,5}
s2 = {3,4,5}
s3 = {3,4,5,6}

print(s2.issubset(s1))
print(s3.issubset(s1))

s1= {1,2,3,4,5}
s2 = {3,4,5}
print(s1.issuperset(s2))
print(s2.issuperset(s1))
