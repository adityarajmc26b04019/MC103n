# Exercise:

fruits = ['apple','banana','cherry','mango','grape']
print(len(fruits)) # no of fruits

# fruits = ['apple','banana','cherry','mango','grape']
fruits.append('orange')
print(fruits)

# fruits = ['apple','banana','cherry','mango','grape']
fruits.sort()
print(fruits)

# fruits = ['apple','banana','cherry','mango','grape']
fruits.sort(reverse = True)
print(fruits)

# fruits = ['apple','banana','cherry','mango','grape']
fruits.insert(2,'kiwi')
print(fruits)

# fruits = ['apple','banana','cherry','mango','grape']
fruits.remove('banana')
print(fruits)

# fruits = ['apple','banana','cherry','mango','grape']
fruits.pop()
print(fruits)

# fruits = ['apple','banana','cherry','mango','grape']
print(fruits[:2])

# fruits = ['apple','banana','cherry','mango','grape']
print(fruits[1:])

# fruits = ['apple','banana','cherry','mango','grape']
print(fruits[1:len(fruits)-1])