password = input()
lenpassword = len(password)
num_valid = 0
num_invalid = 0
while password != "q":

    if len(password) < 6 or len(password) > 20:
        print(f"{password}: Invalid length.")
        password = input()
        num_invalid += 1
    else:
        is_missinglower = True
        is_missingupper = True
        is_missingnumeric = True

        for char in password:
            if char.islower() == True:
                is_missinglower = False
            elif char.isupper() == True:
                is_missingupper = False
            elif char.isnumeric() == True:
                is_missingnumeric = False

        if is_missinglower:
            print(f"{password}: Missing lower case letter.")

        if is_missingupper:
            print(f"{password}: Missing upper case letter.")

        if is_missingnumeric:
            print(f"{password}: Missing numeric letter.")
        
        if is_missinglower == True or is_missingupper == True or is_missingnumeric == True:
            num_invalid +=1
        
        else:
            if is_missinglower == True and is_missingupper == True and is_missingnumeric == False:
                print(end = "")
            else:
                print(f"{password}: Valid password of length {len(password)}.")
                num_valid += 1
        password = input()

if password == "q":
    print(f"You tried {num_invalid+num_valid} passwords, {num_valid} valid, {num_invalid} invalid.")
    
    
