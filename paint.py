from random import choice
from pathlib import Path
import button 
import mod 
import pygame as pg


pg.init()

WIDTH, HEIGHT = 1000, 1000 # x, y
FPS = 10 # Frames Per Second
COLOR = (0, 0, 0) # Black

images_path = fr'{Path(__file__).parents[0]}\images'
image_path = fr'{images_path}\drawing.png'


class Paint:
    def __init__(self, surface, word):
        if word:
            self.word = word
        else:
            self.word = choice(mod.words)
        self.surface = surface

    def play(self):
        # if finish:
        #     return True
        return False

    def get_image(self):
        return 1

        
def main(word=None):
    # Display a caption in the top left of the program
    pg.display.set_caption("Paint")

    # The program
    surface = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
    
    # Used to set the FPS of the game
    clock = pg.time.Clock()
    paint = Paint(surface, word)

    start_button = button.Button(surface, pg.image.load(f'{images_path}\start.png'), 1)
    start = False

    while True:
        print('ur mom')
        # If user quits then quit
        for event in pg.event.get():
            if event.type==pg.QUIT:
                exit()

        # Setting fps
        clock.tick(FPS)

        # Resetting screen every tick
        surface.fill(COLOR)

        if start or start_button.click(0, 0):
            start = True
            if paint.play():
                break
        # else:

        pg.display.update()
        
    return paint.get_image()


if __name__ == "__main__":
    main()
