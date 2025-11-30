import random
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):

    password=[]
    chars=""
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower='abcdefghijklmnopqrstuvwxyz'
    digits='0123456789'
    special='!@#&*'
    n=0
   

    if use_upper:
        chars+=upper
        password.append(random.choice(upper))
        n+=1
    if use_digits:
        chars+=digits
        password.append(random.choice(digits))
        n+=1
    if use_special:
       chars+=special
       password.append(random.choice(special))
       n+=1
    if use_lower:
        chars+=lower
        password.append(random.choice(lower))
        n+=1
    if chars=="":
        print("User needs to select atleast one category")
        return None
    elif length<n:
        print(f"There should atleast be {n} charecters")
        return None

    else:
        for i in range(length-n):
            password.append(random.choice(chars))
    random.shuffle(password)
    return "".join(password)
print(generate_password(length=10, use_special=False))
