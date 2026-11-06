# 1.)
# n = int(input('n: '))
# def factorial(a):
#     factorial = 1
#     for i in range(0,a):
#         factorial *= (i+1)

#     return factorial

# print(factorial(n))

# 2.)
# sum1 = 0.0
# for i in range(0,n):
#     sum1 += (1/((i+1)**2))

# print(sum1)

# Do without math module
#  import math
# n = int(input('n: '))
# sum2 = 0.0
# for i in range(1,n+1):
#     sum2 += (math.log(i,math.e))/i

# print(sum2)

# import math
# # n = int(input('n: '))
# sum3 = 0.0
# for i in range(1, n+1):
#     sum3 += ((math.e)**i)/factorial(i)

# print(sum3)

# 3.)
# def fibonacci(a):
#     if a == 1:
#         return 0
#     if a == 2:
#         return 1
#     return fibonacci(a-1)+fibonacci(a-2)

# for i in range(1,21):
#     print(fibonacci(i))

# Next is Conditionals:

# Pnt = int(input("Percentage: "))

# cmp = Pnt/10
# if isinstance(cmp,int):
#     cmp = cmp - 1
# else:
#     cmp = int(cmp)

# grades = ['O','A','B','C','D','E','F']
# cmp_int = [9,8,7,6,5,4,3]

# for i in range(7):
#     if cmp_int[i] = cmp:
#         print(grades[i])

# Tuples
# lst1 = [1,2,3,4]
# lst2 = [2]

# lst = lst1 + lst2
# print(lst) 
# 

# tp1 = (1,2,3,4,5)
# tp2 = (6,7,8,9)
# # tp2.append(10) --> not allowed
# # tp1[0] =9
# tp3 = tp1 + tp2
# print(tp3)

# Dictionaries: {Key:value, key:value}

# student_profile = {
#     'Name':'Aditya',
#     'Age':120,
#     'Address':'DTU'
# }

# student_profile['ROLL'] = 19

# # print(student_profile)

# for item in student_profile:
#     print(student_profile[item])

# .keys()
# .values()
# .items

# print("""
# This is a 
# Multi line 
# comment""")

