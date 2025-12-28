# enter the no of inputs
num_ip = int(input("Enter the number of inputs : "))

# Set the weights with value 1
w1 = 1
w2 = 1

print("For the", num_ip, "inputs calculate the net input using yin = x1w1 + x2w2")

x1 = []
x2 = []

for j in range(0, num_ip):
    ele1 = int(input("x1 = "))
    ele2 = int(input("x2 = "))
    x1.append(ele1)
    x2.append(ele2)

print("x1 =", x1)
print("x2 =", x2)

# Step 1: Calculate Yin = x1w1 + x2w2
n = [i * w1 for i in x1]
m = [i * w2 for i in x2]

Yin = []
for i in range(0, num_ip):
    Yin.append(n[i] + m[i])
print("Yin =", Yin)

# Step 2: Assume one weight as excitatory and the other as inhibitory
Yin = []
for i in range(0, num_ip):
    Yin.append(n[i] - m[i])
print("After assuming one weight as excitatory and the other as inhibitory, Yin =", Yin)
# Step 3: Apply threshold θ ≥ 1
# The neuron fires (Y = 1) if Yin >= 1, otherwise Y = 0
Y = []
for i in range(0, num_ip):
    if Yin[i] >= 1:
        ele = 1
        Y.append(ele)
    else:
        ele = 0
        Y.append(ele)

print("Y =", Y)
