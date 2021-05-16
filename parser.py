from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from selenium import webdriver
from lxml import html
from selenium.webdriver import DesiredCapabilities
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import time

DOMAIN = 'vk.com'
HOST = 'http://' + DOMAIN
FORBIDDEN_PREFIXES = ['#', 'tel:', 'mailto:']
links = set() # множество всех ссылок
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(HOST, headers=headers)

chrome_options = webdriver.ChromeOptions()
# директория сохранения профиля
chrome_options.add_argument("--user-data-dir=C:/Users/galya/PycharmProjects/pythonProject11")
#dcap = dict(DesiredCapabilities.CHROME)
chrome = webdriver.Chrome('D:\\chromedriver\\chromedriver.exe')

chrome.get(HOST)
times = []

def add_all_links_recursive(url, maxdepth=1):

    #глубина рекурсии не более `maxdepth`

    # список ссылок, от которых в конце мы рекурсивно запустимся
    links_to_handle_recursive = []
    #получаем html код страницы
    request = requests.get(url, headers=headers)
    # парсим его с помощью BeautifulSoup
    soup = BeautifulSoup(request.content, 'lxml')
    # рассматриваем все теги <a>, при том, что href - не пустые
    for tag_a in soup.find_all('a', href=lambda v: v is not None):
        link = tag_a['href']

        # если ссылка не начинается с одного из запрещённых префиксов
        if all(not link.startswith(prefix) for prefix in FORBIDDEN_PREFIXES):
            # проверяем, является ли ссылка относительной
            if link.startswith('/') and not link.startswith('//'):
                # преобразуем относительную ссылку в абсолютную
                link = HOST + link
            # проверяем, что ссылка ведёт на нужный домен
            # и что мы ещё не обрабатывали такую ссылку
            if urlparse(link).netloc == DOMAIN and link not in links:
                links.add(link)
                links_to_handle_recursive.append(link)

    if maxdepth > 0:
        for link in links_to_handle_recursive:
            add_all_links_recursive(link, maxdepth=maxdepth - 1)

def main():
    print("\nSite: " + DOMAIN)
    urls = []
    add_all_links_recursive(HOST + '/')
    for link in links:
        start = time()
        result = chrome.get(link)
        end = time()
        urls.append(link)
        times.append(end - start)
        s = end - start;

    print("\n")
    # Ограничение вывода строк - максимум 10 000 (чтобы не выводило многоточия)
    pd.options.display.max_rows = 10000
    df = pd.DataFrame({'URL': urls, 'Time of open, sec': times})
    print(df)
    writer = pd.ExcelWriter('C:/Users/galya/Desktop/Data parsing/testing.xlsx')
    df.to_excel(writer, 'Лист1')
    writer.save()
    print(" Домены с временем их открытия выгружены в таблицу Excel в папке Data parsing.")


if __name__ == '__main__':
    main()
