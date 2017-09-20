'''tup1 =()
fhand = open('TheVictors.txt', 'r')
for lines in fhand:
	lines = lines.rstrip()
	lst = lines.split()
	tup1 += tuple(lst)
#print(tup1)
print(sorted(tup1))
	#print(type(list_lines))
'''

# WORKS
'''
count = dict()
fhand = open('TheVictors.txt', 'r')
print(fhand)
for lines in fhand:
	words = lines.split()
	for word in words:
		count[word] = count.get(word,0) +1

lst = list()
for key, val in count.items():
	x = (val, key)
	lst.append(x)

lst = sorted(lst, reverse= True)

for val, key in lst[:15]:
	print(key,val)


'''


my_file = open('TheVictors.txt', 'r')
words = []
lines = []
my_dict = {}
for line in my_file:
    my_line = line.split()
    for word in my_line:
        if word not in words:
            words.append(word)
            my_dict[word] = 1
        else:
            my_dict[word] += 1
x = my_dict.items()
x = sorted([(value, key) for key, value in my_dict.items()], reverse = True)[:15]
for my_pair in x:
    print (my_pair[0], my_pair[1])
