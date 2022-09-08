bal = 0
while True:
    amount = input()
    if amount == " ":
        break
    else:
        amt = amount.split(" ")
        if amt[0] == 'D' or amt[0] == 'd':
            bal = bal + int(amt[1])
        if (amt[0] == 'W' or amt[0] == 'w') and (int(amt[1]) < bal):
            bal = bal - int(amt[1])
print(bal)