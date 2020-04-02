import availability # availability.py
import namelist # namelist.py
import printer # printer.py

def main():
    unassigned = namelist.attendance()
    schedule = [[] for x in range(13)]
    
    solve(unassigned,schedule,1)


def solve(unassigned,schedule,n):

    availMat = availability.availability()
    # 성공 기저 사례: unassigned가 한명도 없을 때
    if len(unassigned)==0:
        printer.printer(schedule)
        return True

    interviewee = unassigned[-1] # popped interviewee 이름
    print(interviewee)
    each = availMat[n*-1]
    for time in range(13): # 각각 시간대에 대한 가능 여부
        if each[time]==1 and len(schedule[time])<20: # 한 타임 당 두명만 볼 수 있다는 가정
            
            unassigned.pop()
            schedule[time].append(interviewee)
            if (solve(unassigned, schedule,n+1)):
                return True
            unassigned.append(interviewee)
            schedule[time].pop()
        else:
            continue
            
    return False
    


if __name__ == "__main__":
	main()