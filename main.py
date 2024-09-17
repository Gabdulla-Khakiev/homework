from src.utils import load_transactions, get_transaction_amount_in_rub
from src.external_api import get_exchange_rate
from src.csv_excel import read_transactions_from_csv, read_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions
from src.search_and_categorize import search_operations, categorize_operations
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_type = input()

    if file_type == '1':
        transactions = load_transactions('data/operations.json')
        print("Для обработки выбран JSON-файл.")
    elif file_type == '2':
        transactions = read_transactions_from_csv('data/transactions.csv')
        print("Для обработки выбран CSV-файл.")
    elif file_type == '3':
        transactions = read_transactions_from_excel('data/transactions_excel.xlsx')
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор.")
        return

    while True:
        state = input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ")
        if state.upper() not in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f"Статус операции \"{state}\" недоступен.")
        else:
            break

    filtered_transactions = filter_by_state(transactions, state.upper())
    print(f"Операции отфильтрованы по статусу \"{state.upper()}\"")

    while True:
        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
        if sort_choice == 'да':
            while True:
                sort_order = input("Отсортировать по возрастанию или по убыванию?: ").lower()
                if sort_order == 'по возрастанию':
                    reverse = False
                    filtered_transactions = sort_by_date(filtered_transactions, reverse)
                    break
                elif sort_order == 'по убыванию':
                    filtered_transactions = sort_by_date(filtered_transactions)
                    break
            break
        elif sort_choice == 'нет':
            break

    while True:
        rub_choice = input("Выводить только рублевые тразакции? Да/Нет: ").lower()
        if rub_choice == 'да':
            rub = 'RUB'
            filtered_transactions = filter_by_currency(filtered_transactions, rub)
            break
        elif rub_choice == 'нет':
            break

    while True:
        desc_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
        if desc_choice == 'да':
            word = input("Введите слово для фильтрации: ")
            filtered_transactions = search_operations(filtered_transactions, word)
            break
        elif desc_choice == 'нет':
            break

    counter = 0

    if len(filtered_transactions) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f'Всего банковских операций в выборке: {len(filtered_transactions)}')

        for transaction in filtered_transactions:

            date = get_date(transaction.get('date'))

            description = list(transaction_descriptions(filtered_transactions))

            sender = mask_account_card(transaction.get('from'))
            recipient = mask_account_card(transaction.get('to'))
            amount = transaction.get('operationAmount').get('amount')
            currency_data = transaction.get('operationAmount').get('currency')
            currency_name = currency_data.get('name')
            if sender == 'Ошибка ввода':
                print(f'''{date} {description[counter]}\n{recipient}\nСумма: {amount} {currency_name}''')
            else:
                print(f'''{date} {description[counter]}\n{sender} -> {recipient}\nСумма: {amount} {currency_name}''')
            print(" ")
            counter += 1





if __name__ == "__main__":
    main()
