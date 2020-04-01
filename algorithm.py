"""
<완전 탐색 알고리즘으로 개대충 테스팅>

아이디어:

시간대 x 사람 의 2 by 2 array, 가능하면 1 불가능하면 0을 담고 있음. 
아직 배정이 안된 사람의 list [], 배정이 되면 list에서 pop()
그 시간대마다 배정된 사람의 list [], 배정이되면 list에 append 해주기

만약 list가 다 찼고,(max 6) 그 시간대만 되는 사람이 있으면, 실패.
unassigned가 비어있으면 성공.

만약 프로그램이 그냥 리턴하고 끝나면 맞는 시간표가 없는 거. 
결과를 프린트하고 끝나면 성공한거!!!


              1시  2시 3시  4시 5시  6시 7시  8시
-------------------------------------- 
면접자1         0   0   1   1   0   1   1   1
면접자2         0   0   0   0   0   1   1   1
면접자3         0   0   0   0   0   0   1   1
면접자4         0   1   0   0   0   0   0   0
면접자5         1   0   1   1   0   1   1   1
면접자6         1   0   1   1   0   1   1   1
면접자7         1   0   1   1   0   1   1   1
면접자8         1   0   1   1   0   1   1   1
면접자9         1   0   1   1   0   1   1   1
면접자10        1   0   1   1   0   1   1   1
면접자11        1   0   1   1   0   1   1   1

"""

availability = [[0,0,1,1,0,1,1,1],
                [0,0,0,0,0,1,1,1],  
                [0,0,0,0,0,0,1,1],
                [0,1,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1],
                [0,0,1,0,0,1,1,1],
                [0,1,1,1,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,0,0,0,0],
                [0,1,1,1,1,0,1,1]]


#재귀호출
def solve(unassigned,schedule,n):

    # 성공 기저 사례: unassigned가 한명도 없을 때
    if len(unassigned)==0:
        print('time1:')
        print(schedule[0])
        print('time2:')
        print(schedule[1])
        print('time3:')
        print(schedule[2])
        print('time4:')
        print(schedule[3])
        print('time5:')
        print(schedule[4])
        print('time6:')
        print(schedule[5])
        print('time7:')
        print(schedule[6])
        print('time8:')
        print(schedule[7])
        return True

    interviewee = unassigned[-1] # popped interviewee 이름
    each = availability[n*-1]
    for time in range(8): # 각각 시간대에 대한 가능 여부
        if each[time]==1 and len(schedule[time])<2: 
            unassigned.pop()
            schedule[time].append(interviewee)
            if (solve(unassigned, schedule,n+1)):
                return True
            unassigned.append(interviewee)
            schedule[time].pop()
            
        else:
            continue
            
    return False
    

solve([0,1,2,3,4,5,6,7,8,9,10],[[],[],[],[],[],[],[],[]],1)
