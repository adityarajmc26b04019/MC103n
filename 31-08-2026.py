#indexing

# str = 'Python'

# print(str[-3:])
# print(str[:-2])

# print(str[::2])
# How It Works
# Python uses slice syntax in the format [start:end:step].
# The start defaults to the beginning of the string (index 0).
# The end defaults to the end of the string.
# The step value of 1 means it moves forward by one character at a time, keeping the entire string unchanged.

# str = 'Hello World'
# print(str[::-1])

# How It Works
# The expression [::-1] uses Python's extended slicing syntax, which follows the format [start:stop:step]
# start is omitted, so it defaults to the end of the string when the step is negative.
# stop is omitted, so it goes all the way to the beginning of the string.
# step is set to -1, which tells Python to traverse the string backward, one character at a time.

# As a result, the entire string is reversed.

# line = 'Python is  a programming language.'
# print(line.split(' '))
# print(line.replace('i','z'))
# print(line.swapcase())
# print(line.find('i'))

# Strings are immutable.

#lists: 

# cities = ['Delhi','Mumbai','Kolkata']
# print(cities[0])
# print(cities[-1])
# cities.sort() # method
# print(sorted(cities)) # function
# cities.reverse()
# print(cities)
# cities.append('Jaipur')
# print(cities)
# cities.insert(2,'Chennai')
# print(cities)
# del(cities[1])
# print(cities)
# city = cities.pop()
# print(cities)
# print(city)
# cities.remove('Kolkata')
# print(cities)
# cities.sort()
# print(cities)
# print(sorted(cities))
# cities.reverse()
# print(cities)
# print(cities[::-1])
# print(cities[0:2])

# Looping
# for i in range(1,5):
#     print(i)

# for i in range(7):
#     print(i)

# for i in range(1,11):
#     print(i**2)

# for i in range(2,11,2):
#     print(i)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for i in range(11):
#     squares.append(i**2)

# print(squares)

# squares = [i**2 for i in range(11)]
# print(squares )

# even_number = [i for i in range(50,101,2)]
# print(even_number)

# squares = list(i**2 for i in range(11))
# squares = [i**2 for i in range(11)]
# print(squares)

cities = True
# print(cities is True)
# print(cities is not True)
print(cities == False)
print(cities != True)