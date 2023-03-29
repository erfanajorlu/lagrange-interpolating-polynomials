# Erfan Ajorlu Lagrange implement
def multi(A, B):
    s = len(A) + len(B) - 1
    ans = []
    for i in range(s):
        ans.append(0)
    for i in range(len(A)):
        for j in range(len(B)):
            ans[i+j] += A[i] * B[j]
    return ans


def L1(x, i):
    m = 1
    ans = []
    for j in x:
        if x[i] - j == 0:
            pass
        else:
            m *= (x[i] - j)
    for j in range(len(x)):
        if j == i:
            pass
        else:
            p = [-1 * x[j], 1]
            ans.append(p)

    for j in range(1, len(ans)):
        ans1 = multi(ans[0], ans[j])
        ans[0] = ans1

    for j in range(len(ans[0])):
        ans[0][j] = ans[0][j] / m
    return ans[0]


def calc(p, x):
    ans = 0
    for i in range(len(p)):
        ans += p[i] * (x ** i)
    ans = round(ans, 4)
    return ans


n = int(input("Enter n->"))

x = []
f = []
L = []

for i in range(n):
    x1 = float(input(f"Enter x{i} ->"))
    x.append(x1)
    x1 = float(input(f"Enter f{i} ->"))
    f.append(x1)

for i in range(n):
    L.append(L1(x, i))

P = []

for i in range(n):
    P.append(0)

for i in range(n):
    for j in range(len(L[i])):
        P[j] += f[i] * L[i][j]
for i in range(n):
    P[i] = round(P[i], 4)
for i in range(n-1, 0, -1):
    print(f"({P[i]} x^{i})", end="+ ")

print(f"({P[0]} x^{0})")
calculate = True
while calculate:
    print("do you want to calculate any x?")
    s = int(input("""1-YES
2-No
"""))
    if s == 2:
        calculate = False
    else:
        m = float(input("enter your number ->"))
        ans = calc(P, m)
        print(ans)
print("Good By")
