class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        n = len(s)
        c = 0
        for i in range(n//2):
            if s[i] in vowels:
                c+=1
            if s[i+n//2] in vowels:
                c-=1
        return c==0