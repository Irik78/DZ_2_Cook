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
print(f'cook_book = {cook_book}')



def get_shop_list_by_dishes(dishes,person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                new_shop_list_item = dict(ingredient)
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingredient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    print(shop_list)