'''
Метод реализует поиск ссылок на страницы персон интерпола
красного и жёлтого списоков. На вход метод принимает ссылку
и класс драйвера (Chrome или Firefox):
    url str: ссылка на страницу для парсинга данных
    driver : класс драйвера (webdriver.Chrome() или webdriver.Firefox())
После выполнения, метод возвращает список ссылок на персон.
    ready_link_list list: возвращаемый список ссылок.
'''


import time
import logging

from selenium.webdriver.common.keys import Keys


def search_link_persons(
    url: str,
    driver,
    links_cache
):
    driver.get(url)
    time.sleep(2)
    try:
        logging.info('--- Started downloading profile links. ---')
        while True:
            for link_profile in driver.find_elements('class name', 'redNoticeItem__labelLink'):
                red_links_list = link_profile.get_attribute('href')
                links_cache.lpush('links_list', red_links_list)
            driver.find_element('tag name', 'body').send_keys(Keys.END)
            driver.find_element('css selector', '.nextIndex').click()
            time.sleep(3)

    except:
        logging.info('--- Link loading completed. --- The data is recorded in Redis. ---')
        logging.info(f'--- {len(links_cache.lrange("links_list", 0, -1))} links were recorded. ---')
        driver.close()
        driver.start_session({})
