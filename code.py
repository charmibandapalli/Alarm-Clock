import time
import os

alarm_time = input("Enter alarm time (HH:MM): ")
while True:
    if time.strftime("%H:%M") == alarm_time:
        os.system("start alarm.mp3")
        break
    time.sleep(30)
