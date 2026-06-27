# Quiz & Examination System

questions = [
    ("Who developed Python?", "A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Bjarne Stroustrup", "C"),

    ("Which data type is immutable in Python?", "A. List", "B. Dictionary", "C. Set", "D. Tuple", "D"),

    ("Which symbol is used to define a comment in Python?", "A. //", "B. #", "C. /*", "D. --", "B"),

    ("Which function is used to display output in Python?", "A. print()", "B. input()", "C. show()", "D. output()", "A"),

    ("Which loop is used when the number of iterations is known?", "A. while", "B. do-while", "C. for", "D. None", "C"),

    ("What is the correct file extension for Python files?", "A. .java", "B. .py", "C. .html", "D. .cpp", "B"),

    ("Which keyword is used to define a function in Python?", "A. function", "B. define", "C. def", "D. fun", "C"),

    ("Which data structure stores data as key-value pairs?", "A. List", "B. Tuple", "C. Set", "D. Dictionary", "D"),

    ("Which function is used to get user input?", "A. print()", "B. input()", "C. len()", "D. type()", "B"),

    ("What is the output type of input() function?", "A. int", "B. float", "C. str", "D. bool", "C")
]

# Grade Function
def calculate_grade(percent):

    if percent >= 90:
        return "O"

    elif percent >= 80:
        return "A+"

    elif percent >= 70:
        return "A"

    elif percent >= 60:
        return "B+"

    elif percent >= 50:
        return "B"

    else:
        return "F"


# Quiz Function
def start_quiz():

    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    score = 0
    wrong_answers = []

    for q in questions:

        print("\n" + q[0])
        print(q[1])
        print(q[2])
        print(q[3])
        print(q[4])

        answer = input("Your Answer (A/B/C/D): ").upper()

        if answer == q[5]:
            print("Correct!")
            score += 1

        else:
            print("Wrong!")
            wrong_answers.append((q[0], q[5]))

    total_questions = len(questions)

    percent = (score / total_questions) * 100

    grade = calculate_grade(percent)

    print("\n===== RESULT REPORT =====")
    print("Name :", name)
    print("Roll :", roll)
    print("Score :", score, "/", total_questions)
    print("Percentage :", round(percent, 2))
    print("Grade :", grade)

    if percent >= 50:
        print("Result : PASS")
    else:
        print("Result : FAIL")

    if len(wrong_answers) > 0:

        print("\n===== WRONG ANSWERS =====")

        for item in wrong_answers:
            print("Question :", item[0])
            print("Correct Answer :", item[1])
            print()


# Start Quiz
start_quiz()