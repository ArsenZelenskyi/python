
def get_number(text, decimal=False):
    while True:
        try:
            if decimal:
                number = float(input(text))
            else:
                number = int(input(text))

            if number <= 0:
                print("Число має бути більше 0!")
            else:
                return number

        except ValueError:
            print("Введіть число!")


def input_data():
    money = get_number("Enter the amount deposited: ")
    rate = get_number("Enter the annual interest rate (0.12 for 12%): ", True)
    months = 24

    return money, rate, months


def monthly_profit(money, rate):
    return money * rate / 12


def total_money(money, profit, months):
    return money + profit * months


def main():
    money, rate, months = input_data()

    profit = monthly_profit(money, rate)
    total = total_money(money, profit, months)

    current_money = money

    for month in range(1, months + 1):
        current_money += profit
        print(f"Month: {month:2d}, Profit: {profit:.2f}, Total amount: {current_money:.2f}")

    print(f"Total amount after {months} months: {total:.3f}")


if __name__ == '__main__':
    main()
