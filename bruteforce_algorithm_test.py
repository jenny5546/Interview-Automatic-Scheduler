"""

시간대 x 사람 의 2 by 2 array, 가능하면 1 불가능하면 0을 담고 있음. 
아직 배정이 안된 사람의 list [], 배정이 되면 list에서 pop()
그 시간대마다 배정된 사람의 list [], 배정이되면 list에 append 해주기

만약 list가 다 찼고,(max 6) 그 시간대만 되는 사람이 있으면, 실패.
unassigned가 비어있으면 성공.

        1시 2시 3시 4시 5시 6시 7시 8시
-------------------------------------- 
ann     0   0   1  1  0   1  1   1
berry   0   0   0  0  0   1  1   1
cally   0   0   0  0  0   0  1   1
jenny   0   1   0  0  0   0  0   0
lulu    1   0   1  1  0   1  1   1
tom     1   0   1  1  0   1  1   1

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
