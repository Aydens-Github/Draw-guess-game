''' Module and runnable paint game where you can draw on a canvas '''
from random import choice
from pathlib import Path
import button 
import mod 
import pygame as pg
from cv2 import imread, imwrite, imshow


# Initialize pygame
pg.init()

WIDTH, HEIGHT = 800, 900 # x, y
FPS = 1024 # Frames Per Second

images_path = fr'{Path(__file__).parents[0]}\images'
image_path = fr'{images_path}\canvas.png'
font_path = fr'{Path(__file__).parents[0]}\font\HugMeTight.ttf'


class Paint:
    def __init__(self, surface):
        # The screen where everything is drawn
        self.surface = surface

        # Default color is black
        self.color = 'black'

        # Size of cursor
        self.size = 10

        # Canvas is blank
        self.canvas = []

        # Games flag
        self.running = True

        # Used for the buttons
        self.colors = button.Button(surface, pg.image.load(f'{images_path}\colors.png'), 2.9)
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
        # Draw canvas
        [pg.draw.circle(i[0], i[1], i[2], i[3]) for i in self.canvas]

        # The mouse' current position
        pos = pg.mouse.get_pos()
        
        # If the mouse' is not hovering over the menu
        if pos[1] < 800:
            # Draw a circle following the mouse
            pg.draw.circle(self.surface, self.color, pos, self.size)
            # Give the circle a border
            pg.draw.circle(self.surface, 'grey', pos, self.size, 1)
            # If the mouse currently held down i.e. pressed/clicked with the left mouse button i.e. left click
            if pg.mouse.get_pressed()[0]:
                # then append a circles arguments as a tuple inside of the canvas
                self.canvas.append((self.surface, self.color, pos, self.size))

        # Draw the menu 
        self.colors.draw(0, 800)
        # Make the menu clickable
        for color, x in self.invisible_buttons.items():
            # If the menu was clicked
            if button.Button(self.surface, pg.image.load(f'{images_path}\\blank.png'), 2.87).click(x, 824):
                # Change the color of the cursor and check to see if the user has selected to finish
                self.change_color(color)
                    

    def change_color(self, color):
        # If the user picked to erase the canvas
        if color == 'erase':
            # Clear the canvas
            self.canvas = []
            return None
        # If the user has had enough
        elif color == 'finish':
            # Terminate the program
            self.running = False
        # If neither statements above have been hit change the color of the cursor to the color the user picked
        else:
            self.color = color


    def save_canvas(self):
        pg.image.save(self.surface, image_path)
        canvas = imread(image_path)
        canvas = canvas[0:800, 0:800]
        imwrite(image_path, canvas)
        

def text_builder(surface, q, size, x, y):
    # Allow for newlines
    for mini_q in q.split(r'\n'):
        if len(q.split(r'\n')) > 1:
            y += size
        font = pg.font.Font(font_path, size, bold=True)
        text = font.render(mini_q, True, 'black')
        textRect = text.get_rect()
        textRect.center = (x, y)
        surface.blit(text, textRect)


def main(word=None):
    # If this file was ran directly then get a random word from mod.words
    if not word:
        word = choice(mod.words)

    # Display a caption in the top left of the program
    pg.display.set_caption("Paint")

    # The program
    surface = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
    
    # Used to set the FPS of the game
    clock = pg.time.Clock()
    paint = Paint(surface)

    # Has the paint started yet? No it hasn't i.e. False
    started = False
    
    # Should the size of the brush be currently changing? No it shouldn't i.e. None
    change_size = None

    # Main game loop
    while paint.running:
        # If user quits then quit
        for event in pg.event.get():
            if event.type==pg.QUIT:
                paint.running = False

            # User must press any key to start
            if event.type == pg.KEYDOWN:
                started = True

                # If the user is pressing the up arrow
                if event.key == pg.K_UP:
                    # Should the size of the brush be currently changing? Yes it should be getting larger i.e. True
                    change_size = True
                if event.key == pg.K_DOWN:
                    # Should the size of the brush be currently changing? Yes it should be getting smaller i.e. False
                    change_size = False

                color = paint.color

                if event.key == pg.K_r:
                    color = 'red'
                if event.key == pg.K_b:
                    color = 'blue'
                if event.key == pg.K_g:
                    color = 'green'
                if event.key == pg.K_c:
                    color = 'cyan'
                if event.key == pg.K_p:
                    color = 'magenta'
                if event.key == pg.K_y:
                    color = 'yellow'
                if event.key == pg.K_w:
                    color = 'white'
                if event.key == pg.K_k:
                    color = 'black'
                if event.key == pg.K_e:
                    color = 'erase'
                if event.key == pg.K_f:
                    color = 'finish'
                
                paint.change_color(color)
                    
            # If the user is not pressing any keys
            if event.type == pg.KEYUP:
                # Should the size of the brush be currently changing? No it shouldn't i.e. None
                change_size = None
        
        # If the brush should be getting larger
        if change_size == True:
            # then make it larger
            paint.size += 1
        # If it should be getting smaller
        elif change_size == False:
            # Then make it smaller
            paint.size -= 1
        
        # If the size of the brush has reached 1 i.e. the smallest size, stop making it smaller
        if paint.size < 1:
            paint.size = 1
        # If the size of the brush has reached 300 i.e. the largest size, stop making it larger
        elif paint.size > 300:
            paint.size = 300
        
        # Setting fps
        clock.tick(FPS)

        # Resetting screen every tick
        surface.fill('white')

        # If the paint has started,
        if started:
            # paint, if the user has chosen to finish painting
            if paint.play():
                # return an image of the canvas
                paint.running = False
        else:
            # Draw text to a screen explaining what to do
            text_builder(surface, q='Welcome to Paint', size=90, x=405, y=100)
            text_builder(surface, q='Your word is:', size=100, x=410, y=350)
            text_builder(surface, q=word.upper(), size=120, x=400, y=465)
            text_builder(surface, q=r'Press anything\nto start', size=100, x=400, y=600)
        
        # Update the display
        pg.display.update()

    paint.save_canvas()


if __name__ == "__main__":
    main()
