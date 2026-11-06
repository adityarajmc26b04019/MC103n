dim_1 = (15,15,25)

print("Surface_Area: ", 2*(dim_1[0]*dim_1[1] + dim_1[1]*dim_1[2] + dim_1[2]*dim_1[0]))
print("Volume: ", dim_1[0]*dim_1[1]*dim_1[2])

dim_2 = list(dim_1)
dim_2[2] += 25

print(dim_2)
print(min(dim_2),max(dim_2),sum(dim_2))

if sum(dim_2) < 50:
    print("Sum of sides is less than 50")
elif sum(dim_2) >= 50 and sum(dim_2) <100:
    print("Sum of sides lies between 50 and 100")
else:
    print("Sum of sides is greater than or equal to 100")