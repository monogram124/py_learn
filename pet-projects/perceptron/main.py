def bubble_sort(nums):
    for num in range(1, len(nums)):
        for i in range(1, len(nums)-1-num):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[len(nums) // 2]
    less = []
    greater = []

    for num in nums:
        if num == pivot:
            continue

        if num < pivot:
            less.append(num)
        else:
            greater.append(num)
        
    return quick_sort(less) + [pivot] + quick_sort(greater)

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return True
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

def merge_two_lists(a, b):
    i = j = 0
    res = []

    if i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
        
    if i < len(a):
        res += a[i:]
    
    if j < len(b):
        res += b[j:]
    
    return res