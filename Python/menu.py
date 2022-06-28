import main, pygame

pygame.init()

"""

    ---  FILE DEL MENU PRINCIPALE DELl'AVVIO DEL GIOCO	---

"""


def get_font(size):
    return pygame.font.Font("font/font.ttf", size)

def play():
    main.inizializza()
    main.main()
    
play()