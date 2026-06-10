class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minimum = min(nums)
        maximum = max(nums)

        x = [0] * (maximum - minimum + 1)

        for num in nums:
            x[num - minimum] += 1

        indices = sorted(
            range(len(x)),
            key=lambda i: x[i],
            reverse=True
        )

        return [i + minimum for i in indices[:k]]