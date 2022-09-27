import time
import curses
screen = curses.initscr()
curses.start_color()


menu = ['Home', 'Ranking', 'Opções', 'Sair']




#getmaxyx é uma função que pega o tamanho maximo da tela
tamanhoDaTela, larguraDaTela = screen.getmaxyx()

#paleta de cores 1
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
text = "olá mundo"
#função pra botar os textos no meio da tela


def logo(screen) :
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    text = "Gorilaz!"
    x = larguraDaTela//2 - len(text)//2
    y = tamanhoDaTela//2 
   
    
    screen.attron(curses.color_pair(1))

    screen.addstr(y, x, text)
    screen.attroff(curses.color_pair(1))
    
    screen.refresh()
    time.sleep(3)
curses.wrapper(logo)

def printMenu(screen, selected_row_idx):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

    

    screen.clear()
    for idx, row in enumerate(menu):
        x = larguraDaTela//2 - len(row)//2
        y = tamanhoDaTela//2  - len(menu)//2 + idx
        selected_row_idx  = idx 

        if idx == selected_row_idx:
            screen.attron(curses.color_pair(1))
            screen.addstr(y, x, row)
            screen.attroff(curses.color_pair(1))
        else:
            screen.addstr(y,x, row)
    screen.refresh()
curses.wrapper(printMenu)

def main(screen) :
    #paleta de cores
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

    curses.init_pair(1)

    current_row = 0
    printMenu(screen, current_row)

    while 1 :
        tecla = screen.getch()
        if tecla == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif tecla  == curses.KEY_DOWN and current_row < len(menu) -1 :
            current_row += 1
        elif tecla == curses.KEY_ENTER :
            print_meio(f'Selecionado : {format(menu[current_row])}')
            screen.addstr(y, x, {format(menu[current_row])})
curses.wrapper(main)



curses.endwin() 
