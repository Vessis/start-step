# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 15:21:43 2025
파일내용 : 틱택토 게임
@author: songTaeYang
"""

def scrine(board): #보드판 표시 함수
    for r in range(3):
         print(" " + board[r][0] + " | " + board[r][1] + " | "
               + board[r][2])
         if (r != 2):
             print("---|---|---")

def first(): #선후공 판별 함수. 1=선공 2=후공
    first=int(input("1. 플레이어 선공\n2. com선공\n"))
    
    if first==1:
        return 1
    elif first==2:
        return 2
    else:
        print("다시 입력해주시기 바랍니다.")
        return False
        
def inputxy(board): #플레이어 x,y값 입력함수. xy리스트 리턴
    listxy=[]

    x=int(input("둘 수의 x좌표를 입력해주세요\n"))    
    if x>3:
        print("다시 입력해주시기 바랍니다.(1<=x,y<=3)")
        return False
    listxy.append(x-1)
    
    y=int(input("둘 수의 y좌표를 입력해주세요\n"))
    if y > 3:
        print("다시 입력해주시기 바랍니다.(1<=x,y<=3)")
        return False
    listxy.append(y-1)


    if board[y-1][x-1] != " ":
        print("이미 선택되어있는 위치입니다. 다시 입력해주세요")
        return False
        
    return listxy

def player1Turn(board,xy): #플레이어1 진행함수. board=게임판/xy=x,y값
    board[int(xy[0])][int(xy[1])]="O"
    return board

def player2Turn(board,xy): #플레이어2 진행함수. board=게임판/xy=x,y값
    board[int(xy[0])][int(xy[1])]="X"
    return board

def checkWin(board): #승리판별 함수. board=게임판/부울함수

    if board[0][0]==board[0][1]==board[0][2]!=" " or \
       board[1][0]==board[1][1]==board[1][2]!=" " or \
       board[2][0]==board[2][1]==board[2][2]!=" " or \
       board[0][0]==board[1][0]==board[2][2]!=" " or \
       board[0][1]==board[1][1]==board[2][1]!=" " or \
       board[0][2]==board[1][2]==board[2][2]!=" " or \
       board[0][0]==board[1][1]==board[2][2]!=" " or \
       board[0][2]==board[1][1]==board[2][0]!=" " :
           return True

def computer(board):
    for i in range(3):
        for j in range(2):
            if board[i][j]==board[i][j+1]:
                x=int(i)
                y=3-int(j*2+1)
            elif board[j][i]==board[j+1][i]:
                y=int(i)
                x=3-int(j*2+1)
    if board[x][y]!=" ":
        for i in range(3):
            if " " in board[i]:
                x=i
                y=board[i].index(" ")
    board[x][y]="X"
    return board

def vsComGame(board,i): #vs com 게임함수. board=게임판/i=선공후공판별
    if i==1:
        while True:

            while True:
                xy=inputxy(board)
                if xy != False:
                    break
                
            board=player1Turn(board,xy)
            scrine(board)
            winner=checkWin(board)
            if winner == True:
                print("player의 승리입니다!")
                break
            
            board=computer(board)
            scrine(board)
            winner=checkWin(board)
            if winner == True:
                print("com의 승리입니다:0")
                break
        
    elif i==2:
        while True:
            scrine(board)
            board=computer(board)
            scrine(board)
            winner=checkWin(board)
            if winner == True:
                print("com의 승리입니다:0")
                break
            
            while True:
                xy=inputxy(board)
                if xy != False:
                    break
                
            board=player1Turn(board,xy)
            scrine(board)
            winner=checkWin(board)
            if winner == True:
                print("player의 승리입니다!")
                break
    else :
        print("비정상적인 접근으로 게임을 종료합니다.")

def vsHumanGame(board): #vs hum 게임함수. board=게임판
    while True:
        scrine(board)
        while True:
            xy=inputxy(board)
            if xy != False:
                break
        
        board=player1Turn(board,xy)
        scrine(board)
        winner=checkWin(board)
        if winner == True:
            print("player1의 승리입니다!")
            break
        
        while True:
            xy=inputxy(board)
            if xy != False:
                break
            
        board=player2Turn(board,xy)
        scrine(board)
        winner=checkWin(board)
        if winner == True:
            print("player2의 승리입니다!")
            break
        
def finGame(): #게임 종료함수. 재시작가능
    a=int(input("게임이 종료되었습니다. 다시 시작하려면 1을 입력해주세요.\n"))
    if a==1:
        tickTakToe()
    else:
        print("즐겨주셔서 감사합니다:)")
    return 0

def tickTakToe(): #메인 게임함수
    board= [[' ' for x in range (3)] for y in range(3)]
    startGame=input("Tick! Tack! Toe! :) \nHave nice game\n\
1. vs com \n2. vs human \n3. turn off\n")
    startGame=int(startGame)

    if startGame == 1:
        scrine(board)
        while True:
            f=first()
            if f != False:
                break
        vsComGame(board,f)
        finGame()
        
    elif startGame == 2:
        scrine(board)
        vsHumanGame(board)
        finGame()
        
    elif startGame == 3:
        print("안녕히가세요:)")
        
    else:
        print("--------------------------------")
        print("1부터 3까지의 숫자를 입력해주세요:)")
        tickTakToe()

tickTakToe()