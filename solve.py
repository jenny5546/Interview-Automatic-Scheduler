import availability # availability.py
import namelist # namelist.py
import printer # printer.py

availMat = availability.availability()

def main():
    unassigned = namelist.attendance()
    schedule = [[] for x in range(13)]
    solve(unassigned,schedule,124)


def solve(unassigned,schedule,person):
    # 필요한 변수들 
    global availMat
    full = True
    checked = [i for i,e in enumerate(availMat[person]) if e==1]
    
    for t in checked:
        if len(schedule[t])<12:
            full = False

    
    # 실패하는 경우: 만약 unassigned > 0, 그 사람이 들어갈 자리가 없을 때, 
    if len(unassigned)>0 and full:
        return False

    # 성공 기저 사례: 더 이상 assign 할 사람이 없다
    if len(unassigned)==0:
        printer.printer(schedule)
        return True

    for time in checked:
        interviewee = unassigned[-1] 
        print(interviewee)
        if len(schedule[time])<12:
            schedule[time].append(interviewee)
            newS = schedule
            unassigned.pop()
            newU = unassigned
            if (solve(newU, newS, person-1)==True):
                schedule[time].append(interviewee)
                unassigned.pop()
                # print(schedule)
                return True
            
            else:
                continue



    return False


if __name__ == "__main__":
	main()

# graph 처럼 dirty한걸 표현해야할듯.