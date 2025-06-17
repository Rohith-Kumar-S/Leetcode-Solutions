

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = ''
        l = []
        for i, val in enumerate(s):
            a+=val
            if i+1 == len(s):
                l.append(len(a))
                break
            for val1 in s[i+1:]:
                if val1 in a:
                    break
                a+=val1
            l.append(len(a))
            a = ''
        return max(l) if l else 0
        
    

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(" ")) 