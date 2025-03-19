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
       
def main():
    unnum = inp("학번")
    name = inp("이름")
    en = inp("영어")
    c = inp("C-언어")
    py = inp("파이썬")
    
    sm = sumlg(en,c,py)
    grade = grlg(sm)
    sup=arrlg(sm)
    print("=====================================")
    print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")    
    print("=====================================")

    for i in range(len(unnum)):
        print(unnum[i],name[i],en[i],c[i],py[i],sm[i],round(avlg(sm[i],3),2),grade[i],sup[i])

main()
