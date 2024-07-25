import datetime
from typing import List, Tuple


# Функция для уведомления клиента о платеже
def notify_client(payment_date: datetime.date, amount: float):
    print(f"Payment of {amount:.2f} received on {payment_date}")


# Функция для обработки платежа
def make_payment(transactions: List[Tuple[datetime.date, float]], amount: float, payment_date: datetime.date):
    transactions.append((payment_date, amount))
    notify_client(payment_date, amount)


# Функция для конвертации даты из строки в объект date
def parse_date(date_str: str) -> datetime.date:
    return datetime.datetime.strptime(date_str, "%d.%m.%Y").date()


# Функция для расчета текущего остатка и пеней
def calculate_balance_and_penalties(principal: float, approval_date: datetime.date, current_date: datetime.date,
                                    transactions: List[Tuple[datetime.date, float]]) -> Tuple[
    float, List[Tuple[datetime.date, float]], bool]:
    balance = principal
    penalties = []
    days_passed = (current_date - approval_date).days

    consolidated_transactions = {}
    for date, amount in transactions:
        consolidated_transactions[date] = consolidated_transactions.get(date, 0) + amount

    for day in range(1, days_passed + 1):
        day_date = approval_date + datetime.timedelta(days=day)
        daily_payment = consolidated_transactions.get(day_date, 0)
        balance -= daily_payment

        if day > 30 and balance > 0:
            daily_penalty = balance * 0.001
            balance += daily_penalty
            penalties.append((day_date, daily_penalty))

        if day > 100:
            return balance, penalties, True

    return balance, penalties, False


# Основной процесс
def loan_process(principal: float, approval_date_str: str, current_date_str: str,
                 transactions: List[Tuple[str, float]]):
    approval_date = parse_date(approval_date_str)
    current_date = parse_date(current_date_str)
    parsed_transactions = [(parse_date(date_str), amount) for date_str, amount in transactions]

    balance, penalties, sold_to_collector = calculate_balance_and_penalties(principal, approval_date, current_date,
                                                                            parsed_transactions)

    print(f"Balance on {current_date}: {balance:.2f}")
    print("Penalties accrued:")
    for penalty in penalties:
        print(f"Date: {penalty[0]}, Amount: {penalty[1]:.2f}")

    if sold_to_collector:
        print("Loan sold to collector agency.")
    else:
        if balance <= 0:
            print("Loan fully paid off.")
        else:
            print("Loan not fully paid off.")


# Пример использования
approval_date_str = "01.07.2024"
transactions = [
    ("10.07.2024", 1000),
    ("15.07.2024", 2000),
    ("15.07.2024", 3000)
]

principal = float(input("Введите сумму кредита: "))
current_date_str = input("Введите текущую дату (дд.мм.гггг): ")
loan_process(principal, approval_date_str, current_date_str, transactions)
