#!/usr/bin/env python
# coding: utf-8

# In[8]:



class Square:
    def __init__(self):
        self.square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형 2.평행사변형 3.사다리꼴 \n >>>'))

        if self.square == 1:
            print('직사각형 함수는 rect()입니다.')

        elif self.square == 2:
            print('평행사변형 함수는 par()입니다.')
        
        elif self.square == 3:
            print('사다리꼴 함수는 trape()입니다.')
        
        else:
            print('1, 2, 3 중에서 다시 입력해주세요')

    def rect(self):
        #width, vertical = map(int, input('가로, 세로를 입력하세요. 예시 : 가로,세로\n >>>').split(','))
        width = int(input('가로 길이를 입력하세요 >>> '))
        vertical = int(input('세로 길이를 입력하세요 >>> '))
        area = width * vertical
        result = '직사각형의 넓이는 : ' + str(area)
        return result

    def par(self):
        #bottom, height = map(int,input('밑변, 높이를 입력하세요. 예시 : 밑변,높이\n >>>').split(','))
        bottom = int(input('밑변의 길이를 입력하세요 >>> '))
        height = int(input('높이의 길이를 입력하세요 >>> '))
        area = bottom*height #평행사변형 넓이
        result = '평행사변형의 넓이는 : ' + str(area)
        return result

    def trape(self):
        #bottom, top, height = map(int,input('밑변, 윗변, 높이를 입력하세요. 예시 : 밑변,윗변,높이\n >>>').split(','))
        bottom = int(input('밑변의 길이를 입력하세요 >>> '))
        top = int(input('윗변의 길이를 입력하세요 >>> '))
        height = int(input('높이의 길이를 입력하세요 >>> '))
        area = (bottom+top)*height/2 #사다리꼴 넓이
        result = '사다리꼴의 넓이는 : ' + str(area)
        return result

a = Square()  # 객체 생성 & 2, 3을 각각 입력해 봅시다.


# In[9]:


a.rect()


# In[ ]:




