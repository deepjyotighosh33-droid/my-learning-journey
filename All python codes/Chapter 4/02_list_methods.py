friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(type(friends))
print(friends)

# adding values at the end

friends.append("DJ")
print(friends)

# adding value in which index you want

friends.insert(3, "Detro")
print(friends)

# Deleting

friends.pop(3) # or </> print(l1.pop(3))
print(friends)

# putting numbers in increasing order using sort

l1 = [1, 34, 62, 2, 6, 11]
l1.sort()
print(l1)

# just rotates the list or reverses it

l2 = [1, 34, 62, 2, 6, 11]
l2.reverse()
print(l2)