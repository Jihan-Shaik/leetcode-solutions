class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s=""
        for i in title.split():
            if len(i)>2: s+=i.title()+" "
            else: s+=i.lower()+" "
        return s.rstrip()