class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_of_ones = bin(num2).count('1')
        result = []
        for bit in bin(num1)[2:]:
            if num_of_ones == 0:
                result.append('0')
                continue

            if bit == '1':
                result.append('1')
                num_of_ones -= 1
            else: # bit == '0'
                result.append('0')

        for i, bit in enumerate(result[::-1]):
            if num_of_ones == 0:
                break
            if bit == '0':
                result[-1*(i+1)] = '1'
                num_of_ones -= 1

        while num_of_ones != 0:
            result.append('1')
            num_of_ones -= 1

        return int(''.join(result), 2)
