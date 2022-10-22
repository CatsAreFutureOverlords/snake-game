import pygame
import random
import rgbcolours

class fruit:
    def __init__(self, screen, colour):
        self._screen = screen
        self._colour = colour
        (w, h) = screen.get_size()
        self._dimension = (w/16, h/16)
        self._x = random.randrange(0, w, w/16)
        self._y = random.randrange(0, h, h/16)
        self._avatar = pygame.Rect((self._x, self._y), self._dimension)

    def draw(self):
        pygame.draw.rect(self._screen, self._colour, self._avatar)

    def newLocation(self):
        self._x = random.randrange(0, 720, 45)
        self._y = random.randrange(0, 720, 45)
        self._avatar = pygame.Rect((self._x, self._y), self._dimension)

    def comparison(self):
        return self._avatar
        