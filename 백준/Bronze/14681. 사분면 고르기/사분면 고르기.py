x_coo = float(input())
y_coo = float(input())

if x_coo > 0 and y_coo > 0:
    Quadrant = 1
elif x_coo < 0 and y_coo > 0:
    Quadrant = 2
elif x_coo < 0 and y_coo < 0:
    Quadrant = 3
elif x_coo > 0 and y_coo < 0:
    Quadrant = 4
print(Quadrant)