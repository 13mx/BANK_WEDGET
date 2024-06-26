def filter_by_currency(transaction_list, currency_code):
    for transaction in transaction_list:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction

def transaction_descriptions(transaction_list):
    for transaction in transaction_list:
        yield transaction['description']

def card_number_generator(start, end):
    for number in range(start, end + 1):
        yield f"{number:0>16}".replace("0", "X")

# Пример использования:
global_transactions = [
    {
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
    },
    # ... остальные словари ...
]

usd_transactions = filter_by_currency(global_transactions, "USD")
for _ in range(2):
    print(next(usd_transactions)["id"])

descriptions = transaction_descriptions(global_transactions)
for _ in range(5):
    print(next(descriptions))

for card_number in card_number_generator(1, 5):
    print(card_number)
