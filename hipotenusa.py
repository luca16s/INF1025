import math
b = 16
c = 10
theta = 60
thetaInRadians = math.radians(theta)
a = math.ceil((b**2 + c**2 - 2*b*c*math.cos(thetaInRadians))**0.5)
print(a)
