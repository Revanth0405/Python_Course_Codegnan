# Quiz app

def main():
    print("Welcome to the Quiz App!")
    print("Please answer the following questions:")
    python_questions = [
    {
        "question": "What is the output of `print(type([]))` in Python?",
        "options": {
            "A": "list",
            "B": "tuple",
            "C": "array",
            "D": "dict"
        },
        "correct_answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "def",
            "B": "function",
            "C": "define",
            "D": "func"
        },
        "correct_answer": "A"
    },
    {
        "question": "What does the `len()` function do?",
        "options": {
            "A": "Returns the length of an object",
            "B": "Converts a value to integer",
            "C": "Prints the object to console",
            "D": "Creates a new list"
        },
        "correct_answer": "A"
    },
    {
        "question": "Which of these is NOT a valid Python data type?",
        "options": {
            "A": "float",
            "B": "double",
            "C": "str",
            "D": "bool"
        },
        "correct_answer": "B"
    },
    {
        "question": "How do you start a single-line comment in Python?",
        "options": {
            "A": "//",
            "B": "#",
            "C": "--",
            "D": "/*"
        },
        "correct_answer": "B"
    },
    {
        "question": "What is the result of `3 * 'abc'` in Python?",
        "options": {
            "A": "'abcabcabc'",
            "B": "9",
            "C": "TypeError",
            "D": "'abc3'"
        },
        "correct_answer": "A"
    },
    {
        "question": "Which method is used to add an item to the end of a list?",
        "options": {
            "A": "append()",
            "B": "insert()",
            "C": "add()",
            "D": "push()"
        },
        "correct_answer": "A"
    },
    {
        "question": "What does the `range(5)` function return?",
        "options": {
            "A": "[0, 1, 2, 3, 4]",
            "B": "[1, 2, 3, 4, 5]",
            "C": "A range object from 0 to 4",
            "D": "A list from 0 to 5"
        },
        "correct_answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": {
            "A": "^",
            "B": "**",
            "C": "^^",
            "D": "*^"
        },
        "correct_answer": "B"
    },
    {
        "question": "What is the correct way to create a dictionary?",
        "options": {
            "A": "{'key': 'value'}",
            "B": "dict('key' = 'value')",
            "C": "{key = value}",
            "D": "Dictionary(key: value)"
        },
        "correct_answer": "A"
    },
    {
        "question": "Which module is used for working with dates in Python?",
        "options": {
            "A": "datetime",
            "B": "time",
            "C": "date",
            "D": "calendar"
        },
        "correct_answer": "A"
    },
    {
        "question": "What does the `strip()` method do?",
        "options": {
            "A": "Removes leading and trailing whitespace",
            "B": "Splits a string into a list",
            "C": "Converts string to uppercase",
            "D": "Replaces all spaces with underscores"
        },
        "correct_answer": "A"
    },
    {
        "question": "How do you catch exceptions in Python?",
        "options": {
            "A": "try-except",
            "B": "catch",
            "C": "exception",
            "D": "handle"
        },
        "correct_answer": "A"
    },
    {
        "question": "What is the output of `bool('False')`?",
        "options": {
            "A": "False",
            "B": "True",
            "C": "Error",
            "D": "None"
        },
        "correct_answer": "B"
    },
    {
        "question": "Which of these is immutable in Python?",
        "options": {
            "A": "List",
            "B": "Dictionary",
            "C": "Tuple",
            "D": "Set"
        },
        "correct_answer": "C"
    },
    {
        "question": "What does the `__init__` method do?",
        "options": {
            "A": "Initializes a class instance",
            "B": "Terminates a program",
            "C": "Imports a module",
            "D": "Creates a new file"
        },
        "correct_answer": "A"
    },
    {
        "question": "Which symbol is used for string formatting in f-strings?",
        "options": {
            "A": "%",
            "B": "{}",
            "C": "{{}}",
            "D": "$"
        },
        "correct_answer": "B"
    },
    {
        "question": "What is the result of `[x for x in range(3)]`?",
        "options": {
            "A": "[0, 1, 2]",
            "B": "[1, 2, 3]",
            "C": "(0, 1, 2)",
            "D": "{0, 1, 2}"
        },
        "correct_answer": "A"
    },
    {
        "question": "Which function is used to read input from the user?",
        "options": {
            "A": "input()",
            "B": "get()",
            "C": "read()",
            "D": "scan()"
        },
        "correct_answer": "A"
    },
    {
        "question": "What does the `pass` statement do?",
        "options": {
            "A": "Terminates the program",
            "B": "Does nothing (a null operation)",
            "C": "Skips the current iteration",
            "D": "Passes arguments to a function"
        },
        "correct_answer": "B"
    }
    ]
    score = 0
    for i in range(len(python_questions)):
        print(f"Question {i+1}: {python_questions[i]['question']}")
        print("Options:")
        for option, answer in python_questions[i]['options'].items():
            print(f"{option}: {answer}")
        ans = input("Enter the option (A, B, C, D): ").strip().upper()
        if ans == python_questions[i]['correct_answer']:
            print("Correct!!")
            score += 1
        else:
            print("Incorrect answer!!","The correct answer is", python_questions[i]['correct_answer'])

    print(f"Your total score is: {score}/{len(python_questions)}")
    print("Thank you for participating in the Quiz App!")

if __name__ == "__main__":
    main()