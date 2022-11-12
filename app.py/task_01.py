# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
print(my_favorite_songs[:14],  end=' ' )
print(my_favorite_songs[-13:], end=' ')
print(my_favorite_songs[16:30], end = ' ')
print(my_favorite_songs[51:-15])

# Да, ваше решение рабочее, но мы могли бы его улучшить. 
# Например, не вручную посчитать индекс строки, а попробовать найти индекс через метод для строк find и rfind

# Решение с помощью индекции строк

first_song = my_favorite_songs [
    : my_favorite_songs.find(',')
]

last_song = my_favorite_songs [
    my_favorite_songs.rfind('A') :
]

second_song = my_favorite_songs[
     my_favorite_songs.find('N') : 
     my_favorite_songs.find(', S')
]

previous_song = my_favorite_songs [
    my_favorite_songs.rfind('O') : my_favorite_songs.rfind(',')
    ]

print(first_song, last_song, second_song, previous_song)


# Второй вариант, мы можем воспользоваться методом разделения строк по символам. split.
# Полученный в результате список проиндексируем по песням

# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
