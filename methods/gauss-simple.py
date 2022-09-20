from numpy import array, zeros, fabs, linalg

a = array([[14, 6, -2, 3], [3, 15, 2, -5],
           [-7, 4, -23, 2], [1, -3, -2, 16]])
b = array([12, 32, -24, 14])

#a[1] = a[1] - (a[0]/14)*3
print(a)

print("Solution by NumPy:")
print(linalg.solve(a, b))

n = len(b)
x = zeros(n, float)

# first loop specifys the fixed row
for k in range(n-1):
    if fabs(a[k, k]) < 1.0e-12:

        for i in range(k+1, n):
            if fabs(a[i, k]) > fabs(a[k, k]):
                a[[k, i]] = a[[i, k]]
                b[[k, i]] = b[[i, k]]
                break
 # applies the elimintion below the fixed row
    for i in range(k+1, n):
        if a[i, k] == 0:
            continue

        factor = a[k, k]/a[i, k]
        print(factor)
        a[i] = a[k] - a[i]*factor
        b[i] = b[k] - b[i]*factor
        print(a, b)
print(a)
print(b)


x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    sum_ax = 0

    for j in range(i+1, n):
        sum_ax += a[i, j] * x[j]

    x[i] = (b[i] - sum_ax) / a[i, i]

print("The solution of the system is:")
print(x)
