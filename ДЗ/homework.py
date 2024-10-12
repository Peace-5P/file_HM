


#Задание N 1 и 2
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубчик'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ],
  'Фахитос': [
    {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
    {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}]
  }

def get_shop_list_by_dishes(dishes, person_count):
    """на выходе функции получим словарь с названием ингредиентов и его количества для блюда."""
    shop_list = {}
    for dish in dishes:
        for item in cook_book[dish]:
            if item['ingredient_name'] not in shop_list:
                shop_list[item['ingredient_name']] = {}
                shop_list[item['ingredient_name']]['measure'] = item['measure']
                shop_list[item['ingredient_name']]['quantity'] = item['quantity'] * person_count
            else:
                shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count
    return shop_list

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))


#Задание N 3
with open('final_file.txt', 'w', encoding='utf-8') as outfile:
    files = ['1.txt', '2.txt', '3.txt']
    files.sort(key=lambda file_name: sum(1 for line in open(file_name, 'r', encoding='utf-8')))
    for file_name in files:
        with open(file_name, 'r', encoding='utf-8') as infile:
            outfile.write(file_name + '\n')
            outfile.write(str(len(infile.readlines())) + '\n')
            infile.seek(0)
            outfile.write(infile.read())
        outfile.write('\n')
