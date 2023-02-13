''' Module and runnable paint game where you can draw on a canvas '''
from random import choice
from pathlib import Path
import button 
import mod 
import pygame as pg


# Initialize pygame
pg.init()

WIDTH, HEIGHT = 800, 900 # x, y
FPS = 120 # Frames Per Second

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

        self.reset()

    def play(self, mouse_state):
        self.colors.draw(0, 800)
        for color, x in self.invisible_buttons.items():
            if button.Button(self.surface, pg.image.load(f'{images_path}\\blank.png'), 2.87).click(x, 824):
                self.change_color(color)

        pos = pg.mouse.get_pos()
        if pos[1] < 800:
            pg.draw.circle(self.surface, self.color, pos, self.size)
            if pg.mouse.get_pressed()[0]:
                self.canvas.append((self.color, pos, self.size))

        self.draw_canvas()

    def change_color(self, color):
        self.color = color
        if color == 'erase':
            self.reset()
        elif color == 'finish':
            self.finish()

    def draw_canvas(self):
        for i in self.canvas:
            pg.draw.circle(self.surface, i[0], i[1], i[2])

    def finish(self):
        # Take a 800, 800 screenshot of the canvas and pick a file location
        quit()

    def reset(self):
        self.color = 'black'
        self.size = 10
        self.canvas = []
        
def text_builder(surface, q, size, x, y):
    for mini_q in q.split('||'):
        if len(q.split('||')) > 1:
            y += size
        font = pg.font.Font(font_path, size, bold=True)
        text = font.render(mini_q, True, 'black')
        textRect = text.get_rect()
        textRect.center = (x, y)
        surface.blit(text, textRect)


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

    started = False

    while True:
        # If user quits then quit
        for event in pg.event.get():
            if event.type==pg.QUIT:
                exit()

            if event.type == pg.KEYDOWN:
                started = True

        # Setting fps
        clock.tick(FPS)

        # Resetting screen every tick
        surface.fill('white')

        if started:
            paint.play(event.type)
        else:
            text_builder(surface, q='Your word is:', size=100, x=400, y=150)
            text_builder(surface, q=word.upper(), size=120, x=400, y=275)
            text_builder(surface, q='Press anything||to start', size=100, x=400, y=550)

        pg.display.update()


if __name__ == "__main__":
    main()
