x_min, y_min, z_min = map(float, input().split(','))
x_max, y_max, z_max = x_min, y_min, z_min 

while ((str := input()) != ""):
    x, y, z = map(float, str.split(','))
    x_min = min(x_min, x)
    y_min = min(y_min, y)
    z_min = min(z_min, z)
    x_max = max(x_max, x)
    y_max = max(y_max, y)
    z_max = max(z_max, z)

v = (x_max - x_min) * (y_max - y_min) * (z_max - z_min)
print(v)