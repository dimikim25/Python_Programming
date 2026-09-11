# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 3
i = 0
# found = False

while i < len(nums):
    if nums[i] == target:
        print(f"{target} found.")
        # found = True
        break
    i += 1
# if not found:
else:
    print("NO TARGET")

# 1 ~ 10까지의 합

i = 0
tot = 0

while i <= 10:
    # tot += i if i % 2 == 0 else 0
    i += 1
    if i % 2 == 1:
        continue
    tot += i
print(f"sum : {tot}")
