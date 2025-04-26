# подключаем модули
import pygame
from random import *
import time

# подключаем pygame
pygame.init()

# цвета
red = (255 ,0 ,0)
blue =(15,0,255)
yellow = (251,237,149)
green = (88,221,149)
dark_blue = (0,0,145)
black = (0,0,0)
light_red =(255,0,0)
light_green = (0,255,0)

# заливка экрана
mw = pygame.display.set_mode((500 , 500))# в программе создается дисплей
mw.fill(green)#заливка зеленом цветом
clock = pygame.time.Clock()# в программе создается таймер

#создаём класс area .цвет, заливка, рамки
class Area():
    # карточка
    def __init__(self, x=0, y=0, width=10, height=10, color=None):# создание свойств
        self.rect = pygame.Rect(x, y, width, height )
        self.fill_color = color


    # цвет карточки ,
    def color(self, new_color):
        self.fill_color = new_color


    #заливка карточки
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)


    # рамки карточки
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def collidepoint(self , x,y):# возвращяет кординаты ,попали курсором по карточке = True or false
        return self.rect.collidepoint(x,y)





# класс наследник
class Label(Area):
    def set_text(self,text,fsize = 12 ,text_color= (0,0,0)):# какой текст (шрифт,какой цвет)
        self.image = pygame.font.SysFont('vedrana' ,fsize).render(text,True,text_color)

    # место где будет написоно слово
    def draw(self , shift_x = 0 , shift_y = 0):
        self.fill()
        mw.blit(self.image , (self.rect.x  + shift_x,  self.rect.y + shift_y))





# список карточек
cards = []

# количиство карточек
num_curds = 4

x=70

# создание карточек
for i in range(num_curds):
    new_card = Label(x,170 , 70, 100 , yellow)# запаминаем карточку

    new_card.fill()#рисуем карточку
    new_card.outline(blue,5)#рисуем рамки карточке

    # надпись на карточки
    new_card.set_text('CLICK' , 26 , red)#пишем надпись click на карточке
    cards.append(new_card)# добовляем карту в список
    x += 100# смещяем карточку


start_time = time.time()
cur_time = start_time

text2 = Label(350,15 , 50 ,50 ,green)
text2.set_text('Счет:',30 , dark_blue)
text2.draw(15,15)

time_text = Label(15,15,50,50,green)# место , длина,ширина,цвет
time_text.set_text('Время:',30 , dark_blue)
time_text.draw(15,15)

timer = Label(50,55,50,40,green)# место , длина,ширина,цвет
text1 = Label(400,55 ,50,40,green)




points = 0

wait = 0 # скорость смены карточки

# бесконечный цикл чтоб надпись прыгала, и чтоб принажатие с click карточка окрашивалась в зеленый цвет  иначе в красный цвет
while True:# цикол чтоб
    if wait == 0:
        wait=20# скорость смены карточек
        click = randint(1,num_curds)# рандомные карточки из списска


        for i in range(num_curds): # повторение 4 раза ,генерация Click на раднонмый картокчи
            cards[i].color(yellow)#карточка закрашивается в желтый
            if (i+1) == click:# рандомная карточка
                cards[i].draw(10,40) # пишится надпись Сдшсл
            else:
                cards[i].fill()# другие карточки закрашиваются

    else:
        wait-=1


    new_time = time.time()

    if new_time - cur_time >=1:
        timer.set_text(str(int(new_time - start_time)) , 40 , dark_blue)
        timer.draw(0,0)
        cur_time = new_time

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos

            for i in range(num_curds):
                if cards[i].collidepoint(x,y):
                    if i +1 == click:
                        cards[i].color(green)
                        points +=1

                    # заливка карточки
                    else:
                        cards[i].color(red)
                        points -=1
                    cards[i].fill()

        text1.set_text(str(int(points)) , 40 , dark_blue)
        text1.draw(0,0)
    if new_time - start_time >= 11:
        break
    if points >= 5:
        break

    pygame.display.update()
    clock.tick(40)




if new_time- start_time >= 11:
    win = Label(0,0,500,500, light_red)
    win.set_text('Время вышло!!!' , 60, dark_blue)
    win.draw(110,180)


if points >= 5:
    win= Label(0,0,500,500,light_green)
    win.set_text('Ты победил!!!' , 60 ,dark_blue)
    win.draw(140,180)

    result_time = Label(90, 230,250,250,light_green)
    result_time.set_text('Время прохождения:'+ str(int(new_time - start_time))  + 'сек' , 40 , dark_blue)
    result_time.draw(0,0)



pygame.display.update()
clock.tick(40)

