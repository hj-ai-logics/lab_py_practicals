
signal = input("Enter the traffic signal color (Red/Yellow/Green): ")

if signal == "red":
    print(" Stop! Wait until the signal turns green.")
elif signal == "yellow":
    print(" Slow down and prepare to stop.")
elif signal == "green":
    print(" Go! Drive safely.")
else:
    print(" Invalid signal color. Please enter Red, Yellow, or Green.")
