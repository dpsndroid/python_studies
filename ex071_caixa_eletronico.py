#program that simulates an ATM. Ask what will be the amount withdraw. Inform
#how many money bills will be delivered. Consider money bills from 1,10,20,50
money = 0
while True:
    one = 0
    five = 0
    ten = 0
    twenty = 0
    fifty = 0
    print("====" * 20)
    money = int(input("How much money do you need? "))
    if money > 49:
        fifty = int(money / 50)
        money = money - (50 * fifty)
    if money >= 19:
        twenty = int(money / 20)
        money = money - (20 * twenty)
    if money > 9:
        ten = int(money / 10)
        money = money - (10 * ten)
    if money > 4:
        five = int(money / 5)
        money = money - (5 * five)
    if money > 0:
        one = int(money / 1)
        money = money - (1 * one)

        
    print("You need {:2} bill(s) of R$ 50,00".format(int(fifty)))
    print("You need {:2} bill(s) of R$ 20,00".format(int(twenty)))
    print("You need {:2} bill(s) of R$ 10,00".format(int(ten)))
    print("You need {:2} bill(s) of R$  5,00".format(int(five)))
    print("You need {:2} bill(s) of R$  1,00".format(int(one)))
    continum = str(input("Continue? Any key to continue. 'N' to stop: ")).upper()
    if continum == "N":
        break
print("====" * 20)
print("Could you lend me some money?")
print("""

OTHER WAY

""")
print("====" * 20)
money = int(input("How much money do you need? "))
total = money
bill = 50
totbill = 0
while True:
    if total >= bill:
        total -= bill
        totbill += 1
    else:
        if totbill > 0 :
            print(f"Total of {totbill} bill(s) of R${bill}")
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 5
        elif bill == 5:
            bill = 1
        totbill = 0
        if total == 0:
            break
print("====" * 20)
print("Come back soon")

        
    
