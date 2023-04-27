x = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k):
                x+=1
                print(i, j, k)
print(x)



I = int(input('profit = '))
if I <= 10:
    x = I*0.1
elif 10 < I and I <= 20:
    x = 10*0.1 + (I - 10)*0.075
elif 20 < I and I <= 40:
    x = 10*0.1 + 10*0.075 + (I - 20)*0.05
elif 40 < I and I <= 60:
    x = 10*0.1 + 10*0.075 + 20*0.05 + (I - 40)*0.03
elif 60 < I and I <= 100:
    x = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + (I - 60)*0.015
else:
    x = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + 40*0.015 + (I - 100)*0.01
print(x)