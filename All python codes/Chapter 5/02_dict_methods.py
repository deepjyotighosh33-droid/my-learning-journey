marks = {
    "DJ": 100,
    "Harry": 56,
    "Rohan": 23,
    0: "Shubham"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.get("Harry"))

marks.update({"Harry": 57, "Renuka": 40})
print(marks)

# xxx

my_dict = {'a': 1, 'b': 2} 
my_dict.clear()
print(my_dict)  # Output: {}

original = {'a': 1, 'b': 2}
copied_dict = original.copy()
print(copied_dict)  # Output: {'a': 1, 'b': 2}

my_dict = {'a': 1, 'b': 2}
value = my_dict.get('a', 0)  # Output: 1
missing_value = my_dict.get('c', 0)  # Output: 0

my_dict = {'a': 1, 'b': 2}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])

my_dict = {'a': 1, 'b': 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])

my_dict = {'a': 1, 'b': 2}
print(my_dict.values())  # Output: dict_values([1, 2])

my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('a')  # Output: 1
print(my_dict)  # Output: {'b': 2}

my_dict = {'a': 1, 'b': 2}
item = my_dict.popitem()  # Output: ('b', 2)
print(my_dict)  # Output: {'a': 1}

my_dict = {'a': 1}
value = my_dict.setdefault('b', 2)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'b': 2}

my_dict = {'a': 1}
my_dict.update({'b': 2})
print(my_dict)  # Output: {'a': 1, 'b': 2}





