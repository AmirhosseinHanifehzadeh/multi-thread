from turtle import right


r, c = list(map(int, input().split()))

if c <= 10 : 
    directionCommand = 'Right'
    numberOfSeats = c
else:
    directionCommand = "Left"
    numberOfSeats = 21 - c

print(f"{directionCommand} {11 - r} {numberOfSeats}")

