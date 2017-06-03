# import math
#
# highest = -math.inf
# indexa = None
# indexb = None
#
#
# def adjacentElementsProduct(inputarray):
#     list_range = range(len(inputarray))
#     for n in list_range:
#         if n < list_range[-1]:
#             total = inputarray[n] * inputarray[n + 1]
#             highest = total
#             if total > highest:
#                 indexa = n
#                 indexb = n + 1
#
#
# print(highest)
# print(inputarray[indexa])
# print(inputarray[indexb])

# def adjacentElementsProduct(inputArray):
#     return len([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

