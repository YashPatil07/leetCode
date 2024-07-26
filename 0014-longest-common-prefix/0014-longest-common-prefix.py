class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = min(len(ele) for ele in strs)
        if res==0:
            return ""
        result=""
        for i in range(res):
            chara=strs[0][i]
            for j in range(1,len(strs)):
                if(strs[j][i]!=chara):
                    return result
            result+=strs[0][i]
        return result