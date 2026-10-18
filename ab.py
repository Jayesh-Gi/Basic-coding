readings = 0
total = 0
peak = 0
alerts = 0
current_streak = 0
longest_streak = 0
critical = False

while True:
    reading = int(input())

    if reading == -1:
        break

    if reading < 0 or reading > 5000:
        continue

    readings += 1
    total += reading

    if readings == 1 or reading > peak:
        peak = reading

    if reading >= 2000:
        alerts += 1
        current_streak += 1

        if current_streak > longest_streak:
            longest_streak = current_streak

        if current_streak >= 3:
            critical = True
    else:
        current_streak = 0

if readings == 0:
    print("No valid readings")
else:
    average = total / readings
    print("Readings:", readings)
    print(f"Average: {average:.2f}")
    print("Peak:", peak)
    print("Alerts:", alerts)
    print("Longest streak:", longest_streak)
    print("Critical:", "YES" if critical else "NO")