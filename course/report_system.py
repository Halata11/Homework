requiredMoney = int(input())
cashMoney = 0
cashCount = 0
cardMoney = 0
cardCount = 0
isCash = True
cmd = input()
while cmd != "End":
    money = int(cmd)
    if isCash:
        if money > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cashMoney += money
            cashCount += 1
    else:
        if money < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cardMoney += money
            cardCount += 1
    if cashMoney + cardMoney >= requiredMoney:
        break
    isCash = not isCash
    cmd = input()
if cashMoney + cardMoney >= requiredMoney:
    avgCashMoney = cashMoney / cashCount
    avgCardMoney = cardMoney / cardCount
    print(f"Average CS: {avgCashMoney:.2f}")
    print(f"Average CC: {avgCardMoney:.2f}")
else:
    print("Failed to collect required money for charity.")