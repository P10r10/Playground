class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for letter in letters:
            if target < letter:
                return letter
        return letters[0]


print(Solution().nextGreatestLetter(["c", "f", "j"], "a"))
print(Solution().nextGreatestLetter(["c", "f", "j"], "c"))
print(Solution().nextGreatestLetter(["x", "x", "y", "y"], "z"))
