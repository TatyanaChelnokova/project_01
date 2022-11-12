# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
from random import sample 

dct = my_favorite_songs
data = list(dct.items())
r = sample(data, 3)
print(r)

total_tame = 0

for tame in r:
    total_tame += tame[1]

    print(f'Три песни звучат - {total_tame} минут')
    
#     Отлично
