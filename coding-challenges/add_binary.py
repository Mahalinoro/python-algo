# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

# Example:
# Input: a = "11", b = "1"
# Output: "100"

class Solution:
    # Convert Decimal to Binary 
    def convertDectoBin(self, k):
        binary = ""
        
        quotient = k // 2
        binary += str(k % 2)
        
        while quotient:
            binary += str(quotient % 2)     
            quotient = quotient // 2
            
        return binary[::-1]
        
     # Convert Binary to Decimal
    def convertBintoDec(self, k):
        dec = 0
        n = 0
        
        for i in range(len(k)-1, -1, -1):
            dec += 2**n * int(k[i])
            n += 1
        
        return dec
            
    def addBinary(self, a: str, b: str) -> str:
        return self.convertDectoBin(self.convertBintoDec(a) + self.convertBintoDec(b))