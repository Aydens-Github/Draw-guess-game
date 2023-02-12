from random import choice
from pathlib import Path
import button 
import mod 
import pygame as pg


pg.init()

WIDTH, HEIGHT = 1000, 1000 # x, y
FPS = 60 # Frames Per Second
COLOR = (100, 100, 100) # RGB
BLACK = (0, 0, 0) # RGB
images_path = fr'{Path(__file__).parents[0]}\images'
# image_path = fr'{images_path}\drawing.png'

font_path = fr'{Path(__file__).parents[0]}\font\HugMeTight.ttf'


class Paint:
    def __init__(self, surface, word):
        self.surface = surface
        self.word = word

    def play(self):
        # if finish:
        #     return True
        return False

    def get_image(self):
        return 1

        
def main(word=None):
    if not word:
        word = choice(mod.words)

    # Display a caption in the top left of the program
    pg.display.set_caption("Paint")

    # The program
    surface = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
    
    # Used to set the FPS of the game
    clock = pg.time.Clock()
    paint = Paint(surface, word)

    start_button = button.Button(surface, pg.image.load(f'{images_path}\start.png'), 4  )
    start = False
    
    font1 = pg.font.Font(font_path, 160, bold=True)
    text = font1.render(word.upper(), True, BLACK)
    textRect = text.get_rect()
    textRect.center = (500, 400)

    font2 = pg.font.Font(font_path, 150, bold=True)
    text2 = font2.render('Your word is: ', True, BLACK)
    textRect2 = text2.get_rect()
    textRect2.center = (520, 200)

    while True:
        # If user quits then quit
        for event in pg.event.get():
            if event.type==pg.QUIT:
                exit()

        # Setting fps
        clock.tick(FPS)

        # Resetting screen every tick
        surface.fill(COLOR)

        if start or start_button.click(30, 550):
            start = True
            if paint.play():
                break
        else:
            surface.blit(text, textRect)
            surface.blit(text2, textRect2)

        pg.display.update()
        
    return paint.get_image()


if __name__ == "__main__":
    main('Restaurant')
