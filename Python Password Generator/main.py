import random,string,pyperclip

password_lenght = int(input("Enter desired password lenght>").strip() or 8)
password =''

for i in range(password_lenght):
    if password_lenght > len(password):
        password += random.choice(string.ascii_uppercase)
        if password_lenght > len(password):
            password += random.choice(string.digits)
            if password_lenght > len(password):
                password += random.choice(string.punctuation)
                if password_lenght >len(password):
                    password += random.choice(string.ascii_lowercase)
    else: 
        break


print(f"Your password is: {password}")
pyperclip.copy(password)
print('Password successfully copied to clipboard!!!')
