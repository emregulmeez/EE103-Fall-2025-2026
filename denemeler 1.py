for v in range (12,25,12):
    for r in range (20,61,20):
        p=(v**2)/r
        if p>10:
            print(f"ERROR!!! Power has exceeded the safe limits.\n Power:{p}\n Voltage:{v}\n Resistance:{r}")
        else:
            print(f"Power has not exceeded the safe limits.\n Power:{p}\n Voltage:{v}\n Resistance:{r}")

