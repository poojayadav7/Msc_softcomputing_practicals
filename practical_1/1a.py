# simple linear neuron with clipping activation in [0,1]
x = float(input("Enter value of x: "))
w = float(input("Enter value of weight w: "))
b = float(input("Enter value of bias b: "))

net = w * x + b   # keep as float
if net < 0:
    out = 0.0
elif net <= 1:
    out = net
else:
    out = 1.0

print(f"net = {net}")
print(f"output = {out}")

