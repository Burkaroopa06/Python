def calculate_bill(units):

    if units <= 50:
        bill_amount = units * 0.50
    elif units <= 150:
        bill_amount = 50 * 0.50 + (units - 50) * 0.75
    elif units <= 250:
        bill_amount = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
    else:
        bill_amount = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50
    return bill_amount


def main():

    units_consumed = int(input("Enter the number of units consumed: "))
    total_bill = calculate_bill(units_consumed)
    print(f"The total electricity bill is: ${total_bill:.2f}")


if __name__ == "__main__":
    main()
