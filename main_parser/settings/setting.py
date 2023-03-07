from redis import StrictRedis
from selenium import webdriver
import logging

from main_parser.settings.config import REDIS_HOST as host
from main_parser.settings.config import REDIS_PORT as port
from main_parser.settings.config import REDIS_PASSWORD as pswd


if not port:
    raise ValueError(
        "REDIS_PORT env variables "
        "wasn't implemented in .env (both should be initialized)."
    )

if not pswd:
    raise ValueError(
        "REDIS_PASSWORD env variables "
        "wasn't implemented in .env (both should be initialized)."
    )   

if not host:
    raise ValueError(
        "REDIS_HOST env variables "
        "wasn't implemented in .env (both should be initialized)."
    )

driver = webdriver.Firefox()

links_cache = StrictRedis(
    host = host,
    port = port,
    password = None,
    db = 0
)

data_cache = StrictRedis(
    host = host,
    port = port,
    password = None,
    db = 1
)

logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

logger = logging.getLogger(__name__)

