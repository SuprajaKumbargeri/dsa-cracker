# Link to Leetcode problem: https://leetcode.com/problems/rotate-array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # reverse the whole array, then reverse individual slices
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        # TC: O(klog(k) + (n-k)log(n-k) + nlog(n))
        # SC: O(n) - temporary arrays for reversed()
        
        # Notice how reversed(list) gives a new reversed list similar to sorted(list)
        # and list.reverse() reverses the list in place list list.sort()

        # smart slicing method
        '''
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        '''
        

        '''
        # Cyclic replacements
        if k == 0: return

        n = len(nums)
        if k > n: k %= n

        swaps = n
        i = -1
        start = -1
        prev = nums[0] # initial val to swap (itself)

        while swaps:
            if start == i:
                start = i = i + 1
                nums[i], prev = prev, nums[i]
            
            i = (i + k) % n
            nums[i], prev = prev, nums[i]
            swaps -= 1
        '''
        # You could also reverse the array, multiple times.

        """
        # previous attempt
         n = len(nums)
        if k % n == 0:
            return

        while k > n:
            k -= n

        swaps = 0
        start = 0
        curr = 0
        toStore = nums[curr]

        while (swaps < n):
            
            
            newIndex = curr + k
            if newIndex >= n:
                newIndex -= n
            
            temp = nums[newIndex]
            nums[newIndex] = toStore
            curr = newIndex
            toStore = temp
            
            if curr == start:
                start = curr = start + 1
                toStore = nums[curr]
            swaps += 1
        """
