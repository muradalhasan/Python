dist=int(input("Enter the distance: "))
time=int(input("Enter the time in sec: "))
dist1=dist/1000
time1=time/3600
speed=dist1/time1
if speed<=60:
    print("Too slow! needs more changes")
elif speed >60 and speed <=90:
    print("Velocity is okay! The car is ready")
else:
    print("Too fast. Only a few changes should suffice.")