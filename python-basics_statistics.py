#!/usr/bin/python3

SALES = [
    "Электрический чайник",
    "Тостер",
    "Фен для волос",
    "Фен для волос",
    "Тостер",
    "Тостер",
    "Фен для волос",
]

import collections, json

def create_ordered_sales_stats(sales_log):
    ''' Функция возвращает словарь, отсортированный по количеству вхождений товаров.
        На вход подается файл .json'''
        
    with open(sales_log) as sales_log:
        content = sales_log.read()
        sales_list = json.loads(content)
    sales_stats = collections.Counter(sales_list)
    ordered_sales_stats = dict(sales_stats.most_common())
    
    return ordered_sales_stats
    
def print_sales_stats(ordered_sales_stats):
    for name, count in ordered_sales_stats.items():
        print("{} - {}".format(name, count))

def main():
    sales_log = 'sales_log.json'
    sales_stats = create_ordered_sales_stats(sales_log)
    print_sales_stats(sales_stats)
    
    
if __name__ == '__main__':
  main()
