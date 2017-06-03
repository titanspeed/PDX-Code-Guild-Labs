total = 0
nums = [1, 2, 3, 4, 5]


def incremental(nums):
    global total
    while True:
        for i in nums:
            total += i
            print(total)

incremental(nums)


