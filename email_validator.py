# Email Validator 30/11/2022
user = input("Enter your Email: ")
if len(user) >= 6:
    error = 0
    dot = 0
    if user[0].isalpha():
        if ("@" in user) and (user.count("@") == 1):
            if (user[-4] == ".") or (user[-3] == "."):
                j, k, d = 0, 0, 0
                for i in user:
                    if i == i.isspace():
                        k = 1
                    elif i == "_" or i == "." or i == "@":
                        continue
                    elif i.isdigit():
                        continue
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Error 5")
                else:
                    print("Valid Email")
            else:
                print("Error 4")
        else:
            print("Error 3")
    else:
        print("Error 2")
else:
    print("Error 1")
