#!/usr/bin/env python

import pygame
import rgbcolours

class default_scene:
    def __init__(self, screen):
        self._state = 0
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(rgbcolours.misty_rose)
        self._is_valid = True
    
    def draw(self):
        self._screen.blit(self._background, (0, 0))
    
    def process_event(self, event):
        print(str(event))
        if event.type == pygame.QUIT:
            print('Good Bye!')
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print('Bye bye!')
            self._is_valid = False

    def is_valid(self):
        return self._is_valid
    
    def update(self):
        pass

    def getNextState(self):
        return self._state


class TitleScene(default_scene):
    def __init__(self, screen, title, title_color, title_size):
        super().__init__(screen)
        self._state = 2
        self._background.fill(rgbcolours.turquoise)
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, title_color)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any key.', True, rgbcolours.black)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(w/2, h/2))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w/2, h - 50))
        settings_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._settings_key = settings_font.render('Press spacebar for Options Menu.', True, rgbcolours.black)
        self._settings_posi = self._settings_key.get_rect(center = (w/2, h/(32/31)))
    
    def draw(self):
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)
        self._screen.blit(self._settings_key, self._settings_posi)
    
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self._state = 1
                self._is_valid = False
            else:
                self._state = 2
                self._is_valid = False 

class OptionScreen(default_scene):
    def __init__(self, screen):
        super().__init__(screen)
        self._state = 0
        self._background.fill(rgbcolours.light_sky_blue)
        (w, h) = self._screen.get_size() 
        easy_mode_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        medium_mode_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._easy_mode = easy_mode_font.render('Press ENTER for Easy Mode', True, rgbcolours.black)
        self._medium = medium_mode_font.render('Press SPACE for Medium Mode', True, rgbcolours.black)
        self._easy_position = self._easy_mode.get_rect(center = ((w/2), (h/3)))
        self._medium_position = self._medium.get_rect(center = ((w/2), (h/2)))

    def draw(self):
        super().draw()
        self._screen.blit(self._easy_mode, self._easy_position)
        self._screen.blit(self._medium, self._medium_position)

    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self._state = 3
            elif event.key == pygame.K_BACKSPACE:
                self._state = 0
            else:
                self._state = 2
            self._is_valid = False 

class GameLevel(default_scene):
    def __init__(self, screen, snake, food, time):
        super().__init__(screen)
        self._state = 4
        self._background.fill(rgbcolours.lavender)
        self._screen = screen
        self._snake = snake
        self._food = food
        self._clock = time
        self.timeskip = 0
        self.constMove = 0
        self._score = self._snake.getScore()
        (w, h) = self._screen.get_size()
        self.score_font = pygame.font.Font(pygame.font.get_default_font(), 48)
        self._score_screen = self.score_font.render('Score: {}'.format(self._score), True, rgbcolours.black)
        self._score_pos = self._score_screen.get_rect(center=(w/2, h/16))
    
        self._boundaryList = []
        for x in range(0, 720, 16):
            front = pygame.Rect((-45, x), (45, 45))
            back = pygame.Rect((x, -45), (45, 45))
            top = pygame.Rect((720, x), (45, 45))
            bottom = pygame.Rect((x, 720), (45, 45))
            self._boundaryList.append(front)
            self._boundaryList.append(back)
            self._boundaryList.append(top)
            self._boundaryList.append(bottom)

    def draw(self):
        super().draw()
        self._snake.draw()
        self._food.draw()
        self._screen.blit(self._score_screen, self._score_pos)
    
    def process_event(self, event):
        super().process_event(event)
        self._snake.process_event(event)

    def update(self):        
        super().update()
        self._score = self._snake.getScore()
        self._score_screen = self.score_font.render('Score: {}'.format(self._score), True, rgbcolours.black)
        
        timepassed = self._clock.tick()
        self.timeskip += timepassed
        self.constMove += timepassed       
        
        if self.timeskip > 3000:
            self._snake.addPoints()
            self.timeskip = 0
        if self.constMove > 300:
            self._snake.move(self._snake._movement)
            self._snake._tail.pop()
            self.constMove = 0
        
        for body in self._snake._tail:
            if self._snake._avatar.colliderect(body):
                self._is_valid = False
        
        if self._snake._avatar.colliderect(self._food.comparison()):
            self._snake.grow()
            self._food.newLocation()
        
        for wall in self._boundaryList:
            if self._snake._avatar.colliderect(wall):
                self._is_valid = False

class GameHarder(GameLevel):
    def update(self):        
        super().update()
        self._score = self._snake.getScore()
        self._score_screen = self.score_font.render('Score: {}'.format(self._score), True, rgbcolours.black)
        
        timepassed = self._clock.tick()
        self.timeskip += timepassed
        self.constMove += timepassed       
        
        if self.timeskip > 3000:
            self._snake.addPoints()
            self.timeskip = 0
        if self.constMove > 100:
            self._snake.move(self._snake._movement)
            self._snake._tail.pop()
            self.constMove = 0
        
        for body in self._snake._tail:
            if self._snake._avatar.colliderect(body):
                self._is_valid = False
        
        if self._snake._avatar.colliderect(self._food.comparison()):
            self._snake.grow()
            self._food.newLocation()
        
        for wall in self._boundaryList:
            if self._snake._avatar.colliderect(wall):
                self._is_valid = False

class GameOver(default_scene):
    def __init__(self, screen, snake):
        self._snake = snake
        self._score = self._snake.getScore()
        self._state = 0
        super().__init__(screen)
        self._background.fill(rgbcolours.sea_green)
        (w, h) = self._screen.get_size()
        title_font = pygame.font.Font(pygame.font.get_default_font(), 124)
        self._end_screen = title_font.render('Game Over', True, rgbcolours.dark_red)
        self._caption_pos = self._end_screen.get_rect(center=(w/2, h/2))
        self.score_font = pygame.font.Font(pygame.font.get_default_font(), 72)
        self._score_screen = self.score_font.render('Score: {}'.format(self._score), True, rgbcolours.black)
        self._score_pos = self._score_screen.get_rect(center=(w/2, h/4))

    def draw(self):
        super().draw()
        self._screen.blit(self._end_screen, self._caption_pos)
        self._screen.blit(self._score_screen, self._score_pos)

    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                pygame.quit()
            self._is_valid = False 

    def update(self):
        super().update()
        self._score = self._snake.getScore()
        self._score_screen = self.score_font.render('Score: {}'.format(self._score), True, rgbcolours.black)