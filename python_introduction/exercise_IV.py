"""
Write a Python program to count the members of a list and print them
"""
test = [1, 5, 6, 1, 1, 's', 's', 'hola']

lst_ = []
for i in range(len(test)):
    lst = 0
    for j in range(len(test)):
        if test[i] == test[j]:
            lst += 1
    lst_.append(lst)

zip_ = zip(test, lst_)
list_zip = list(zip_)
res = list(set(list_zip))

for t in range(len(res)):
    print(f"{res[t][0]} >>> {res[t][1]}")
