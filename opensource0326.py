# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 09:09:54 2025
@author: 2022078019 songTaeYang in chungbuk
메뉴입력 제작

"""
#입력
def inp(x):
    a = list(map(int,input(x+":").split()))
    return a

#총점
def sumlg(listx,listy,listz):
    sumlg = [x + y + z for x, y, z in zip(listx,listy,listz)]
    a=list(map(int,sumlg))
    return a

#평균
def avlg(listx,y):
    return float(listx/y)

#학점계산
def grlg(listlg):
    stgrade=list()
    for n in range(len(listlg)):
        if listlg[n] >= 95*3:
            stgrade.append("A+")
        elif listlg[n] >= 90*3:
            stgrade.append("A")
        elif listlg[n] >= 85*3:
            stgrade.append("B+")
        elif listlg[n] >= 80*3:
            stgrade.append("B")
        elif listlg[n] >= 75*3:
            stgrade.append("C+")
        elif listlg[n] >= 70*3:
            stgrade.append("C")
        elif listlg[n] >= 65*3:
            stgrade.append("D+")
        elif listlg[n] >= 60*3:
            stgrade.append("D")
        else:
            stgrade.append("F")
    return stgrade

#총점기준 정렬
def arrange(wholeList):
    wholeList.sort(key=lambda x:x[5])
    return wholeList

#이름검색
def findName(wholeList):
    for i in range(len(wholeList)):
        if str(input()) in wholeList[i]:
            print(wholeList[i])
    return 0

#학번검색
def findUn(wholeList):
    for i in range(len(wholeList)):
        if int(input()) in wholeList[i]:
            print(wholeList[i])
    return 0

#80점이상 학생 수수
def count80(wholeList):
    count = 0
    for i in range(len(wholeList)):
        if wholeList[i][6] >= 80:
            count =+ 1
    return count
#등수계산
def arrlg(listlg):
    x = list(listlg)
    dic = dict()
    for num in range(len(x)):
        a=max(x)
        orderLg = x.index(a)
        dic[orderLg] = num+1
        x[orderLg] = 0
    return dic
       
def inputMain():
    unnum = inp("학번")
    name = inp("이름")
    en = inp("영어")
    c = inp("C-언어")
    py = inp("파이썬")
    
    sm = sumlg(en,c,py)
    grade = grlg(sm)
    sup=arrlg(sm)
    wholeList=[]
    for i in range(len(unnum)):
        a=list(unnum[i],name[i],en[i],c[i],py[i],sm[i],round(avlg(sm[i],3),2),grade[i],sup[i])
        wholeList.append(a)

    wholeList = arrange(wholeList)
    print("=====================================")
    print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")    
    print("=====================================")

    for i in range(len(unnum)):
        print(wholeList[i],name[i],en[i],c[i],py[i],sm[i],round(avlg(sm[i],3),2),grade[i],sup[i])
    
    return wholeList

print("성적관리프로그램에 오신걸 환영합니다.")
print("----------------------------------")
print("학생 정보를 순서대로 입력해주세요")
wholeList = inputMain()
print("학번검색은 1번, 이름검색은 2번, 80점이상\n 학생 수를 아시려면 3번을 눌러주세요.")
if int(input())=="1":
    findUn(wholeList)
elif int(input())=="2":
    findName(wholeList)
elif int(input())=="3":
    count80(wholeList)