num_list=[1,2,3,4,5]
count={i: 0 for i in range(1, 6)}

for i in range(1, 6):
    for num in num_list:
        if num % i == 0:
            count[i] += 1
print(count)
