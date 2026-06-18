import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        array=[]
        for i in strs :
            array.append(str(len(i)))
            array.append("#")
            array.append(i)
        return "".join(array)



    def decode(self, s: str) -> List[str]:
        array =[]
        point = 0
        lenght = []
        word = []
        i=0
        while(i<len(s)):
            while(s[i]!="#"):
                lenght.append(s[i])
                i+=1
            for j in range(i+1,i+1+int("".join(lenght))):
                word.append(s[j])
            array.append("".join(word))
            i= i+1+int("".join(lenght))
            lenght =[]
            word=[]
        return array


    
