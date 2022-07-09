"""
Challenge - Task Two (Day 2)

Write a python program that takes user inputs and determines what career the user should
learn.
Requirements:
● Store career options in a list or in variables.
● Store career advices in a list.
● Store career questions in a list.
● Use conditional statements that determines the user selected choice.
● When a wrong input is entered the program should print out an error message.
● When all the questions are done the program should determine which career the user
should venture in and program should terminate.
"""
# A prototype for a career advice program that will help form 4 leavers in choosing suitable careers
# subject to advancements

# list declaration


career_options = ['Law.', 'Engineering.', 'Technology.', 'Education.', 'Business.', 'Aviation.', 'Health sciences.', 'medicine and Surgery.',
                  'Hospitality management and tourism.', 'music and perfoming arts.', 'Theology.', 'Agriculture.', 'political science.', 'mass communication and journalism.']
career_questions = ['what grades did you score in the following subjects?', 'What subjects do you like from the above subjects? ',
                    'What is your personality(ies) from the list provided below?(Select atmost 3)', 'What are you passionate about from the list provided below?(Select atmost 3)']
career_advices = ['With relation to the information provided,',
                  'you best qualify for', 'It is a very good and marketable career.']

print()
print(' Welcome to the career advice program '.center(50, '-'))
print()


def main():
    # Grades scored by the user
    print(f" {career_questions[0].title()} \nUse grade values between A - E")

    # maths  input validation
    while True:
        maths = input('Maths: ')
        if maths.lower() == 'a' or maths.lower() == 'b' or maths.lower() == 'c' or maths.lower() == 'd' or maths.lower() == 'e':
            break
        else:
            print("Invalid input")
            continue

    # english input validation
    while True:
        english = input('English: ')
        if english.lower() == 'a' or english.lower() == 'b' or english.lower() == 'c' or english.lower() == 'd' or english.lower() == 'e':
            break
        else:
            print("Invalid input")
            continue

    # kiswahili  input validation
    while True:
        kiswahili = input('Kiswahili: ')
        if kiswahili.lower() == 'a' or kiswahili.lower() == 'b' or kiswahili.lower() == 'c' or kiswahili.lower() == 'd' or kiswahili.lower() == 'e':
            break
        else:
            print("Invalid input")
            continue

    # physics  input vaidation
    while True:
        physics = input('physics:')
        if physics.lower() == 'a' or physics.lower() == 'b' or physics.lower() == 'c' or physics.lower() == 'd' or physics.lower() == 'e':
            break
        else:
            print("Invalid input")
            continue

    # chemistry input validation
    while True:
        chemistry = input('Chemistry: ')
        if chemistry.lower() == 'a' or chemistry.lower() == 'b' or chemistry.lower() == 'c' or chemistry.lower() == 'd' or chemistry.lower() == 'e':
            break
        else:
            print("Invalid input")
            continue

    # biology input validation
    while True:
        biology = input('Biology: ')
        if biology.lower() == 'a' or biology.lower() == 'b' or biology.lower() == 'c' or biology.lower() == 'd' or biology.lower() == 'e':
            break
        else:
            print("Invalid input")
            continue

    # mean grade input validation
    while True:
        mean_grade = input('Mean Grade: ')
        if mean_grade.lower() == 'a' or mean_grade.lower() == 'b' or mean_grade.lower() == 'c' or mean_grade.lower() == 'd' or mean_grade.lower() == 'e':
            break
        else:
            print("Invalid input")
            continue

    # User's favourite subject
    print(career_questions[1])

    # favourite_subject1 input validation

    while True:
        favourite_subject1 = input('>')
        if favourite_subject1.lower() == 'maths' or favourite_subject1.lower() == 'english' or favourite_subject1.lower() == 'kiswahili' or favourite_subject1.lower() == 'physics' or favourite_subject1.lower() == 'chemistry' or favourite_subject1.lower() == 'biology':
            break
        else:
            print("Enter atleast one subject")
            continue

    # favourite_subject2 input validation
    while True:
        favourite_subject2 = input('>')
        if favourite_subject2.lower() == 'maths' or favourite_subject2.lower() == 'english' or favourite_subject2.lower() == 'kiswahili' or favourite_subject2.lower() == 'physics' or favourite_subject2.lower() == 'chemistry' or favourite_subject2.lower() == 'biology' or favourite_subject2.lower() == '':
            break
        else:
            print("Invalid input")
            continue

    # favourite_subject3 input validation
    while True:
        favourite_subject3 = input('>')
        if favourite_subject3.lower() == 'maths' or favourite_subject3.lower() == 'english' or favourite_subject3.lower() == 'kiswahili' or favourite_subject3.lower() == 'physics' or favourite_subject3.lower() == 'chemistry' or favourite_subject3.lower() == 'biology' or favourite_subject3.lower() == '':
            break
        else:
            print("Invalid input")
            continue

    # favourite_subject4 input validation
    while True:
        favourite_subject4 = input('>')
        if favourite_subject4.lower() == 'maths' or favourite_subject4.lower() == 'english' or favourite_subject4.lower() == 'kiswahili' or favourite_subject4.lower() == 'physics' or favourite_subject4.lower() == 'chemistry' or favourite_subject4.lower() == 'biology' or favourite_subject4.lower() == '':
            break
        else:
            print("Invalid input")
            continue

    # User's  Personalities
    print(career_questions[2], '''
    (USE THE LETTERS PROVIDED AS INPUTS)
    Introversion(I)
    Extroversion/social(E)
    Judging(J)
    Perceiving(P)
    Sensing(S)
    Intuitive(N)
    Feeling(F)
    Thinking(H)
    ''')

    # Personality1 input validation
    while True:
        personality1 = input('First personality: ')
        if personality1.lower() == 'i' or personality1.lower() == 'e' or personality1.lower() == 'j' or personality1.lower() == 'p' or personality1.lower() == 's' or personality1.lower() == 'n' or personality1.lower() == 'f' or personality1.lower() == 'h':
            break
        else:
            print("Enter atleast one personality")
            continue

    # personality2 input validation
    while True:
        personality2 = input('Second personality: ')
        if personality2.lower() == 'i' or personality2.lower() == 'e' or personality2.lower() == 'j' or personality2.lower() == 'p' or personality2.lower() == 's' or personality2.lower() == 'f' or personality2.lower() == 'f' or personality2.lower() == 'h' or personality2.lower() == '':
            break
        else:
            print("Invalid input")
            continue

    # personality3 input validation
    while True:
        personality3 = input('Third personality: ')
        if personality3.lower() == 'i' or personality3.lower() == 'e' or personality3.lower() == 'j' or personality3.lower() == 'p' or personality3.lower() == 's' or personality3.lower() == 'n' or personality3.lower() == 'f' or personality3.lower() == 'h' or personality3.lower() == '':
            break
        else:
            print("Invalid input")
            continue

    # users interests
    print(career_questions[3], '''
    (USE THE LETTERS PROVIDED AS INPUTS)
    Helping people live healthier lives(H)
    Software computers and Technology(S)
    Solving problems(O)
    Agriculture(A)
    Politics(P)
    Advocating people's rights(R)
    Enterprenuership and Bussiness(E)
    Cooking(C)
    Travelling(T)
    ''')

    # passion1 input validation
    while True:
        passion1 = input('First Interest: ')
        if passion1.lower() == 'h' or passion1.lower() == 's' or passion1.lower() == 'o' or passion1.lower() == 'a' or passion1.lower() == 'p' or passion1.lower() == 'r' or passion1.lower() == 'e' or passion1.lower() == 'c' or passion1.lower() == 't':
            break
        else:
            print("Enter atleast one personality")
            continue

    # passion2 input validation
    while True:
        passion2 = input('Second Interest: ')
        if passion2.lower() == 'h' or passion2.lower() == 's' or passion2.lower() == 'o' or passion2.lower() == 'a' or passion2.lower() == 'p' or passion2.lower() == 'r' or passion2.lower() == 'e' or passion2.lower() == 'c' or passion2.lower() == 't' or passion2.lower() == '':
            break
        else:
            print("Invalid input")
            continue

    # passion3 input validation
    while True:
        passion3 = input('Third Interest: ')
        if passion3.lower() == 'h' or passion3.lower() == 's' or passion3.lower() == 'o' or passion3.lower() == 'a' or passion3.lower() == 'p' or passion3.lower() == 'r' or passion3.lower() == 'e' or passion3.lower() == 'c' or passion3.lower() == 't' or passion3.lower() == '':
            break
        else:
            print("Invalid input")
            continue

    # Determining the best career the user should venture into from the data collected, by using conditional statements.

    if mean_grade.lower() == 'b' or mean_grade.lower() == 'a' and english.lower() == 'b' or english.lower() == 'a' or kiswahili.lower() == 'b' or kiswahili.lower() == 'a' and favourite_subject1.lower() == 'english' or favourite_subject1.lower() == 'kiswahili' or favourite_subject2.lower() == 'english' or favourite_subject2.lower() == 'kiswahili' or favourite_subject3.lower() == 'english' or favourite_subject3.lower() == 'kiswahili' and personality1.lower() != 'i' or personality2.lower() != 'i' or personality3.lower() != 'i' and passion1 != 's' or passion2 != 's' or passion3 != 's' or passion1.lower() == 'r' or passion2.lower() == 'r' or passion3.lower() == 'r':
        print("Advice:")
        print(career_advices[0], career_advices[1],
              career_options[0], career_advices[2])
    else:
        print('Thank you')


if __name__ == '__main__':
    main()
