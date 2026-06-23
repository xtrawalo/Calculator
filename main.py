Numbers = []
Operators = []
solution = 0

type = int(input('Choose one calculator (1, 2) : '))
start = 0

while start < 1:

    if type == 1:

        try:
            Numbers.append(float(input('Enter a number : ')))
        except ValueError:
            print('Invalid Number, Try again')
            Numbers.append(float(input('Enter a number : ')))

        i=0
        while i < 6:

            Operators.append(input('Enter an operator (+, -, *, /) : '))
            if Operators[i] == "*" or Operators[i] == "/" or Operators[i] == "+" or Operators[i] == "-":
                pass
            else:
                print("Invalid Operator, Try again")
                Operators.remove(Operators[i])
                Operators.append(input('Enter an operator (+, -, *, /) : '))

            try:
                Numbers.append(float(input('Enter a number : ')))
            except ValueError:
                print('Invalid Number, Try again')
                Numbers.append(float(input('Enter a number : ')))


            if i == 0:
                if Operators[0] == "*" or Operators[0] == "/":
                    if Operators[0] == "*":
                        solution = Numbers[0] * Numbers[1]
                    else:
                        solution = Numbers[0] / Numbers [1]
                if Operators[0] == "+" or Operators[0] == "-":
                    if Operators[0] == "+":
                        solution = Numbers[0] + Numbers[1]
                    else:
                        solution = Numbers[0] - Numbers[1]
            else:
                if Operators[i] == "*" or Operators[i] == "/":
                    if Operators[i] == "*":
                        solution = solution * Numbers[i+1]
                    else:
                        solution = solution / Numbers [i+1]
                if Operators[i] == "+" or Operators[i] == "-":
                    if Operators[i] == "+":
                        solution = solution + Numbers[i+1]
                    else:
                        solution = solution - Numbers[i+1]
            print (solution)

            if i == 6:
                choice = input('Restart (Y/N) : ')
                if choice == "Y" or choice == "y":
                    start = 0
                    break
                elif choice == "N" or choice == "n":
                    start = 1
                    break
                else:
                    print("Invalid Answer, Try again")
                    choice = input('Continue (Y/N)')
            else:
                choice = input('Continue (Y/N) : ')
                if choice == "Y" or choice == "y":
                    i += 1
                    continue
                elif choice == "N" or choice == "n":
                    choice = input('Restart (Y/N) : ')
                    if choice == "Y" or choice == "y":
                        start = 0
                        Numbers.clear()
                        Operators.clear()
                        solution = 0
                        break
                    elif choice == "N" or choice == "n":
                        start = 1
                        break
                    else:
                        print("Invalid Answer, Try again")
                        choice = input('Continue (Y/N)')
                else:
                    print("Invalid Answer, Try again")
                    choice = input('Continue (Y/N)')

    elif type == 2:
        
        try:
            Numbers.append(float(input('Enter a number : ')))
        except ValueError:
            print('Invalid Number, Try again')
            Numbers.append(float(input('Enter a number : ')))

        i=0
        while i < 6:
            Operators.append(input('Enter an operator (+, -, *, /) : '))
            if Operators[i] == "*" or Operators[i] == "/" or Operators[i] == "+" or Operators[i] == "-":
                pass
            else:
                print("Invalid Operator, Try again")
                Operators.remove(Operators[i])
                Operators.append(input('Enter an operator (+, -, *, /) : '))

            try:
                Numbers.append(float(input('Enter a number : ')))
            except ValueError:
                print("Invalid Number, Try again")
                Numbers.append(float(input('Enter a number : ')))
            
            answer = input('Continue (Y/N) : ')
            if answer == "Y" or answer == "y":
                i += 1
            elif answer == "N" or answer == "n":
                i = 6
                a = 0
                while a < len(Operators):
                    if Operators[a] == "-":
                        Numbers[a+1] =  -Numbers[a+1]
                        Operators[a] = "+"
                    elif Operators[a] == "/":
                        Numbers[a+1] = 1 / Numbers[a+1]
                        Operators[a] = "*"
                    else:
                        pass
                    a += 1
                
                
                temp = []
                a=0
                while a < len(Operators):
                    if Operators[a] == "*":
                        if a == 0:
                            temp = [Numbers[0]]
                        else:
                            pass    
                        temp[-1] = temp[-1] * Numbers[a+1]
                    else:
                        if (
                            (a > 0 and Operators[a-1] == "*")
                            or
                            (a < len(Operators)-1 and Operators[a+1] == "*")
                        ):
                            temp.append(Numbers[a+1])
                            if a == 0:
                                solution = Numbers[a] 
                            else:
                                pass
                        else:
                            if a == 0:
                                solution = Numbers[a] + Numbers[a+1]
                            else:
                                solution = solution + Numbers[a+1]
                    a += 1

                a=0
                while a < len(temp):
                    solution = solution + temp[a]
                    a += 1
                
                print(solution)
                
                choice = input('Restart (Y/N) : ')
                if choice == "Y" or choice == "y":
                    start = 0
                    break
                elif choice == "N" or choice == "n":
                    start = 1
                    break
                else:
                    print("Invalid Answer, Try again")
                    choice = input('Continue (Y/N)')
        
            else:
                print("Invalid Answer, Try again")
                answer = input('Continue (Y/N)')

    else:
        print("Invalid Number")
        answer = int(input('Choose one calculator (1, 2) : '))