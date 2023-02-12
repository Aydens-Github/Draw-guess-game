""" Helper class that handles buttons"""
import pygame as pg


# Initializing pygame
pg.init()


class Button():
    def __init__(self, surface, img, size):
        # Getting the image width and height
        width, height = img.get_width(), img.get_height()

        # Scaling the image width and height based on the size parameter
        self.img = pg.transform.scale(img, (int(width * size), int(height * size)))

        # Creating button base
        self.rect = self.img.get_rect()

        # The surface to draw the button
        self.surface = surface

    # Returns True if the button is clicked, False otherwise
    def click(self, x, y):
        # draw button
        self.draw(x, y)

        # Change clicked if the button is clicked, the default is False
        self.clicked = False

        # The mouse position
        pos = pg.mouse.get_pos()

        # Moving the button to correct position
        self.rect.topleft = (x, y)

        # If the mouse is pressed
        if pg.mouse.get_pressed()[0] == 1:
            # if the mouse is hovering over the button
            if self.rect.collidepoint(pos):
                # change clicked to True because the button was clicked
                self.clicked = True

        # Return if the button was clicked
        return self.clicked

    def draw(self, x, y):
        # Moving the button to correct position
        self.rect.topleft = (x, y)
        # Drawing the button to the screen
        self.surface.blit(self.img, (self.rect.x, self.rect.y))
