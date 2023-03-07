from main_parser.app.parser_links import search_link_persons
from main_parser.app.red_aggregate import red_aggregate_info
from main_parser.app.yellow_aggregate import yellow_aggregate_info
from main_parser.app.record_json import record_json
from main_parser.app.get_photo import get_photo

from main_parser.settings.config import URL_PARSER as url
from main_parser.settings.setting import driver
from main_parser.settings.setting import links_cache
from main_parser.settings.setting import data_cache
from main_parser.settings.setting import logger


if not url:
    raise ValueError(
        "URL_PARSER env variables "
        "wasn't implemented in .env (both should be initialized)."
    )

def main():

    search_link_persons(
        url,
        driver,
        links_cache
    )
    
    if 'Red' in url:
        red_aggregate_info(
            driver,
            links_cache,
            data_cache
        )
        
    elif 'Yellow' in url:
        yellow_aggregate_info(
            driver,
            links_cache,
            data_cache
        )

    else:
        raise ValueError(
            "URL_PARSER is not valid"
            "Please, check URL_PARSER and run again"
        )

    record_json(data_cache)

    get_photo(
        driver,
        links_cache
    )

if __name__ == '__main__':
    try:
        main()
        data_cache.flushall()
        driver.close()
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())