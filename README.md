# Тестовое задание. Марк Изотов

## ТЕХНИЧЕСКОЕ ЗАДАНИЕ

1. С сайта интерпола собрать данные всех профилей [жёлтого](https://www.interpol.int/How-we-work/Notices/View-Yellow-Notices.md) и [красного](https://www.interpol.int/How-we-work/Notices/View-Red-Notices.md) списков вместе с фотографиями профилей. Записать данные в JSON.

## КРАТКАЯ ИНФОРМАЦИЯ

1. Запуск через консоль ```python -m main_parser```

2. Реализация на микроархитектуре, применён паттерн Visitor.

3. Использовал нереляционную БД Redis. Перед началом работы проверить выделенное место в памяти.
Ввиду динамического сайта интерпола, для парсинга данных использовал фреймворк Selenium. Загрузку данных и фотографий реализовал раздельно в целях безопасности и стабильности работы приложения.

4. Данные REDIS_HOST и REDIS_PORT помещены в .env.

5. Проверить начилие хорошего интернета и стабильность работы компьютера. Задержка выставлена 5 сек после запроса с сайта.

6. Ссылка на [репозиторий](https://github.com/Markinmarch/Interpol-parser.md)

7. Протестировано.
