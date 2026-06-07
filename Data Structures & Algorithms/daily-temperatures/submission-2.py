class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [temperatures[0]]
        res = [0] * n

        for i in range(1, n):

            if stack[-1]  < temperatures[i] :
                index = i 
                counter = 1

                while stack and stack[-1] < temperatures[i] :
                    print ('while loop:' ,stack, 'index: ', index)
                    index -= 1
                    if res[index] == 0 :
                        stack.pop()
                        res[index] = counter
                    counter += 1

            stack.append(temperatures[i])
            
        
        return res