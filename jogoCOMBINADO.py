import curses
from curses import textpad, window
import math
from math import ceil, sin, cos, tan, floor
import time
from curses.textpad import Textbox, rectangle
import random


#menu 

jogador = []
pontuação = []
oi = 1
while oi<2:
    playerone = input('Digite Jogador 1: ')
    pointsone = input('Digite os pontos de Jogador 1: ')
    playertwo = input('Digite Jogador 2: ')
    pointstwo = input('Digite os pontos de Jogador 2: ')
    jogador.insert(len(jogador), playerone)
    pontuação.insert(len(pontuação), pointsone)
    jogador.insert(len(jogador), playertwo)
    pontuação.insert(len(pontuação), pointstwo)
    oi += 1

opcoes = ['Jogar', 'Ranking', 'Configurações', 'Sair']

def print_opcoes(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(opcoes):
        x = w//2 - len(row)//2
        y = h//2 - len(opcoes)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_center_opcoes(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main_opcoes(stdscr):
    stdscr.keypad(True)
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    current_row = 0

    print_opcoes(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(opcoes)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center_opcoes(stdscr, "Você selecionou {}".format(opcoes[current_row]))
            stdscr.getch()
            if current_row == len(opcoes)-1:
                window.erase()
                curses.endwin()
                exit()
                break
            




            if current_row == len(opcoes)-2:
                #Falta criar as variáveis

                global opcao 
                opcao = ['Fácil', 'Médio', 'Difícil', 'Retornar']
                




                def print_settings(stdscrsettings, selected_row_idx):
                    stdscrsettings.clear()
                    h, w = stdscrsettings.getmaxyx()
                    for idx, row in enumerate(opcao):
                        x = w//2 - len(row)//2
                        y = h//2 - len(opcao)//2 + idx
                        if idx == selected_row_idx:
                            stdscrsettings.attron(curses.color_pair(1))
                            stdscrsettings.addstr(y, x, row)
                            stdscrsettings.attroff(curses.color_pair(1))
                        else:
                            stdscrsettings.addstr(y, x, row)
                    stdscrsettings.refresh()

                def print_center_settings(stdscrsettings, text_settings):
                    stdscrsettings.clear()
                    h, w = stdscrsettings.getmaxyx()
                    x = w//2 - len(text_settings)//2
                    y = h//2
                    stdscrsettings.addstr(y, x, text_settings)
                    stdscrsettings.refresh()


                def main_settings(stdscrsettings):
                    curses.curs_set(0)
                    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
                    current_row_settings = 0

                    print_settings(stdscrsettings, current_row_settings)

                    while 1:
                        key = stdscrsettings.getch()

                        if key == curses.KEY_UP and current_row_settings > 0:
                            current_row_settings -= 1
                        elif key == curses.KEY_DOWN and current_row_settings < len(opcao)-1:
                            current_row_settings += 1
                        elif key == curses.KEY_ENTER or key in [10,13] and current_row_settings == len(opcao)-1:
                            break
                        elif key == curses.KEY_ENTER or key in [10,13] and current_row_settings == len(opcao)-2:
                            print_center_settings(stdscrsettings, "Você selecionou {}".format(opcao[current_row_settings]))
                            stdscrsettings.getch()
                        elif key == curses.KEY_ENTER or key in [10,13] and current_row_settings == len(opcao)-3:
                            print_center_settings(stdscrsettings, "Você selecionou {}".format(opcao[current_row_settings]))
                            stdscrsettings.getch()
                        elif key == curses.KEY_ENTER or key in [10,13] and current_row_settings == len(opcao)-4:
                            print_center_settings(stdscrsettings, "Você selecionou {}".format(opcao[current_row_settings]))
                            stdscrsettings.getch()
                        elif current_row_settings == None :
                            current_row_settings == len(opcao) - 3

                        print_settings(stdscrsettings, current_row_settings)
                curses.wrapper(main_settings)
                curses.wrapper(main_opcoes)




            
            if current_row == len(opcoes)-3:






                


                    
                #Ordenar os jogadores
                junção = zip(pontuação, jogador)


                novajunção = sorted(junção)

                final = [element for _, element in novajunção]

                print(final)

                final.reverse()
                pontuação.sort()

                pontuação.reverse()

                qualquernome = []

                for x, y in zip(final, pontuação):
                    variavel = x + " " + y
                    qualquernome.insert(len(qualquernome), variavel)

                qualquernome.insert(len(qualquernome), "Retornar")




                def print_ranking(stdscr_ranking, selected_row_idx):
                    stdscr_ranking.clear()
                    h, w = stdscr_ranking.getmaxyx()
                    for idx, row in enumerate(qualquernome):
                        x = w//2 - len(row)//2
                        y = h//2 - len(qualquernome)//2 + idx
                        if idx == selected_row_idx:
                            stdscr_ranking.attron(curses.color_pair(1))
                            stdscr_ranking.addstr(y, x, row)
                            stdscr_ranking.attroff(curses.color_pair(1))
                        else:
                            stdscr_ranking.addstr(y, x, row)
                    stdscr_ranking.refresh()

                def print_center_ranking(stdscrsettings, text_settings):
                    stdscrsettings.clear()
                    h, w = stdscrsettings.getmaxyx()
                    x = w//2 - len(text_settings)//2
                    y = h//2
                    stdscrsettings.addstr(y, x, text_settings)
                    stdscrsettings.refresh()


                def main_ranking(stdscr):
                    curses.curs_set(0)
                    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
                    current_row = 0

                    print_ranking(stdscr, current_row)

                    while 1:
                        key = stdscr.getch()

                        if key == curses.KEY_UP and current_row > 0:
                            current_row -= 1
                        elif key == curses.KEY_DOWN and current_row < len(qualquernome)-1:
                            current_row += 1
                        elif key == curses.KEY_ENTER or key in [10, 13]:
                            if current_row == len(qualquernome)-1:
                                break

                        print_ranking(stdscr, current_row)
                curses.wrapper(main_ranking)
                curses.wrapper(main_opcoes)


            

            if current_row == len(opcoes)-4:
                print('oi')
                break





        print_opcoes(stdscr, current_row)
curses.wrapper(main_opcoes)


def main(stdscr):
    curses.curs_set(0)

    t = 1
    k = 1

    sh, sw = stdscr.getmaxyx()
    box = [[3,18], [sh-3, sw-18]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    
    # print_center_opcoes(stdscr, input('Insira o nome do jogador 1 : '))
    # print_center_opcoes(stdscr, input('Insira o nome do jogador 2 : '))

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
    if opcao[1]:
        #predios medianos cada predio tem 9 espaços de largura
        
        alturapredio1 = random.randint((macacoALTURA) - 5 ,(macacoALTURA)+5)
        alturapredio2 = random.randint((macacoALTURA) - 10 ,(macacoALTURA)+5)
        alturapredio3 = random.randint((macacoALTURA) - 5 ,(macacoALTURA)+5)
        #interior
        #predio1
        for y in range(alturapredio1, sh-3):
            for x in range(31, sw-49):
                stdscr.addstr(y,x, 'X')
        #predio2
        for y in range(alturapredio2, sh-3):
            for x in range(31, sw-40):
                stdscr.addstr(y,x, 'X')
        #predio3    
        for y in range(alturapredio3, sh-3):
            for x in range(31, sw-31):
                stdscr.addstr(y,x, 'X')
            
        #exterior dos predios do meio
        #predio1
        for y in range(alturapredio1-1, alturapredio1 -2 ):
            for x in range(31, sw-49):
                stdscr.addstr(y,x, '_')  
        for x in range (sw-50, sw-49):
                stdscr.addstr(y,x, '|')
        #predio2
        for y in range(alturapredio2-1, alturapredio2-2):
            for x in range(31, sw-40):
                stdscr.addstr(y,x, '_')
        for x in range (sw-41, sw-40):
                stdscr.addstr(y,x, '|')
        #predio3
        for y in range (alturapredio3-1, alturapredio3-2):
            for x in range(31, sw-31):
                stdscr.addstr(y,x, '_')
        for x in range (sw-32, sw-33):
                stdscr.addstr(y,x, '|')
    
   #colisao da banana com o predio :
    while banana1[0][0] == (y,x, 'X'):
        stdscr.addstr(y,x,' ')
        break

    
    pontuação = 0
    score_text = "Pontos: {}".format(pontuação)
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

    stdscr.refresh()

    janela3 = curses.newwin(1, 5, 1, 20)
    box4 = Textbox(janela3)

    box4.edit()
    num2 = math.radians(float(box4.gather()))

    stdscr.refresh()

    janela4 = curses.newwin(1, 5, 1, 28)
    box5 = Textbox(janela4)

    box5.edit()
    vel2 = float(box5.gather())

    stdscr.refresh()
    
   
    #A banana anda 108 casas no eixo x.

    while True:
        if t < 6:
            if banana1[0][1] < sw - 18: 
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
                pontuação += 100
                score_text = "Pontuação: {}".format(pontuação)
            
            #if banana1 == predio[1] or ...:
                #...
            
            if (banana1 in [box[0][0], box[1][0]] or banana1 in [box[0][1], box[1][1]]):
                for y,x in banana1:
                    stdscr.addstr(y,x, 'O')
            
            stdscr.refresh()

        if t >= 6 and k < 6:
            banana1 =  [[macaco[0][0] - 1,macaco[0][1]]]
            for y,x in banana1:
                stdscr.addstr(y,x, 'O')

            new_banana2 = [banana2[0][0] - floor(vel2*sin(num2)*k) + 2*k*k +2, banana2[0][1] - floor(vel2*cos(num2)) - 1]
            k += 1
            time.sleep(0.325)

            if new_banana2[1] < 2 or new_banana2[0] < 3 or new_banana2[0] > sw - 3:
                break

            stdscr.addstr(new_banana2[0], new_banana2[1], 'O')
            
            banana2.insert(0, new_banana2)

            stdscr.addstr(banana2[-1][0], banana2[-1][1], ' ')
            banana2.pop()
            
            #if banana2 == predio[1] or ...:
            #...
            
            if (banana2 in [box[0][0], box[1][0]] or banana2 in [box[0][1], box[1][1]]):
                for y,x in banana2:
                    stdscr.addstr(y,x, 'O')

            stdscr.refresh()

    stdscr.getch()

curses.wrapper(main)