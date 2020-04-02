import pandas as pd
from pandas import ExcelFile


def attendance():

    """

    전체 사람들의 명단을 하나의 list로 저장해두기 위해서 만든 method
    엑셀 파일을 읽어와서 {지원서id}+{이름} 의 string 형식으로 저장하고, 전체 사람의 list 반환

    """
    intervieweeList = []
    df = pd.read_excel(r'availability_file.xlsx')

    for index,row in df.iterrows():
        nameId = ''
        nameId += str(row[0])
        nameId += str(row[1])
        intervieweeList.append(nameId) 

    return intervieweeList


if __name__ == "__main__":
	attendance()