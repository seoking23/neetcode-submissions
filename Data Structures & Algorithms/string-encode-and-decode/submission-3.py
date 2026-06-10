class Solution:
    def encode(self, strs: List[str]) -> str:
        finalString = ""
        for string in strs:
            finalString += "/" + str(len(string)) + "/" + string 
        return finalString

    def decode(self, s: str) -> List[str]:
        finalString = []
        i = 0
        while  i < len(s) and s[i] == "/":
            i += 1
            lengthString = ""
            while s[i] != "/":
                lengthString += s[i]
                i += 1
            i += 1
            finalString.append(s[i:i+int(lengthString)])
            i += int(lengthString) 
            
        return finalString
