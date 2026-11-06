my_profile = {
    'Name':'Adi',
    'RegNo.':12344,
    'Address':'DTU',
    'DOB':'09/11/2004',
    'Height': 160
}

print(my_profile)

my_profile.pop('Height')
print(my_profile)
my_profile['Fav_Language'] = 'C'

print(f"Hello, my name is {my_profile['Name']}. My favorite programming language is {my_profile['Fav_Language']}.")

for i in my_profile.keys():
    print(i)
for j in my_profile.values():
    print(j)
for k in my_profile.items():
    print(k)