import pygame
import rgbcolours

class SnakeBody:
    def __init__(self, screen):
        self._screen = screen
        (w, h) = screen.get_size()
        self._score = 0
        self._movement = 'right'
        self._dimension = (w/16, h/16)
        self._avatar = pygame.Rect((w/8, 0), self._dimension)
        self._tail = [pygame.Rect((w/16, 0), self._dimension), pygame.Rect((0, 0), self._dimension)]
    
    def grow(self):
        self.addPoints()
        self.move(self._movement)

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('right arrow key pressed!')
                self._movement = 'right'
                self.move(self._movement)
                self._tail.pop()
            elif event.key == pygame.K_LEFT:
                print('left arrow key pressed!')
                self._movement = 'left'
                self.move(self._movement)
                self._tail.pop()
            elif event.key == pygame.K_UP:
                print('up arrow key pressed!')
                self._movement = 'up'
                self.move(self._movement)
                self._tail.pop()
            elif event.key == pygame.K_DOWN:
                print('down arrow key pressed!')
                self._movement = 'down'
                self.move(self._movement)
                self._tail.pop()

    def move(self, direction):
        if direction == 'left':
            self._tail.insert(0, self._avatar)    
            self._avatar = self._avatar.move((-self._dimension[0], 0))
        elif direction == 'right':
            self._tail.insert(0, self._avatar)
            self._avatar = self._avatar.move((self._dimension[0], 0))
        elif direction == 'up':
            self._tail.insert(0, self._avatar)
            self._avatar = self._avatar.move((0, -self._dimension[0]))
        elif direction == 'down':
            self._tail.insert(0, self._avatar)
            self._avatar = self._avatar.move((0, self._dimension[0]))

    def draw(self):
        pygame.draw.rect(self._screen, rgbcolours.green, self._avatar)
        for body in self._tail:
            pygame.draw.rect(self._screen, rgbcolours.limegreen, body)

    def getScore(self):
        return self._score

    def addPoints(self):
        self._score += 1