sent=input("Enter a sentence!\n")
lst=sent.split(" ")
LetterCount=0
DigitCount=0
for i in range(len(lst)):
    if lst[i].isalpha():
        lst[i].strip()
        LetterCount+= len(lst[i])
    if lst[i].isdigit():
        lst[i].strip()
        DigitCount+=len(lst[i])
print("Letters count= ", LetterCount)
print("Digit count= ", DigitCount)