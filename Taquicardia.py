import time
import random
import os

def Cinderela():
    time.sleep(1)
    os.system("clear")

def Heart():
    heart_beat = []
    for i in range(60):
        heart_beat.append(random.randint(55, 120))
    return heart_beat

def Shock():
    print("You get hypershocked Zzzz..")

beats = Heart()  # Call the heart() function and assign the result to heart_beat

for j in range(len(beats)):
    print(beats[j])
    if beats[j] >= 70:
        Shock()
        
    Cinderela()