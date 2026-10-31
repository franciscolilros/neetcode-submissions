class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            for j in i:
                res += str(ord(j))
                res += "/"
            res += "-"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        temp = ""
        curr = ""
        for i in s:
            if i == "/":
                temp += chr(int(curr))
                curr = ""
            elif i == "-":
                res.append(temp)
                temp = ""
            else:
                curr += i
        return res