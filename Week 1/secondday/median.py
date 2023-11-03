def find_median_sorted_lists(nums1, nums2):
    merged = []
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    
    total = len(merged)
    
    if total % 2 == 0:
        middle1 = total // 2
        middle2 = middle1 - 1
        return (merged[middle1] + merged[middle2]) / 2.0
    else:
        middle = total // 2
        return merged[middle]

# Example usage:
nums1 = [1,3,5,7,9]
nums2 = [2,55,22,44]
median = find_median_sorted_lists(nums1, nums2)
print("The median is:", median)