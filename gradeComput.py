# -*- coding: utf-8 -*-
"""
Created on Wed April 15 09:09:54 2025
@author: 2022078019 songTaeYang in chungbuk
메뉴입력 제작

"""

def inp(x):
    return list(map(int, input(x + ": ").split()))

class Computation:
    def grlg(sum_list):
        stgrade = []
        for score in sum_list:
            if score >= 95 * 3:
                stgrade.append("A+")
            elif score >= 90 * 3:
                stgrade.append("A")
            elif score >= 85 * 3:
                stgrade.append("B+")
            elif score >= 80 * 3:
                stgrade.append("B")
            elif score >= 75 * 3:
                stgrade.append("C+")
            elif score >= 70 * 3:
                stgrade.append("C")
            elif score >= 65 * 3:
                stgrade.append("D+")
            elif score >= 60 * 3:
                stgrade.append("D")
            else:
                stgrade.append("F")
        return stgrade

    def arrange(data):
        return sorted(data, key=lambda x: x[5], reverse=True)

    def findName(data, keyword):
        for student in data:
            if keyword in student[1]:
                print(student)
                
    def findUn(data, keyword):
        for student in data:
            if keyword == student[0]:
                print(student)

    def count80(data):
        return sum(1 for student in data if student[6] >= 80)

    def arrlg(sum_list):
        sorted_scores = sorted(set(sum_list), reverse=True)
        return [sorted_scores.index(score) + 1 for score in sum_list]

def inputMain():
    unnum = inp("학번")
    name = input("이름 (공백으로 구분): ").split()
    en = inp("영어")
    c = inp("C-언어")
    py = inp("파이썬")

    sumlg = [x + y + z for x, y, z in zip(en, c, py)]
    avg = [round(s / 3, 2) for s in sumlg]
    grade = Computation.grlg(sumlg)
    rank = Computation.arrlg(sumlg)

    wholeList = []
    for i in range(len(unnum)):
        student = [unnum[i], name[i], en[i], c[i], py[i], sumlg[i], avg[i], grade[i], rank[i]]
        wholeList.append(student)

    wholeList = Computation.arrange(wholeList)

    print("\n=====================================")
    print("학번\t이름\t영어\tC\t파이썬\t총점\t평균\t학점\t등수")
    print("=====================================")
    for student in wholeList:
        print("\t".join(map(str, student)))
    
    return wholeList

# 메인 실행
print("성적관리프로그램에 오신걸 환영합니다.")
print("----------------------------------")
print("학생 정보를 순서대로 입력해주세요")

wholeList = inputMain()

print("\n학번검색은 1번, 이름검색은 2번, 80점 이상 학생 수를 보려면 3번을 입력하세요.")
choice = input("선택: ")

if choice == "1":
    keyword = int(input("검색할 학번 입력: "))
    Computation.findUn(wholeList, keyword)
elif choice == "2":
    keyword = input("검색할 이름 입력: ")
    Computation.findName(wholeList, keyword)
elif choice == "3":
    print("80점 이상 학생 수:", Computation.count80(wholeList))