import curses
from curses import textpad
import math
from math import ceil, sin, cos, tan, floor
import time
from curses.textpad import Textbox, rectangle
import random

def main(stdscr):
    curses.curs_set(0)

    t = 1

    sh, sw = stdscr.getmaxyx()
    box = [[3,18], [sh-3, sw-18]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    

    #o macaco ta sendo gerado mto perto do fim do prédio, seria bom depois a gente mudar o x dele


    macacoALTURA = random.randint(sh//2-5, sh//2+6)
    #macaco = [[sh//2+1, 30],[sh//2+1, sw-30]]
    macaco = [[macacoALTURA, 24],[macacoALTURA, sw-24]]
    banana1 =  [[macaco[0][0] - 1,macaco[0][1]]]
    banana2 =  [[macaco[1][0] - 1, macaco[1][1]]]
    
    for y,x in macaco:
        stdscr.addstr(y,x, '*')

    for y,x in banana1:
        stdscr.addstr(y,x, 'O')

    for y,x in banana2:
        stdscr.addstr(y,x, 'O')

    #predio
    #predio inicial 1
    #def predioINTERIOR(): 
        for y in range(macacoALTURA+ 3, sh-3):
            for x in range(19, 30):
                stdscr.addstr(y,x, 'P') 
            for x in range(30,32) :
                stdscr.addstr(y,x, '|')
            
    #def predioEXTERIOR():
        for y in range(macacoALTURA+ 1, macacoALTURA+ 2):
            for x in range(19, 30):
                stdscr.addstr(y,x, '_')
        for y in range(macacoALTURA+2, sh-3) :
            for x in range(30,32) :
                stdscr.addstr(y,x, '|')
            

    #predio inicial 2
    #predioINTERIOR()
    for y in range(macacoALTURA + 3, sh-3 ):
        for x in range( sw-31,sw-19):
            stdscr.addstr(y,x, 'P')
    #predioEXTERIOR
    for y in range(macacoALTURA+ 1, macacoALTURA+ 2):
        for x in range( sw-30,sw-19):
          stdscr.addstr(y,x, '_')  
    for y in range(macacoALTURA+2, sh-3) :
            for x in range(sw-31,sw-30) :
                stdscr.addstr(y,x, '|')

    #predios medianos
    alturapredio1 = random.randint((macacoALTURA) - 10 ,(macacoALTURA))

    for y in range(alturapredio1, sh-3):
        for x in range(31, sw-31):
            stdscr.addstr(y,x, 'X')
    
    score = 0
    score_text = "Pontos: {}".format(score)
    stdscr.addstr(1, sw//2 - len(score_text)//2, score_text)

    rectangle(stdscr, 0, 18, 2,25)
    janela = curses.newwin(1, 5, 1,20)
    box2 = Textbox(janela)
    
    stdscr.refresh()
    
    box2.edit()
    num = math.radians(float(box2.gather()))

    rectangle(stdscr, 0, 27, 2, 34)
    janela2 = curses.newwin(1, 5, 1, 28)
    box3 = Textbox(janela2)

    stdscr.refresh()

    box3.edit()
    vel = float(box3.gather())

    #A banana anda 86 casas no eixo x.

    while 1:

        if banana1[0][1] < sw - 3: 
            new_banana1 = [banana1[0][0] - floor(vel*sin(num)*t) + 2*t*t + 2, banana1[0][1] + floor(vel*cos(num)) + 1]
            t += 1
            time.sleep(0.325)

        if new_banana1[0] > 4:
            stdscr.addstr(new_banana1[0], new_banana1[1], 'O')
        
        banana1.insert(0, new_banana1)

        if new_banana1[0] > 4:
            stdscr.addstr(banana1[-1][0], banana1[-1][1], ' ')
            banana1.pop()

        if banana1 == macaco[1] or banana1 == banana2:
            score += 100
            score_text = "Pontuação: {}".format(score)
        
        #if banana1 == predio[1] or ...:
            #...
        
        if (banana1 in [box[0][0], box[1][0]] or banana1 in [box[0][1], box[1][1]]):
            for y,x in banana1:
                stdscr.addstr(y,x, 'O')

        stdscr.refresh()

    stdscr.getch()

curses.wrapper(main)