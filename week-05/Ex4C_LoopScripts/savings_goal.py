bank_balance = int(input("How much is in your Balance? "))
savings_goal = int(input("Savings goal: "))
weekly_savings = int(input("Weekly savings amount: "))

while bank_balance < savings_goal:
    bank_balance += weekly_savings
    if bank_balance >= savings_goal * 0.75:
        bank_balance -= 10
        print(f"So close! After treating myself, my balance is up to {bank_balance}")

    elif bank_balance > savings_goal / 2:
        print(f"Almost there! This week my balance is up to {bank_balance}")

    else:
        print(f"This week my balance increased to {bank_balance}")

print(f"Goal met! My current balance is {bank_balance}")