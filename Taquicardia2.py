import time
import neurokit2 as nk
import os
import random

def Cinderela():
    time.sleep(1)
    os.system("clear")

def Heart():
    heart_rate = random.randint(60, 70)
    
    # Generate a realistic ECG signal
    simulated_ecg = nk.ecg_simulate(duration=60, sampling_rate=100, heart_rate=heart_rate)
    
    # Find R-peaks and calculate heart rates
    rpeaks = nk.ecg_findpeaks(simulated_ecg, sampling_rate=100)
    heart_rates = nk.ecg_rate(rpeaks, sampling_rate=100)
    
    return heart_rates

def Shock():
    print("You get hypershocked Zzzz..")

beats = Heart()  # Call the heart() function and assign the result to heart_beat
i = 0
for j in range(len(beats)):
    print(f"""    |-----------------------|
    |   {beats[j]}   |
    |-----------------------|""")
    if beats[j] >= 70:
        Shock()
    i += 1
    Cinderela()

print(f"At totaly {i} beats your haeart performed.")