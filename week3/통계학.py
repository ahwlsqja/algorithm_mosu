import sys

input = lambda: sys.stdin.readline().strip()
N = int(input())
nums = [N]

for i in range(N):
    num = int(input())
    nums.append(i)


nums = nums.sort()
temp = 0
for i in nums:
    temp += i

print(f"{temp/N:.1f}")
print(nums[N//2])

print(max(nums) - min(nums))

