#!/usr/bin/env python
""" Playing a sound with only Pygame. """
import pygame
import sys

def main():
    if len(sys.argv) < 2:
        print('Provide a file to play.')
        exit(1)
    print('Playing {}'.format(sys.argv[1]))
    # pygame init does init the mixer
    pygame.init()
    try:
        sound = pygame.mixer.Sound(sys.argv[1])
        pygame.mixer.music.load('knight_rider_theme.mp3')
    except pygame.error:
        print('Cannot open {}'.format(sys.argv[1]))
        raise SystemExist(str(geterror()))
    pygame.mixer.music.play(-1)

    # Wait 2 seconds
    pygame.time.wait(2000)
    # Play the sound effect
    channel = sound.play()

    # In a game you won't have to wait, but in this program
    # where the program ends immediately after playing we
    # have to stall until the sound object is finished playing.
    while channel.get_busy():
        print("playing...", end=' ')
        sys.stdout.flush()
        pygame.time.wait(250)
    print('Done!')
    # Wait for 4 seconds to enjoy the knight rider theme
    pygame.time.wait(4000)

    pygame.quit()

if __name__ == '__main__':
    main()