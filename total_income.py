def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_input = int(input("How many months? "))

    for month_input in range(1, months_input + 1):
        income = float(input("Enter income for month {} : ".format(month_input)))
        incomes.append(income)
    # float(input("Enter income for month " + str(month_input) + ": "))
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months_input + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()