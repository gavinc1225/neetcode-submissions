class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # find length of string 
            i = j + 1 # move i past the hashtag
            j = i + length # move j to respective length
            res.append(s[i:j]) # add encoded string
            i = j # set i to the end and continue
        return res

