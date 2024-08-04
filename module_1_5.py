immutable_var = 1, 2, "Alexandr", False
print(immutable_var)

#Если мы попытаемся изменить элемент кортежа на число 2024, то в результате увидим ошибку
#immutable_var [0] = 2024
#print(immutable_var)
#"~~~~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
#Вывод: кортеж не поддерживает обращение по элементам.

#Кортеж может хранить в себе изменяемые объекты (например: список)
immutable_var_list = ([1, 3, 5], 7)
print(immutable_var_list)
immutable_var_list[0][-1] = 2024
print(immutable_var_list)

#Также кортежи поддерживают два вида операций – конкатенацию и умножение
immutable_var2 = ([1, 3, 5], 7) + (1, 3)
print(immutable_var2)

immutable_var2 = ([1, 3, 5], 7) * 2
print(immutable_var2)
#-------------

mutable_list = ["bridge", "pile foundation", "asphalt concrete", 2024, 1996]
print(mutable_list)
print(mutable_list[1])
mutable_list[2] = "reconstruction"
mutable_list[-1] = 2025
print(mutable_list)
mutable_list.append("building")
print(mutable_list)
mutable_list.extend([True, 2026])
print(mutable_list)
mutable_list.remove(2024)
print(mutable_list)
print(2024 in mutable_list)
print("reconstruction" in mutable_list)
print("bridge" not in mutable_list)
print(mutable_list[1:6])