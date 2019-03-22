A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum_A = 0
index = 0
while index < len(A):
    if A[index] >= 50:
            sum_A += A.pop(index)
    index += 1
print(sum_A)