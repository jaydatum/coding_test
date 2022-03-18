T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    min_num = nums[0]
    max_num = nums[0]
    
    for num in nums:
        if num < min_num:
            min_num = num
    
    for num in nums:
        if num > max_num:
            max_num = num
    
    answer = max_num - min_num
    
    print('#{} {}'.format(tc,answer))