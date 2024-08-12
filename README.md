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
###2. Обработка данных (processing.py)
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
