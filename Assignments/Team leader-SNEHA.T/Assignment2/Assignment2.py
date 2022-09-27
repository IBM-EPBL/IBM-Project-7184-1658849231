import random

temp = random.randint(10,100)
print("Enter temperature:",temp)

humidity = random.randint(10,100)
print("Enter Humidity:",humidity)

if (temp>40):
    if (humidity>30):
        print("ALERT detected....DANGER")
    else:
        print("High temperature")
elif temp==40:
    print("Reached maximum temperrature")
else:
    print("all good")