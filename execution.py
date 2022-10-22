import pygame
from snakey import *
from snake_object import *
from fruit_object import *

def display_info():
    """ Print out information about the display driver and video information. """
    print('The display is using the "{}" driver.'.format(pygame.display.get_driver()))
    print('Video Info:')
    print(pygame.display.Info())  

def main():
    print('hello world!')
    pygame.init()
    
    display_info()
    window_size = (720, 720)

    screen = pygame.display.set_mode(window_size)
    title = 'Tapeworm'
    pygame.display.set_caption(title)

    playtime = pygame.time.Clock()

    snake = SnakeBody(screen)
    food = fruit(screen, rgbcolours.red4)

    MainMenu = TitleScene(screen, title, rgbcolours.red, 72)
    Settings = OptionScreen(screen)
    EasyLevel = GameLevel(screen, snake, food, playtime)
    MediumLevel = GameHarder(screen, snake, food, playtime)
    EndGame = GameOver(screen, snake)

    scene_list = [MainMenu]              

    for scene in scene_list:
        while scene.is_valid():
            for e in pygame.event.get():
                scene.process_event(e)
            scene.update()
            scene.draw()
            pygame.display.update()
        if scene.getNextState() == 1:
            scene_list.append(Settings)
        elif scene.getNextState() == 2:
            scene_list.append(EasyLevel)
        elif scene.getNextState() == 3:
            scene_list.append(MediumLevel)
        elif scene.getNextState() == 4:
            scene_list.append(EndGame)
        elif scene.getNextState() == 0:
            scene_list.append(MainMenu)
        
    pygame.quit()

if __name__ == '__main__':
    main()