s = input()
for i in range(len(s)):
    if s[i].isupper():
        print(s[i].lower(), end='')
    else: 
        print(s[i].upper(), end='')