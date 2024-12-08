class Solution:
    # O(n), while n == max(len(s), len(n))
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
