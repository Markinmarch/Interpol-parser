'''
Метод реализует запрос данных по ссылкам из красного
или жёлтого списков с последующим запросом и записью
в файл "data_persons" фотографий с профилей. На вход
принимает драйвер, класс подключения к БД.
    driver : класс драйвера (webdriver.Chrome() или webdriver.Firefox())
    links_cache : класс подключения к БД Redis "links_list"
'''


import time
import requests
import logging

from main_parser.app.links_persons import list_persons


def get_photo(
    driver,
    links_cache
):
    logging.info('--- Loading photo persons ---')
    for red_ready_link in list_persons(links_cache):
        driver.get(red_ready_link)
        time.sleep(5)                       # время паузы зависит от скорости интернета, RAM и CPU
        photos = driver.find_element('xpath', '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/img')
        photo = photos.get_attribute('src')
        file_name = photos.get_attribute('alt')
        img_data = requests.get(photo).content
        with open(f'data_persons/photo/{file_name}.jpg', 'wb') as handler:
            handler.write(img_data)
        driver.close()
        driver.start_session({})
    logging.info('--- The work of the program is completed! ---')