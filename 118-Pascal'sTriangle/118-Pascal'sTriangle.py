class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return [[]]
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            ret = self.generate(numRows - 1)
            temp = ret[-1]
            # Initialize a new list of zeros with length len(existing_list) + 1
            pascal = [0] * (len(temp) + 1)
            pascal[0] = 1
            pascal[-1] = 1
            p_idx = 1
            for i in range(len(temp) - 1):
                pascal[p_idx] = temp[i] + temp[i + 1]
                p_idx += 1
            ret += [pascal]
            print(ret)
            return ret

