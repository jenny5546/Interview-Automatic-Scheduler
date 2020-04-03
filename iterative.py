import availability # availability.py
import namelist # namelist.py
import printer # printer.py

availMat = availability.availability()
visited = [[] for x in range(125)]
unassigned = namelist.attendance()
schedule = [[] for x in range(13)]

def solve():

    num = 124
    while True:

        if len(unassigned) == 0:
            printer.printer(schedule)
            return True

        interviewee = unassigned.pop()
        available = [i for i,e in enumerate(availMat[num]) if e==1]
        full = True

        for t in checked:
            if len(schedule[t])<12:
                full = False

        if len(unassigned)>0 and full:
            print('full')
            return False

        

        num-=1



if __name__ == "__main__":
	solve()