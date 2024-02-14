"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Riley Pollard
Lab Time: Thursday 2pm lab, wednesday class
"""

def password_mod():
    word = input()
    password = ''
    # Type your code here.
    for i in word:
        if i == 'i':
            password+='1'
        elif i == 'a':
            password+='@'
        elif i == 'm':
            password+='M'
        elif i == 'B':
            password+='8'
        elif i == 's':
            password+='$'
        else:
            password += i
        
    password += '!'
    print(password)

if __name__ == "__main__":
    password_mod()