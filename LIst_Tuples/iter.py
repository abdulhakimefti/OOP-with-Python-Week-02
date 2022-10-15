nums = [324, 5324, 131, 142, 354]
nums_iter = iter(nums)
# print(nums_iter);
# print(list(nums_iter))
print(next(nums_iter))
print(next(nums_iter))
try:
    print(next(nums_iter))
    print(next(nums_iter))
    print(next(nums_iter))
    print(next(nums_iter))
    print(next(nums_iter))
    print(next(nums_iter))
except StopIteration:
    print("done")
