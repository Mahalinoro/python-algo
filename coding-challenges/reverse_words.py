# Given an input string, reverse the string word by word

# Example:
# Input: "the sky is blue"
# Output: "blue is sky the"

class Solution:
    def reverseWords(self, s: str) -> str:      
        return " ".join(reversed(s.strip().split()))
    