# use if / elif / else to assign letter grades

# score = int(input("What is the raw score? (Enter a number):"))
# grade = None

# if score == 100:    # order of condtions matters! Most restrictive condtion at the top
#     grade = 'A+'
# elif score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     print("Retake required.")

# print(f'Grade is {grade}')


score = int(input("What is the raw score? (Enter a number):"))

extra_credit = int(input("Extra credit points earned:"))

if extra_credit != 0:
    score += extra_credit
    print(f'Updated score: {score}')


grade = None
score_flat = (score // 10) * 10 # rounds down to the nearest 10

match score_flat:
    case 100:
        grade = 'A+'
    case 90:
        grade = 'A'
    case 80:
        grade = 'B'
    case 70:
        grade = 'C'
    case 60:
        grade = 'D'
    case other:
        print("Retake required.")



print(f'Grade is {grade}')
