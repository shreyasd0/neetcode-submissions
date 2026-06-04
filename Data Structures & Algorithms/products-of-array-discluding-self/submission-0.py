class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward=[]
        prod=1
        for i in nums:
            prod=prod*i
            forward.append(prod)
        print(forward)

        backward=[]
        prd=1
        for i in nums[::-1]:
            prd=prd*i
            backward.append(prd)
        backward=backward[::-1]
        print(backward)

        op=[backward[1]]
        for i  in range(1,len(nums)-1):
            op.append(forward[i-1]*backward[i+1])
        op.append(forward[-2])
        return op

            