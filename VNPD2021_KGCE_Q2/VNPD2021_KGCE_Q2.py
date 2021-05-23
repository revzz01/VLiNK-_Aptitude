#Declare all characters which are valid for the password
#num = "0123456789"
#lower = "abcdefghijklmnopqrstuvwxyz"
#upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#special = "!@#$%^&*()-+"

#Check if the password statisfies all the conditions
def min(n, password):
    digit = 1
    lower = 1
    upper = 1
    special = 1
    special_characters = "!@#$%^&*()-+"

    for i in range(n):
        if password[i].isupper():
            upper = 0
        elif password[i].islower():
            lower = 0
        elif password[i].isdigit():
            digit = 0
        elif password[i] in special_characters:
            special = 0

    total = digit + lower + upper + special

    if n < 6:
        ans = n + total
        if ans < 6:
            final = total + (6 - ans)
        else:
            final = total
    else:
        final = total

    return final

#User Input
if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    ans = min(n, password)
    print(ans)
