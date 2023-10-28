#Check Alphabets vovel or consonant or not a alphabets

ch = input("Enter a character : ")
if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
    if(ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")
else:
    print(ch,'Is not an alphabet')
