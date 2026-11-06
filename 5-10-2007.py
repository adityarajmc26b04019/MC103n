# # def fullname(first_name,last_name,middle_name = ' '):
# #     return first_name + middle_name + last_name

# # print(fullname('Aditya','Raj'))

# def student_list(*names):#arbitary number of argument
#     print(names)

# student_list('John','Tony','Steve')

# def user_profile(**key_value):
#     dict1 = dict()
#     for item in key_value:
#         dict1[item] = key_value[item]
#     print(dict1)

# user_profile(f_name ='Aditya', l_name = 'Raj', College ='DTU', year = 'first')


#Exceptions
# while True:
#     try:
#         p = int(input("Enter 1st number: "))
#         q = int(input("Enter 2nd number: "))
#         break
#     except:
#         # print("Try Again")

# try:
#     p = int(input("Enter 1st number: "))
#     q = int(input("Enter 2nd number: "))
# except:
#     print("You can't divide by zero and please enter integer.")
# else:
#     print(p/q)
# finally:
#     print('Done')

# x = "Aditya"
# print(x[::-1])

# a = 1
# a += 1
# print(a)