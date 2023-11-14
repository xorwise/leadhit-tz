# Техническое задание для вакансии на hh.ru

## Описание решения
Основной алгоритм заключается в том, что я беру все шаблоны из БД, которые имеют хотя бы один ключ, совпадающий во входной форме, и уже среди них перебираю все ключи и значения, валидируя их через регулярные выражения.
Можно было просто перебрать все шаблоны и сравнить, но при большом количестве шаблонов, мой алгоритм даст значительное преймущество в производительности.

Сделал это через POST запрос и Query параметры, хотя понимаю, что обычно так не принято делать и следует использовать Body. Однако в ТЗ формат данных уж сильно походил на Query.

## Getting started
- Установите версию Python 3.10 и выше.
- Склонируйте репозиторий
- Создайте вирутуальное окружение `python3 -m venv venv`
- Подключитесь к виртуальному окружению `source venv/bin/activate`
- Установите необходимые пакеты `pip install -r requirements.txt`
- Запустите веб-сервер `python3 main.py`
- Протестируйте задание с помощью **test.sh** `./test.sh`

**Надеюсь, такое решение вас устроит!**
**С уважением,**
**Ситников Михаил**
