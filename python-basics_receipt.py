#!/usr/bin/python3

PRODUCTS = [
   # название, цена
   [ 'яблоки', 100 ],
   [ 'швейцарский сыр', 1500 ],
   [ 'красная и очень дорогая рыба', 450 ],
   [ 'морской окунь холодного копчения', 12400 ]
]

def create_formatted_receipt(products):
    """Функция создает новый чек, принимает на вход любой список покупок - `products`.
    
    Функция сама не вызывает `print`, только готовит строки к последующему
    выводу на экран или печати."""

    receipt_lines = []
    
    receipt_width = 30
    text_width = receipt_width - 2 # '|' по краям -> 2 символа
    price_width = 10 # '99999' -> 5 символов, ' руб.' -> 5 символов
    name_width = receipt_width - price_width - 3 # '|' + ' ' + '|' -> 3 символа
    
    horizontal_line = ' ' + ('-' * text_width) + ' '
    empty_line = '|' + (' ' * text_width) + '|'
    
    # верхняя граница рамки
    receipt_lines.append(horizontal_line)
    receipt_lines.append(empty_line)
    
    # вывод позиций в чеке
    for product_name, product_price in PRODUCTS:
        if len(product_name) > name_width:
            product_name = product_name[:name_width - 3] + '...'
        product_name = product_name.ljust(name_width)
        
        product_price = str(product_price) + ' руб.'
        product_price = product_price.rjust(price_width)
        
        receipt_lines.append('|' + product_name + ' ' + product_price + '|')
    
    # нижняя граница рамки        
    receipt_lines.append(empty_line)
    receipt_lines.append(horizontal_line)
   
    return receipt_lines

def print_all_lines(lines):
    for line in lines:
        print(line)

if __name__ == '__main__':
    receipt = create_formatted_receipt(PRODUCTS)
    print_all_lines(receipt)
