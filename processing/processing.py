def filter_by_state(transaction_list, state='EXECUTED'):
    """Фильтрует транзакции по состоянию."""
    return [transaction for transaction in transaction_list if transaction['state'] == state]


def sort_by_date(transaction_list, descending=True):
    """Сортирует транзакции по дате."""
    return sorted(transaction_list, key=lambda x: x['date'], reverse=descending)


# Пример использования функций:
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по состоянию 'EXECUTED'
executed_transactions = filter_by_state(transactions)
print(executed_transactions)

# Фильтрация по состоянию 'CANCELED'
canceled_transactions = filter_by_state(transactions, 'CANCELED')
print(canceled_transactions)

# Сортировка по дате по убыванию
sorted_transactions_desc = sort_by_date(transactions)
print(sorted_transactions_desc)

# Сортировка по дате по возрастанию
sorted_transactions_asc = sort_by_date(transactions, False)
print(sorted_transactions_asc)
