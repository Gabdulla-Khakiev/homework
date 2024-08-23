# Проект: Серверная часть виджета банковских операций
## описание проекта
программа создана для фильтрации и сортировке банковских счетов и карт по дате и оплате, для маскировки номеров карт и счетов
## инструкция по установке
Для использования функций из этого проекта, необходимо клонировать репозиторий и установить необходимые зависимости (если они есть).

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Gabdulla-Khakiev/homework.git
cd homework
```
2. Установите зависимости (если они есть):
   ```bash
   pip install -r requirements.txt
   ```
## Использование
### 1. Маскирование данных (masks.py)
#### Маскирование номера карты
Функция `get_mask_card_number(card_number: str) -> str` возвращает замаскированный номер карты, где символы с 7 по 12 заменяются на звёздочки (`*`).

Пример использования:
```python
from masks import get_mask_card_number

card_number = "1234567812345678"
masked_card = get_mask_card_number(card_number)
print(masked_card)  # Вывод: 1234 56** **** 5678
```
#### Маскирование номера счета
Функция `get_mask_account(account_number: str) -> str` возвращает замаскированный номер счета, где первые два символа последних шести цифр заменяются на звёздочки (`*`).

Пример использования:
```python
from masks import get_mask_account

account_number = "9876543210"
masked_account = get_mask_account(account_number)
print(masked_account)  # Вывод: **76543210

```
### 2. Обработка данных (processing.py)
#### Фильтрация по состоянию
Функция `filter_by_state(list_of_dict: List[dict], state='EXECUTED') -> List[dict]` возвращает список словарей, отфильтрованных по значению ключа `state`.

Пример использования:
```python
from processing import filter_by_state

data = [{'state': 'EXECUTED', 'date': '2023-01-01'}, {'state': 'PENDING', 'date': '2023-02-01'}]
filtered_data = filter_by_state(data)
print(filtered_data)  # Вывод: [{'state': 'EXECUTED', 'date': '2023-01-01'}]
```
#### Сортировка по дате
Функция `sort_by_date(list_of_dict: List[dict], reverse=True)` сортирует список словарей по значению ключа `date` в порядке убывания (по умолчанию).

Пример использования:
```python
from processing import sort_by_date

data = [{'state': 'EXECUTED', 'date': '2023-01-01'}, {'state': 'PENDING', 'date': '2023-02-01'}]
sorted_data = sort_by_date(data)
print(sorted_data)  # Вывод: [{'state': 'PENDING', 'date': '2023-02-01'}, {'state': 'EXECUTED', 'date': '2023-01-01'}]
```

### 3. Маскирование и форматирование данных (widget.py)
#### Маскирование данных в строке
Функция `mask_account_card(user_information: str) -> str` маскирует номер карты или счета в переданной строке.

Пример использования:
```python
from widget import mask_account_card

info = "Card number 1234567812345678"
masked_info = mask_account_card(info)
print(masked_info)  # Вывод: Card number 1234 56** **** 5678
```
#### Преобразование формата даты
Функция `get_date(date: str) -> str` преобразует дату из формата `YYYY-MM-DD` в формат `DD.MM.YYYY`.

Пример использования:
```python
from widget import get_date

date_str = "2023-08-10"
formatted_date = get_date(date_str)
print(formatted_date)  # Вывод: 10.08.2023
```

## Обработки транзакций и генерация данных (generators.py)

Этот модуль предоставляет функции для работы с транзакциями и генерации банковских карт.

Включает три основные функции:

1.Фильтрация транзакций по валюте:
+ `filter_by_currency(transactions_list, currency)` - Фильтрует список транзакций по заданной валюте и возвращает отфильтрованный список.

2.Генерация описаний транзакций:

+ `transaction_descriptions(transactions)` - Генерирует описания для каждой транзакции из списка. Если список пустой, возвращает "Нет транзакций".

3.Генерация номеров банковских карт:

+ `card_number_generator(start, stop)` - Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в диапазоне от start до stop.

### Примеры использования
#### Фильтрация транзакций
```python
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
#### Генерация описаний транзакций
```python
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
#### Генерация номеров банковских карт
```python
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```

## Декораторы (decorators.py)
### Декоратор `log`
Этот декоратор предназначен для логирования информации о выполнении функций.
Он может записывать логи как в файл, так и выводить их в консоль.
### Основные функции
#### Логирование времени выполнения:

+ Записывает время начала и окончания выполнения функции.
+ Логирует результат выполнения функции.

#### Обработка ошибок:

+ При возникновении исключения записывает информацию об ошибке и входных параметрах функции.

#### Запись в файл или вывод на консоль:

+ Если предоставлен параметр filename, декоратор записывает логи в указанный файл.
+ Если параметр filename не задан, логи выводятся на консоль.

### Пример использования:
```python
from src.generators import log

@log(filename='logfile.txt')
def example_function(x, y):
    return x / y

example_function(10, 2)  # Запишет время выполнения и результат в файл 'logfile.txt'

@log()
def another_function(a, b):
    return a + b

another_function(5, 3)  # Выведет информацию о выполнении функции в консоль

```

## Тестирование
Проект включает в себя набор тестов для проверки функциональности основных функций. Тесты написаны с использованием библиотеки pytest и включают как фикстуры, так и параметризацию.

#### Установка зависимостей для тестирования
Убедитесь, что у вас установлены все зависимости, необходимые для тестирования:
```bash
poetry install
```

#### Запуск тестов
Для запуска всех тестов выполните:
```bash
pytest
```

### Описание тестов
Тесты проверяют на коррекность функции представленные в проекте, включая нестандартные ситуации, по типу отсутвия некоторых данных или пустых входных данных.
