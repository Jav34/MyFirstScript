names = []
surnames = []
emails = []


def reg():
    name = input("Name: ")
    surname = input("Surname: ")
    email = input("Enter your email: ")
    input("Password: ")
    names.append(name)
    surnames.append(surname)
    emails.append(email)


def reg_done():
    print("Wonderful! Your data have been added successfully!")
    print(names, surnames, emails)


def in_login_one():
    print("Excellent! Welcome")


def in_login_two():
    print("I'm sorry, but something went wrong. Please try again!")
    print(log_in())


def log_in():
    print("Enter your email: ")
    email = input()
    print("Enter your password: ")
    input()
    if email in emails:
        return in_login_one()
    if email not in emails:
        return in_login_two()


print("HELLO AND WELCOME!")
print("******************")
print("Are you ready to start?")
y = 'Yes'
n = "No"
print("insert 'Yes' of 'No':")
start = input()
if start == y:
    print(reg())
    print(reg_done())
    print(log_in())
    exit()
if start == n:
    print("Thank you for visiting my page. Have a great life :) Bye!")
else:
    print("How should I interpret that?")
    bla_bla = input()
    print("Let's say that", bla_bla, "is not enough for me and let's try again from the beginning")
    print("Are you ready to start?")
y = 'Yes'
n = "No"
print("insert 'Yes' of 'No':")
start = input()
if start == y:
    print(reg())
    print(reg_done())
if start == n:
    exit("Thank you for visiting my page. Have a great life :) Bye!")
else:
    exit("I'm afraid I can't help you. So long, my dear... ")

