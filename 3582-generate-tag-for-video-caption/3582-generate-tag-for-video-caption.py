class Solution:
    def generateTag(self, caption: str) -> str:
        if caption.isspace(): return "#"
        s="#"+caption.title().lstrip(" ")
        s=s.replace(" ","")
        s=s[0]+s[1].lower()+s[2:]
        return s if len(s)<=100 else s[:100]