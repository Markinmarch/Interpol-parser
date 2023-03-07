import json
import ast
import logging


def record_json(
    data_cache
):  
    logging.info('--- Data formation on JSON  ---')
    big_data_list = []
    data_b = data_cache.lrange('persons_dict', 0, -1)
    for data in data_b:
        ready_data = data.decode('utf-8')
        data_to_record = ast.literal_eval(ready_data)
        big_data_list.append(data_to_record)
    with open('data_persons/result.json', 'w', encoding = 'utf-8') as file:
        json.dump(big_data_list, file, indent = 4)
    