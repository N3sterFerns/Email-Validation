

Email = input("Enter Your Email Address: ")

x = 0
y = 0
z = 0

if len(Email)>=6:
    if Email[0].isalpha():
        if ("@" in Email) and (Email.count("@")==1): # @ should be only ones
            if (Email[-4]==".") ^ (Email[-3]=="."):
                for i in Email:
                    if i==i.isspace():
                        x=1
                    elif i.isalpha():
                        if i==i.upper():  #n==N and N==N
                            y=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        z = 1
                if x ==1 or y==1 or z==1:
                    print("Sorry!! Your email is not correct..")
                else:
                    print("Right Email...")
            else:
                print("Invalid Domain")  
        else:
            print("Your email should not contain two @")
    else:
        print("Your email should not contain first digit...")
else:
    print("Your email should not be under six letter...")
