total_sec=int(input("Enter the total seconds: "))
hour=total_sec//3600
rem_sec=total_sec%3600
min=rem_sec//60
sec=rem_sec%60
print(f'Hour: {hour} Minutes: {min} Seconds: {sec}')