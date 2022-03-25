T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    answer = max(nums) - min(nums)
    #여기에 문제 로직이 들어갑니다.
 
    
    # 최종 출력 예시
    print('#{} {}'.format(tc,answer))