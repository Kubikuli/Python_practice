# s = '0123456789'

# print(s[0:5]) # 01234
# print(s[5:10]) # 56789
# print(s[0:10:2]) # 02468
# print(s[1:10:2]) # 13579
# print(s[::2]) # 02468
# print(s[1::2]) # 13579
# print(s[::-1]) # 9876543210
# print(s[::-2]) # 97531
# print(s[5:1:-1]) # 5432
# print(s[5:1:-2]) # 53
# print(s[5:1]) # empty string
# print(s[5:1:1]) # empty string
# print(s[5:1:-3]) # 52
# print(s[5:1:-4]) # 5
# print(s[5:1:-5]) # 5

# tuple1 = (1, 2, 3, 4, 5)

# print(tuple1[1])


# mcase = {'P': 300, 'R': 34, 'p': 65, 's': 3}

# mcase_frequency = {elem.lower(): sum(v for k, v in mcase.items() if k.lower() == elem.lower()) for elem in mcase}
# print(mcase_frequency)

# for elem in mcase:
#     print(elem)

# # expected output:  
# {'p': 365, 'r': 34, 's': 3}


# (r'''
#     ^(?!.*Jan|Vlk).*$
#     $
# ''')

# teststr1 = 'Ada;Bob;Bob;Ada;Cyril;Ada;Cyril'
# teststr2 = 'Dan@Ada@Ada@Dan@Cyril@Ed@Frank'

# used_by_both = set(name for name in teststr1.split(';') if name in teststr2.split('@'))

# for en in used_by_both:
#     print(en)


# import collections
# flights = [('Brno', 'London'), ('Ostrava', 'Split'), ('Brno', 'Berlin')]
# routes = collections.defaultdict(list)

# for (origin, destination) in flights:
#     routes[origin].append(destination)

# reversed_routes = {tuple(dest):orig for orig, dest in routes.items()}

# print(reversed_routes)

# how_many_found = 0
# for plate in stolen_plates:
#     if plate in login2plate.values():
#         how_many_found += 1

# import re

# slova = re.split(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', 'myVATParserMoje')

# print(slova)


# def find_dupes(*numbers):
#     seen = set()
#     duplicates = []
#     added = set()
    
#     for num in numbers:
#         if num in seen and num not in added:
#             duplicates.append(num)
#             added.add(num)
#         seen.add(num)
    
#     return duplicates[::-1]  # Reverse the order


# print(find_dupes(1, 2, 3, 2, 1, 3, 4, 5, 1))

# from itertools import product
# d2l = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs'}

# digits = '234'

# final = [''.join(p) for p in product(*(d2l[d] for d in digits))]

# print(final)


