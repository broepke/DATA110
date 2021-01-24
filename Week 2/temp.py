

alist = [6, 8, 12, 13]
alist[3] % alist[1]

# list
l1 = [1,2,3,4]
l2 = [1,3,2,4]
l1==l2
l1.append('five')
l1.remove('five')
print(len(l1), len(l2))
l2[3]


# tuple
numTup = ("one", 2, "three", 4, "five", 5, 4)
numTup[2:5]


# set
numSet = {"one", 2, "three", 4, "five", 5, 4}

snakes = set(['cobra', 'viper', 'python']) 


print(len(numSet), len(snakes))
print(numSet)
snakes.add('rattler')

snakes.remove('ratter')   # error
snakes.discard('ratter')  # no error

for s in snakes:
    print(s, end=' ')
    #print(s)


# dictionary
student1 = dict(first= 'John', 
               last= 'Doe',
               id= 1234,
               major= 'DA')

student2 = {'first': 'John',
           'last': 'Doe',
           'id': 1234,
           'major': 'DA'}

student1==student2
print(student1)

student2.get('first')
student2['gpa'] = 4.0
myKeys = student2.keys() # dict_keys object presents a list of a dictionary's keys.
myValues = student2.values()




# user input
genre = input('Enter genre : ')   	    # get user input and assign to genre
keys = ['title', 'year', 'rating']   	# list of keys
values = []                       		# empty list of values
title = input('Enter movie title: ') 	# get user input and assign to title
values.append(title)                   	# append to values list
year = int(input('Enter movie year: ')) # get user input and assign to year, converted to int
values.append(year)
rating = float(input("Enter movie rating: "))
values.append(rating)

print(title, year, rating)


# exception handling
user_input = 0
ok=False
while not ok:
  user_input = input("What is your Age? ")
  try:
     val = int(user_input)
     ok = True
  except ValueError:
     print("Invalid type. Please try again ")








# n-D lists
matrix = [['c1', 'c2', 'c3'], 
          [1, 2, 3], 
          [4, 5, 6]]

c1 = matrix[0][0]
c2 = matrix[0][1]
c3 = matrix[0][2]
print(c1, c2, c3, '\n')

r1c1 = matrix[1][0]
r1c2 = matrix[1][1]
r1c3 = matrix[1][2]
print (r1c1, r1c2, r1c3, '\n')

# print all elements of the matrix
for row in matrix:
    for e in row:
        print(e, end=' ')
    print()
    
l = [1,1,2,3]

tup = ( 'apple', 'orange', 'peach', 'apple')
myset = {'apple', 'orange', 'peach', 'apple'}