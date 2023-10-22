
expression = "4 * 100 - 54" 
correct_answer = eval(expression)
user_answer = input(f"Solve the expression: {expression} = ")

try:
    user_answer = float(user_answer)
    if user_answer == correct_answer:
        print("Правильно!")
    else:
        print(f"Неправильно {correct_answer}. ")
except ValueError:
    print("Проверьте правильность введеных данных")


    