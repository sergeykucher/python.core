# Task 1

# Спробуйте переписати наступний код через map.
# Він приймає список реальних імен і замінює їх хеш-прізвищами,
# використовуючи  більш надійний метод-хешування.

names = ['Sam', 'Don', 'Daniel'] 
names = list(map(hash,names))
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
print(names) 


# Вивести список кольору “red”, який найчастіше зустрічається в даному списку
#  [“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ]
#  використовуючи функцію filter

list_colors = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow' ]
red_colors = list(filter(lambda color: color=='red', list_colors))
print(red_colors)

# Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’],
# перетворити цей список  в список, всі числа якого мають тип даних integer:
#  1) використовуючи метод  append
#  2) використовуючи метод  map

list_str = ['1','2','3','4','5','7']
list_int1 = []
for value in list_str:
    list_int1.append(int(value))
print(list_int1)

list_int2 = list(map(int,list_str))
print(list_int2)

# Перетворити список, який містить милі,
# в список, який містить кілометри (1 миля=1.6 кілометра)
#  a) використовуючи функцію map
#  b) використовуючи функцію map та lambda

list_miles = [56, 85, 34, 20]

def imperial_to_metric(value):
    return round(value*1.6,2)

list_kmeters1 = list(map(imperial_to_metric,list_miles))
print(list_kmeters1)

list_kmeters2 = list(map(lambda mile: round(mile*1.6,2),list_miles))
print(list_kmeters2)