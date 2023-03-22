# *Задача 20: 
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12
    
# от себя добавила возможность на вход подавать несколько слов как с русскими так и английскими буквами


LETTER_PRICE = [
    {
        "price": 1,
        "letters": [
            "A", "E", "I", "O", "U", "L", "N", "S", "T", "R",
            "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"
        ]
    },
    {
        "price": 2,
        "letters": [
            "D", "G",
            "Д", "К", "Л", "М", "П", "У"
        ]
    },
    {
        "price": 3,
        "letters": [
            "B", "C", "M", "P",
            "Б", "Г", "Ё", "Ь", "Я"
        ]
    },
    {
        "price": 4,
        "letters": [
            "F", "H", "V", "W", "Y",
            "Й", "Ы"
        ]
    },
    {
        "price": 5,
        "letters": [
            "K",
            "Ж", "З", "Х", "Ц", "Ч"
        ]
    },
    {
        "price": 8,
        "letters": [
            "J", "X",
            "Ш", "Э", "Ю"
        ]
    },
    {
        "price": 10,
        "letters": [
            "Q", "Z",
            "Ф", "Щ", "Ъ"
        ]
    }
]


def get_letter_price(letter):
    price = 0
    for item in LETTER_PRICE:
        if letter in item['letters']:
            price = item['price']
            break
    return price


def get_word_price(word):
    price = 0
    word = word.upper()
    for letter in word:
        price += get_letter_price(letter)
    return price


def get_phrase_price(phrase):
    result = []
    allPrice = 0
    words = phrase.split()
    for word in words:
        price = get_word_price(word)
        result.append({
            'price': price,
            'word': word
        })
        allPrice += price
    return {
        'totalPrice': allPrice,
        'words': result
    }


word = input('Ведите фразу: ')
result = get_phrase_price(word)
totalPrice = result['totalPrice']
print(f'Общая стоимость фразы {totalPrice}')
words = result['words']
for item in words:
    price = item['price']
    word = item['word']
    print(f'Стоимость слова \'{word}\' - {price} очков')
