# Задача №1
with open('cook_b.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredients = []
        quantity_ingredient = int(f.readline())
        for j in range(quantity_ingredient):
            ingredient_name, quantity, measure = f.readline().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
        f.readline()
        cook_book[dish_name] = ingredients
# print(f'cook_book = {cook_book}')

# Задача №2

def get_shop_list_by_dishes(dishes_list, person_count):
    shop_list = {}
    for dish in dishes_list:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[ingredient['ingredient_name']] = ({'measure': ingredient['measure'], 'quantity':
                                                                (ingredient['quantity'] * person_count)})
        else:
            print('Такого блюда нет в книге')
    return shop_list


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

# Задача №3:
with open('file_1.txt', 'r', encoding='utf-8') as file_1:
    line_1 = {}
    count_1 = 0
    for line in file_1.readlines():
        count_1 += 1
        line_1['file_1.txt'] = count_1
with open('file_1.txt', 'r', encoding='utf-8') as file_1:
    text_1 = file_1.read()

with open('file_2.txt', 'r', encoding='utf-8') as file_2:
    line_2 = {}
    count_2 = 0
    for line in file_2.readlines():
        count_2 += 1
        line_2['file_2.txt'] = count_2
with open('file_2.txt', 'r', encoding='utf-8') as file_2:
    text_2 = file_2.read()

with open('file_3.txt', 'r', encoding='utf-8') as file_3:
    line_3 = {}
    count_3 = 0
    for line in file_3.readlines():
        count_3 += 1
        line_3['file_3.txt'] = count_3
with open('file_3.txt', 'r', encoding='utf-8') as file_3:
    text_3 = file_3.read()

join = sorted(list(line_1.items()) + list(line_2.items()) + list(line_3.items()), key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as file_result:
    for line in join:
        file_result.write(f'{join[0][0]}\n {join[0][1]}\n {text_2}\n {join[1][0]}\n {join[1][1]}\n {text_1}\n'
                          f'{join[2][0]}\n {join[2][1]}\n {text_3}\n')

print(file_result)
