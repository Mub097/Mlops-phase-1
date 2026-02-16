y = 20

def greet():
    print("hello to functions")

greet()

#functions with parameters

def greet_user(name):
    print(f"hello, {name}!")


greet_user("usman")
greet_user("Abdul Ahad")

#Functions with return values

def add(a,b):
    return a + b

result = (10 +15)
print(result)


#python functions with variable

def my_funct():
    print(y)

my_funct()

def format_accuracy(model_name, accuracy):
    accuracy_percent = accuracy * 100
    return f"Model {model_name} Acheived accuracy{accuracy_percent:.2f}% accuracy"
print(format_accuracy("logistic regression", 0.88776))


def pred_status(probability):

    if probability > 0.5:
        return "Approved"
    else:
        return "Rejected"
print(pred_status(0.7))
print(pred_status(0.3))


def calculate_accuracy(correct, total):
    accuracy = correct/ total * 100
    return(f"accuracy {accuracy:.2f}%")
print(calculate_accuracy(correct=873, total=1000))


