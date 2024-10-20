from pprint import pprint


#Задание N 1
def cook_book(file_name):
    """на выходе функции получим словарь с рецептами."""
    cook_book = {}
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            if not dish_name:
                continue
            count = int(next(f).strip())
            ingr_list = []
            for i in range(count):
                ingr_name, quantity, measure = next(f).strip().split(' | ')
                ingr_list.append({'ingredient_name': ingr_name, 'quantity': int(quantity), 'measure': measure})
            cook_book[dish_name] = ingr_list
    return cook_book


#Задание N 2
def get_shop_list_by_dishes(dishes, person_count):
    """на выходе функции получим словарь с названием ингредиентов и его количества для блюда."""
    shop_list = {}
    for dish in dishes:
        for item in cook_book('dishes.txt')[dish]:
            if item['ingredient_name'] not in shop_list:
                shop_list[item['ingredient_name']] = {}
                shop_list[item['ingredient_name']]['measure'] = item['measure']
                shop_list[item['ingredient_name']]['quantity'] = item['quantity'] * person_count
            else:
                shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count
    return shop_list


pprint(cook_book('dishes.txt'))
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


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
