class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for i in s:
            if i == " ":
                continue
            elif i.isalnum():
                cleaned+=i.lower()
        return cleaned==cleaned[::-1]
        