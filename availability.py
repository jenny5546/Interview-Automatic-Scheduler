import pandas as pd
from pandas import ExcelFile

def switch(value):

    # 시간대 별 column 번호를 간단한 switch 문으로 구현
    """
    [column 0] 21 (토) 1시 ~ 2시, 
    [column 1] 21 (토) 2시 ~ 3시, 
    [column 2] 21 (토) 3시 ~ 4시, 
    [column 3] 21 (토) 4시 ~ 5시, 
    [column 4] 21 (토) 5시 ~ 6시, 
    [column 5] 22 (일) 1시 ~ 2시, 
    [column 6] 22 (일) 2시 ~ 3시, 
    [column 7] 22 (일) 3시 ~ 4시, 
    [column 8] 22 (일) 4시 ~ 5시, 
    [column 9] 22 (일) 5시 ~ 6시, 
    [column 10] 23 (월) 6시 ~ 7시, 
    [column 11] 23 (월) 7시 ~ 8시, 
    [column 12] 23 (월) 8시 ~ 9시
    """

    columnNum = {
        '21 (토) 1시 ~ 2시': 0,
        ' 21 (토) 2시 ~ 3시': 1,
        ' 21 (토) 3시 ~ 4시': 2,
        ' 21 (토) 4시 ~ 5시': 3,
        ' 21 (토) 5시 ~ 6시': 4,
        ' 22 (일) 1시 ~ 2시': 5,
        ' 22 (일) 2시 ~ 3시': 6,
        ' 22 (일) 3시 ~ 4시': 7,
        ' 22 (일) 4시 ~ 5시': 8,
        ' 22 (일) 5시 ~ 6시': 9,
        ' 23 (월) 6시 ~ 7시': 10,
        ' 23 (월) 7시 ~ 8시': 11,
        ' 23 (월) 8시 ~ 9시': 12
    }.get(value,-1)

    return columnNum

def availability():

    """
    지원자 별로 13가지의 시간대의 가능여부를 담은 125(명) x 13(시간) list를 반환   
    """
    df = pd.read_excel(r'availability_file.xlsx')
    availMatrix = [[0]*13 for x in range(125)] # 125 x 13 matrix
    rowNum = 0
    for index,row in df.iterrows():
        timeList = row[2].split(',') # 한 사람의 가능한 시간대를 담은 List
        for time in timeList:
            column = switch(time)
            availMatrix[rowNum][column]=1
        rowNum+=1
    
    return availMatrix
            

if __name__ == "__main__":
	availability()