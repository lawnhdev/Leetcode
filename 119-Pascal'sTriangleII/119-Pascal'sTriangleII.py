class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            ret = self.getRow(rowIndex - 1)
            # Initialize a new list of zeros with length len(existing_list) + 1
            pascal = [0] * (len(ret) + 1)
            pascal[0] = 1
            pascal[-1] = 1
            p_idx = 1
            for i in range(len(ret) - 1):
                pascal[p_idx] = ret[i] + ret[i + 1]
                p_idx += 1
            return pascal
