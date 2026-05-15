# display_mailing_label(). format and display the data as you would on an address label
def display_mailing_label(name, address, city, state, zip):
    return f'''{name}\n{address}\n{city}, {state} {zip}'''
print(display_mailing_label('Kevin', '123 sesame st', 'San Jose', 'CA', '12345'))

# add_numbers(). add given arguments together and display the results using the following format:
# number[+number2+number3+..] = results
def add_numbers(*args):
    result = sum(args)
    equation = " + ".join([str(n) for n in args])
    return f"{equation} = {result}"
print(add_numbers(1, 2, 3))

# display_receipt(). Compute and display the change due
def display_receipt(total_due, amount_paid):
    print(f"Total due:${total_due}")
    print(f"Amount paid:${amount_paid}")

    if amount_paid < total_due:
        balance = total_due - amount_paid
        return f"Remaing balance to be paid: ${balance}"
    else:
        change = amount_paid - total_due
        return f"Change due: ${change}"

# Test:
print(display_receipt(50, 60)) # They paid more than the total
print(display_receipt(75, 60)) # They still have an unpaid balance
print(display_receipt(50, 50)) # paid exact amount


