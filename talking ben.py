# Talking Ben Momento 
import time
import random
Ben = ["Ben.", "Yes.", "Ho-ho-ho...", "No...", "Ughh."]
print(Ben[0])
'''
while True:
    BenRandInt = random.randrange(1, len(Ben))
    sus = input("VOpros - ")
    if BenRandInt == 1:
        time.sleep(2)
        print(Ben[1])
    elif BenRandInt == 2:
        time.sleep(2)
        print(Ben[2])
    elif BenRandInt == 3:
        time.sleep(2)
        print(Ben[3])
    elif BenRandInt == 4:
        time.sleep(2)
        print(Ben[4])
    elif BenRandInt == 5:
        print(Ben[2])
        time.sleep(1)
        print(Ben[3])
'''
Tru = True
while Tru:
    Vopros = input("Question - ")
    print(Ben[random.randint(1, len(Ben)-1)])
    if Vopros == 'Break':
        Tru = False

