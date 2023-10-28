#Gmail validation

email = input('Enter your Email : ')#g@g.in
k,j,d=0,0,0
if len(email)>=6:#condition 1
    if email[0].isalpha():#condition2
        if ("@" in email) and (email.count("@")==1):#condition 3
            if (email[-4] == ".") ^ (email[-3] == "."):#condition 4
                for i in email:
                    if i == i.isspace():#conditin 5
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i == '_' or i == '.' or i == '@':
                        continue
                    else:
                        d=1
                if k == 1 or j == 1 or d == 1:
                    print('Invalid Email 5')
                else:
                    print('Rigt Email')
            else:
                print('Invalid Email 4')
        else:
            print('Invalid Email 3')
    else:
        print('Invalid Email 2')
else:
    print('Invalid Email 1')
