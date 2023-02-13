from random import choice
from pathlib import Path
import button 
import mod 
import pygame as pg


# Initialize pygame
pg.init()

WIDTH, HEIGHT = 800, 900 # x, y
FPS = 60 # Frames Per Second

images_path = fr'{Path(__file__).parents[0]}\images'
font_path = fr'{Path(__file__).parents[0]}\font\HugMeTight.ttf'


class Paint:
    def __init__(self, surface, word):
        self.surface = surface
        self.word = word
        self.colors = button.Button(surface, pg.image.load(f'{images_path}\colors2.png'), 2.9)
        self.invisible_buttons = {'red': 19,
                'blue': 97,
                'green': 175,
                'cyan': 254,
                'magenta': 332,
                'yellow': 410,
                'white': 488,
                'black': 567,
                'erase': 645,
                'finish': 723
                }

    def play(self):
        self.colors.draw(0, 800)
        for color, x in self.invisible_buttons.items():
            if button.Button(self.surface, pg.image.load(f'{images_path}\\blank.png'), 2.87).click(x, 824):
                self.color = self.change_color(color)

    def change_color(self, color):
        if color == 'erase':
            # Recursion
            main(self.word, started=True)
        elif color == 'finish':
            self.finish()

        # return new brush color

    def finish(self):
        # Take a 800, 800 screenshot of the canvas and pick a file location
        quit()


def text_builder(surface, q, size, x, y):
    for mini_q in q.split('||'):
        if len(q.split('||')) > 1:
            y += size
        font = pg.font.Font(font_path, size, bold=True)
        text = font.render(mini_q, True, 'black')
        textRect = text.get_rect()
        textRect.center = (x, y)
        surface.blit(text, textRect)


def main(word=None, started=False):
    if not word:
        word = choice(mod.words)

    # Display a caption in the top left of the program
    pg.display.set_caption("Paint")

    # The program
    surface = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
    
    # Used to set the FPS of the game
    clock = pg.time.Clock()
    paint = Paint(surface, word)

    while True:
        # Setting fps
        clock.tick(FPS)

        # Resetting screen every tick
        surface.fill('white')

        if started:
            paint.play()
        else:
            text_builder(surface, q='Your word is:', size=100, x=400, y=150)
            text_builder(surface, q=word.upper(), size=120, x=400, y=275)
            text_builder(surface, q='Press anything||to start', size=100, x=400, y=550)

        # If user quits then quit
        for event in pg.event.get():
            if event.type==pg.QUIT:
                exit()

            if event.type == pg.KEYDOWN:
                started = True

        pg.display.update()


if __name__ == "__main__":
    main('Microphone')
