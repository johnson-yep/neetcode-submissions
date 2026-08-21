class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = ""
        encodedStr = ""
        for s in strs:
            lengths += str(len(s)) + ","
            encodedStr += s

        return lengths + "#" + encodedStr
            
    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []
        lengths = []
        num = ""
        i = 0
        while s[i] != "#":
            if s[i] != ",":
                num += s[i]
            else:
                lengths.append(int(num))
                num = ""
            
            i+=1
        
        i+=1
        for leng in lengths:
            strs.append(s[i:i+leng])
            i+=leng

        return strs

