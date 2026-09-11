# for문

# for (int i = 0; i < 10; i++)              ... c
# for i in iterable(반복 가능한) 객체:       ... python

for i in range(5):  # 0 ~ 4
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step, a)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

# 1 ~ 10 step = 2
for i in range(1, 10, 2):
    print(i, end=" ")
print()

# 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10 sum
tot = 0

for i in range(1, 11):
    tot += i
print(tot)
print(sum(range(1, 11)))

s = "dz45@#한글逸¥€⚙️📗"

for c in s:
    print(c, end=" ")
print()

print(len(s))

# 구구단 출력
# 2 * 1 = 2 ....

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()
