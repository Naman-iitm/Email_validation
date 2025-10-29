email = input("Enter your email:") #g@g.in., naman@gmail.com
# sabse minimum charcter kya kya ho skat ahai g@g.in matlab min 6 letter

k = 0
j = 0
d = 0

if len(email)>=6:
    if email[0].isalpha(): # isalpha function yeh dekhta hai ki pehle letter character hona chhaiye
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."): # agar dono true == result false # agar dono false == result false sirf ek hi ho skata hai 
                

                for i in email :

                    if i == i.isspace():
                        k = 1

                    elif i.isalpha():
                        if i == i.upper(): # mail mein uppercase ho then 
                            j = 1

                    elif i.isdigit():
                        continue
                    
                    elif i =="_" or i =="." or i == "@":
                        continue

                    else:
                        d = 1 #yadi koi aur sign ka istemaal hua ho jaise #!%&*

                if k == 1 or j == 1 or d == 1:
                    print("Oops! You have entered some space or some uppercase or any special character in your email")

                else:
                    print("Email format is right buddy !!! ")


            else:
                print("Opps! you have entered wrong domain")

        else:
            print("Oops! you have entered @ more than one time :-)")

    else:
        print("Oops! you have entered wrong email ")

else:
    print(" Oops! you have entered wrong email ")




