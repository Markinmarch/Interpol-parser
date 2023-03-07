'''
Метод реализует запрос данных по ссылкам из красного
списка с последующим формированием словарей и записью
в список БД Redis. На вход принимает драйвер, классы
подключения к БД.
    driver : класс драйвера (webdriver.Chrome() или webdriver.Firefox())
    links_cache : класс подключения к БД Redis "links_list"
    data_cache : класс подключения к БД Redis "persons_dict"
'''


import time
import logging

from main_parser.app.links_persons import list_persons


def red_aggregate_info(
    driver,
    links_cache, 
    data_cache,
):
    logging.info('--- Parsing of person page data. ---')
    for red_ready_link in list_persons(links_cache): 
        red_person_dict = {
            'Wanted by': None,
            'Second name': None,
            'First name': None,
            'Gender': None,
            'Date of birth': None,
            'Nationality': None,
            'Crimes': None
        }
        driver.get(red_ready_link)
        time.sleep(5)                       # время паузы зависит от скорости интернета, RAM и CPU
        wanted_information = driver.find_element('xpath', '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/p/strong')
        red_person_dict['Wanted by'] = wanted_information.text
        name_information = driver.find_elements('id', 'name')
        for name in name_information:
            red_person_dict['Second name'] = name.text
        forename_inforamation = driver.find_elements('id', 'forename')
        for forename in forename_inforamation:
            red_person_dict['First name'] = forename.text
        gender_inforamation = driver.find_elements('id', 'sex_id')
        for gender in gender_inforamation:
            red_person_dict['Gender'] = gender.text
        birth_inforamation = driver.find_elements('id', 'date_of_birth')
        for birth in birth_inforamation:
            red_person_dict['Date of birth'] = birth.text
        nationalities_inforamation = driver.find_elements('id', 'nationalities')
        for nationalities in nationalities_inforamation:
            red_person_dict['Nationality'] = nationalities.text
        charge_inforamation = driver.find_elements('id', 'charge')
        for charge in charge_inforamation:
            red_person_dict['Crimes'] = charge.text
        data_cache.lpush('persons_dict', str(red_person_dict))
        driver.close()
        driver.start_session({})
    logging.info('--- Ready! Data has been generated. ---')
    