# from typing import List
# def cumSum(nums: List[int]) -> int:
#     cum_sum_left = []
#     for i, x in enumerate(nums):
#         if i == 0:
#             cum_sum_left.append(0)
#         else:
#             cum_sum_left.append(cum_sum_left[-1] + nums[i-1])
#     return cum_sum_left

# print(cumSum([1,7,3,6,5,6]))
# print(list(reversed(cumSum(list(reversed([1,7,3,6,5,6]))))))

# print(sum([1, 2, 3, ]))


# cum_sum = []
# print(cum_sum[-1])

digits = [8,8,5,0,5,1,9,7]
remainder = 0
for i in range(len(digits) - 1, -1, -1):
    if i == len(digits) - 1:
        remainder, digits[i] = (1,0) if digits[i] == 9 else (0, digits[i] + 1)
        if len(digits) == 1 and remainder == 1:
            digits.insert(0, 1)
    elif i == 0:
        if digits[i] == 9 and remainder == 1:
            remainder, digits[i] = (1,0)
            digits.insert(0, 1)
        else:
            remainder, digits[i] = (0, digits[i] + remainder)
    else:
        remainder, digits[i] = (1,0) if digits[i] == 9 and remainder == 1 else (0, digits[i] + remainder)


print(digits)