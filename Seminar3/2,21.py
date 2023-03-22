# Задача №21.

# Напишите программу для печати всех уникальных значений в словаре. 

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Примечание: Список словарей задан изначально. 
# Пользователь его не вводит



# list_dictionaries = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
#                      {" V ":" S009 "}, {" VIII ":" S007 "}] 
# print(list_dictionaries)
# my_set = set()
# for dict_i in list_dictionaries:
#     for key in dict_i:
#         my_set.add(dict_i[key].strip())
# print(my_set)


list_dictionaries = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
                     {" V ":" S009 "}, {" VIII ":" S007 "}] 
print(list_dictionaries)
my_set = set()
for dict_i in list_dictionaries:
    for values in dict_i.values():
        my_set.add(values.strip())
print(my_set)