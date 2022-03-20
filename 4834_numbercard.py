"""0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
"""

"""T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    
    sum_list = []
    
    for i in range(N-M+1):
        sum_list.append(sum(nums[i:i+M]))
    
    answer = max(sum_list) - min(sum_list)
    print('#{} {}'.format(tc,answer))"""
    
T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    
    sum_list = []
    
    for i in range(N-M+1):
        sum_range = 0 # 초기값
        for j in nums[i:i+M]:
            sum_range += j
        sum_list.append(sum_range)
    
    min_num = sum_list[0]
    max_num = sum_list[0]
    
    for z in sum_list:
        if z < min_num:
        min_num = z
    
    for z in sum_list:
        if z > max_num:
            max_num = z
    
    answer = max_num - min_num
            
    print('#{} {}'.format(tc,answer))
