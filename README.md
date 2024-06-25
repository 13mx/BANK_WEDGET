# Проект Управления Банковскими Транзакциями

## Описание

Этот проект предоставляет инструменты для фильтрации и сортировки банковских транзакций. Функции `filter_by_state` и `sort_by_date` позволяют пользователям организовывать транзакции по состоянию и дате соответственно.

## Функции

- `filter_by_state(transaction_list, state='EXECUTED')`: Фильтрует транзакции по заданному состоянию.
- `sort_by_date(transaction_list, descending=True)`: Сортирует транзакции по дате.

## Использование

```python
# Фильтрация по состоянию 'EXECUTED'
executed_transactions = filter_by_state(transactions)

# Фильтрация по состоянию 'CANCELED'
canceled_transactions = filter_by_state(transactions, 'CANCELED')

# Сортировка по дате по убыванию
sorted_transactions_desc = sort_by_date(transactions)

# Сортировка по дате по возрастанию
sorted_transactions_asc = sort_by_date(transactions, False)
