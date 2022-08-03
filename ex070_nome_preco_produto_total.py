#program that reads the name and the price from several products. It must ask if
#continue or not. In the end show: total spent, how many products more than
#R$ 1000. What is the name of the cheapest product
count = 0
totprice = 0
cheapest = 0
prodcheap = " "
thousand = 0
while True:
    product = str(input("type the name of the product: "))
    price = float(input("type it's price: "))
    count += 1
    if count == 1 or price < cheapest:
        cheapest = price
        prodcheap = product 
    totprice += price
    if price > 1000:
        thousand += 1
    continum = input("Do you want to continue? Any key to continue. 'N' to exit: ").upper()
    if continum == "N":
        break
print(f"The total amount spent was R${totprice:.2f}")
print(f"There were(was) {thousand} product(s) above R$ 1000.00")
print(f"The cheapest product was {prodcheap}")

