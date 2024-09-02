class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n=len(matrix)
        m=len(matrix[0])
        
        #initialize the pointers read for traversal
        top=0
        bottom = n-1
        left=0
        right = m-1
        # left to right
        while(left <= right and top <= bottom):
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1    

            # top to bottom
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1

            # right to left   
            if top <= bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1

            #bottom to top
            if (left <= right):
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
            
        return ans 
        