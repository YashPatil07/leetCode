class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        answer = []
        temp = [1]
        ans = 1
        for row in range(1, numRows + 1):
            for col in range(1, row):
                ans = ans * (row - col) // col
                temp.append(ans)
            answer.append(temp[:])  # Add a copy of temp to answer
            temp = [1]  # Reset temp for the next row
            ans = 1
        return answer
