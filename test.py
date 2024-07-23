from datetime import datetime, timedelta

# Сумма займа
loan_amount = 30000

# Дата выдачи займа
loan_date = "20.07.2024"

# Текущая дата
current_date = "25.08.2024"

# Транзакции за день
transaction = [[datetime.strptime("22.07.2024", "%d.%m.%Y"), 1, 1000],
               [datetime.strptime("22.07.2024", "%d.%m.%Y"), 2, 3000],
               [datetime.strptime("23.07.2024", "%d.%m.%Y"), 1, 500],
               [datetime.strptime("23.08.2024", "%d.%m.%Y"), 1, 4000]]

# Преобразование строковых дат в объекты datetime
loan_date = datetime.strptime(loan_date, "%d.%m.%Y")
current_date = datetime.strptime(current_date, "%d.%m.%Y")

# Переменная пеня
penya = 0.001

# Текущий остаток займа
current_loan_balance = loan_amount

# Количество дней от даты выдачи займа до текущей
numb_day = (current_date - loan_date).days

# Основной цикл для расчета текущего остатка займа
for day in range(1, numb_day + 1):
    current_day = loan_date + timedelta(days=day)
    total = 0

    # Проверка наличия транзакций на текущий день
    for item in transaction:
        if item[0] == current_day:
            total += item[-1]
            print(
                f"Дата транзакции: {current_day.strftime('%d.%m.%Y')}, Сумма транзакции: {item[-1]}, Текущая сумма займа к погашению: {round(current_loan_balance, 2)}")

    # Начисление пени или учет транзакций в зависимости от периода
    if day <= 30:
        current_loan_balance = loan_amount - total
        if current_loan_balance <= 0:
            print("Поздравляем, вы погасили займ вовремя")
            break
    elif 30 < day <= 100:
        if total > 0:
            current_loan_balance -= total
            print(
                f"Дата транзакции: {current_day.strftime('%d.%m.%Y')}, Сумма транзакции: {item[-1]}, Текущая сумма займа к погашению: {round(current_loan_balance, 2)}")
        else:
            current_loan_balance += current_loan_balance * penya
        if current_loan_balance > 0:
            print(f"У вас просрочка. Текущая сумма займа к погашению: {round(current_loan_balance, 2)}")
    elif day > 100:
        print("Ваш займ передан коллекторам!!!")
        break

    # Округление до сотых
    current_loan_balance = round(current_loan_balance, 2)

    # Убежда
