
def adjacentElementsProduct(inputarray):
    for n in list_range:
        if n < list_range[-1]:
            total = nums[n] * nums[n+1]
            if total > highest:
                highest = total
                indexa = n
                indexb = n + 1



import math

nums = [18, -6, 19, -4, 9, -5, 15]

highest = -math.inf
indexa = None
indexb = None

list_range = list(range(len(nums)))

for n in list_range:
    if n < list_range[-1]:
        total = nums[n] * nums[n+1]
        if total > highest:
            highest = total
            indexa = n
            indexb = n + 1

print(highest)
print(nums[indexa])
print(nums[indexb])
