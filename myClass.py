'''
myClass.py
2018/02/02
by daltago87
'''

class Rectangle:

    count = 0 # 클래스 변수

    #초기자
    def __init__(self, width, height):
         # self.* : 인스턴스변수
        self.width = width
        self.height = height
        Rectangle.count =+1 
    
    #메서드
    def calcArea(self):
        area = self.width * self.height
        return area
    
    
