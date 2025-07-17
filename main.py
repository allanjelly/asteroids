import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        dt = clock.tick(60)/1000

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        

if __name__ == "__main__":
    main()
