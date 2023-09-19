BUS_PRICE = 200
TRUCK_PRICE = 175
TRAIN_PRICE = 120
BUS_TONNAGE = 3
TRUCK_TONNAGE = 11
busTons = 0
truckTons = 0
trainTons = 0
n = int(input())
for i in range(n):
    tons = int(input())
    if tons <= BUS_TONNAGE:
        busTons += tons
    elif tons <= TRUCK_TONNAGE:
        truckTons += tons
    else:
        trainTons += tons
totalTons = busTons + truckTons + trainTons
avgPricePerTon = (busTons * BUS_PRICE + truckTons * TRUCK_PRICE + trainTons * TRAIN_PRICE) / totalTons
busPercent = busTons / totalTons * 100
truckPercent = truckTons / totalTons * 100
trainPercent = trainTons / totalTons * 100
# print('%.2f' % avgPricePerTon)
# print('{:.2f}'.format(avgPricePerTon))
print(f'{avgPricePerTon:.2f}')
print(f'{busPercent:.2f}%')
print(f'{truckPercent:.2f}%')
print(f'{trainPercent:.2f}%')
