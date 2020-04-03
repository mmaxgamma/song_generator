import winsound
interval = 0



while interval <= 8:
    frequency = 440 * (2 ** (interval/12))
    winsound.Beep(round(frequency), 200)
    print(round(frequency))
    print(interval)
    interval = interval + 1
    
interval = 8

while interval > -1:
    frequency = 440 * (2 ** (interval/12))
    winsound.Beep(round(frequency), 200)
    print(round(frequency))
    print(interval)
    interval = interval - 1