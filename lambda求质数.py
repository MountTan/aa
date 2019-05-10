nums = range(2, 20)
for i in nums:
    nums = list(filter(lambda x: x == i or x % i, nums))
print(nums)


