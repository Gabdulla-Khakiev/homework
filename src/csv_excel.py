import pandas as pd

csv_file_path = "data/transactions.csv"
xlsx_file_path = "data/transactions_excel.xlsx"


def read_transactions_from_csv(csv_file_path):
    """Чтение транзакций из CSV-файла и возврат их в виде списка словарей."""
    try:
        df = pd.read_csv(csv_file_path, delimiter=";")
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_transactions_from_excel(xlsx_file_path):
    """Чтение транзакций из XLSX-файла и возврат их в виде списка словарей."""
    try:
        df = pd.read_excel(xlsx_file_path, engine="openpyxl")
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении XLSX-файла: {e}")
        return []
