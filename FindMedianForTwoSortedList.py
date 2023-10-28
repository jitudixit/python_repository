from statistics import median
import sys
from typing import Type

nums1 = [1,3]
nums2 = [2]

m = len(nums1)
n = len(nums2)

print(m)
print(n)
nums3 = nums1 + nums2
nums3.sort()
print(nums3)
start = 0
end = len(nums3)
median = start + end / 2
print(median)
#if m % 2 == 0 & n % 2 == 0:

