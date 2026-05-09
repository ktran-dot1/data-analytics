# What is enumerate()?

grocery_list = ['peach', 'apple', 'chocolate chip cookies', 'rotisserie chicken', 'pita']

for i, thing in enumerate(grocery_list, start=1):
    # print(i, thing)
    if i > 3:
        break
    print(f'Item number {i} in the list is {thing}')
    