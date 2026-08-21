class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output
            
    def decode(self, s: str) -> List[str]:
        i = 0
        strs=[]
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i+=1
            i+=1
            string = ""
            for j in range(int(length)):
                string += s[i]
                i+=1
            strs.append(string)

        return strs
