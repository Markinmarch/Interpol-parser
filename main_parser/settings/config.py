'''
Файл содержит основные данные для стабильной работы приложения.
'''


import os

from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv('REDIS_HOST', '')

REDIS_PORT = os.getenv('REDIS_PORT', '')

REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')

URL_PARSER = 'https://www.interpol.int/How-we-work/Notices/View-Red-Notices'
