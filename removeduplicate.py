
class Solution:
    nums=[1,2,2,2,3,3,4]
    seen = set()

    for num in nums:

        if num not in seen:
            seen.add(num)
        else:
            nums.remove(num)
    print(seen)
    print(nums)
    