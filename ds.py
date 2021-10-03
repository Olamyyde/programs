letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(letters[-2])
print(letters[-3:])
print(letters[::2])

my_range=range(1,21)
print([10 * i for i in my_range])


print(list(map(str, my_range)))



d = {"a": 1, "b": 2}
print(d['b'])


f = {"a": 1, "b": 2, "c": 3}
print(f['a'] + f['b'])


s = {"a": 1, "b": 2}
s['c'] = 3
print(s)

print(sum(s.values()))


g = dict((key, value) for key, value in f.items() if value<=1)
print(g)




from pprint import pprint

j = {"a": list(range(1,11)), "b": list(range(11,21)), "c": list(range(21,31))}

pprint(j)
pprint(j['b'][2])


for key, value in j.items():
	print(f'{key} has value {value}')	


#script that prints out letters of the alphabet from a-z

import string

for letter in string.ascii_lowercase:
	print(letter)