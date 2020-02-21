#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup
from math import ceil

def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')

    tds = soup.find('table').find_all('td')
    links = []
    for td in tds:
        links.append(td.text.strip())
    slised_links = []
   
    # by_num = 4
    # for x in range(0, len(links), by_num):
    #     if x + by_num > len(links):
    #         by_num = len(links)-x
    #     template = ''.join(['{:>2} {}']*by_num)
    #     print(template.format(*[j for i in zip(range(x, x+by_num), links[x:x+by_num]) for j in i]))
    #     # slised_links.append(template.format(*[j for i in zip(range(x, x+by_num), links[x:x+by_num]) for j in i]))
    
    
    lst = list(range(len(links)))

    row_count = ceil(len(lst) / 4)
    for r in range(row_count):
        slised_links.append(links[r])
        print(r)
    return  slised_links
    #задача из листа в 800 элементов сделать 4 колонки 

# def write_in_csv(links):
#     with open('writerts.csv','w') as file:
#         writer = csv.writer(file)
#         writer.writerow(links)

if __name__ == "__main__": 
    url = "https://worldtable.info/literatura/tablica-gody-zhizni-russkih-pisatelei-i-poyet.html"
    table = get_all_links(get_html(url))
    # write_in_csv(table)
    print(table)
