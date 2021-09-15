lst = [8, 2, 6, 4, 3, 1]
# Filter all elements <8
small = filter(lambda x: x < 8, lst)
print(list(small))
# Filter all even elements
even = filter(lambda x: x % 2 == 0, lst)
print(list(even))
# Filter all odd elements
odd = filter(lambda x: x % 2, lst)
print(list(odd))
