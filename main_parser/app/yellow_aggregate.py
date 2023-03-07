import time
import logging

from main_parser.app.links_persons import list_persons


def yellow_aggregate_info(
    driver,
    links_cache,
    data_cache
):
    logging.info('--- Parsing of person page data. ---')
    for yellow_ready_link in list_persons(links_cache):
        yellow_person_dict = {
            'Second name': None,
            'First name': None,
            'Gender': None,
            'Date of birth': None,
            'Nationality': None,
            'Place of disappearance': None,
            'Date of disappearance': None
        }
        driver.get(yellow_ready_link)
        time.sleep(5)                       # время паузы зависит от скорости интернета, RAM и CPU
        name_information = driver.find_elements('id', 'name')
        for name in name_information:
            yellow_person_dict['Second name'] = name.text
        forename_inforamation = driver.find_elements('id', 'forename')
        for forename in forename_inforamation:
            yellow_person_dict['First name'] = forename.text
        gender_inforamation = driver.find_elements('id', 'sex_id')
        for gender in gender_inforamation:
            yellow_person_dict['Gender'] = gender.text
        birth_inforamation = driver.find_elements('id', 'date_of_birth')
        for birth in birth_inforamation:
            yellow_person_dict['Date of birth'] = birth.text
        nationalities_inforamation = driver.find_elements('id', 'nationalities')
        for nationalities in nationalities_inforamation:
            yellow_person_dict['Nationality'] = nationalities.text
        place_disappearance_information = driver.find_elements('id', 'place')
        for place_disappearance in place_disappearance_information:
            yellow_person_dict['Place of disappearance'] = place_disappearance.text
        date_disappearance_information = driver.find_elements('id', 'date_of_event')
        for date_disappearance in date_disappearance_information:
            yellow_person_dict['Date of disappearance'] = date_disappearance.text
        data_cache.lpush('persons_dict', str(yellow_person_dict))
        driver.close()
        driver.start_session({})
    logging.info('--- Ready! Data has been generated. ---')
