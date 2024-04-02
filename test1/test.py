import random
#num = int(input("Enter number = "))
#for i in range(1,(num // 2) + 1):
#    if (num % i == 0):
#        print(f"{i} is a factor of {num}")

def un_fair_coin_flip(probability):
    if (random.random() < probability):
        return "head"
    else:
        return "tail"

head_tally = 0
tail_tally = 0
for i in range(10_000):
    if (un_fair_coin_flip(0.25) == "head"):
        head_tally += 1
    else:
        tail_tally += 1

print(head_tally)
print(tail_tally)
