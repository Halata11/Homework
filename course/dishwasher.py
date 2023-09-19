bottles = int(input())
liquid = bottles*750
index = 0
dishes = 0
pots = 0
cmd = input()
while cmd != "End":
    num = int(cmd)
    if index % 3 == 2:
        liquid -= num * 15
        pots += num
    else:
        liquid -= num * 5
        dishes += num
    index += 1
    if liquid < 0:
        break
    cmd = input()
if liquid >= 0:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {liquid} ml.")
else:
    print(f"Not enough detergent, {-liquid} ml. more necessary!")

