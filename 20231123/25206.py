subject = [0]*20
weight = [0]*20
grade = [0]*20

for i in range(20):
    subject[i], weight[i], grade[i] = input().split()

    weight[i] = float(weight[i])

sum = 0
sum_weight = 0
for i in range(20):
    if grade[i] != 'P':
        if grade[i] == 'A+':
            sum = sum + weight[i]*4.5
            sum_weight = sum_weight + weight[i]
        elif grade[i] == 'A0':
            sum = sum + weight[i]*4.0
            sum_weight = sum_weight + weight[i]
        elif grade[i] == 'B+':
            sum = sum + weight[i]*3.5
            sum_weight = sum_weight + weight[i]
        elif grade[i] == 'B0':
            sum = sum + weight[i]*3.0
            sum_weight = sum_weight + weight[i]
        elif grade[i] == 'C+':
            sum = sum + weight[i]*2.5
            sum_weight = sum_weight + weight[i]
        elif grade[i] == 'C0':
            sum = sum + weight[i]*2.0
            sum_weight = sum_weight + weight[i]
        elif grade[i] == 'D+':
            sum = sum + weight[i]*1.5
            sum_weight = sum_weight + weight[i]
        elif grade[i] == 'D0':
            sum = sum + weight[i]*1.0
            sum_weight = sum_weight + weight[i]
        elif grade[i] == 'F':
            sum = sum + weight[i]*0
            sum_weight = sum_weight + weight[i]
    else:
        continue

mean = float(sum/sum_weight)

print(mean)

