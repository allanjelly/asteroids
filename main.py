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
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Player.containers = (drawable, updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        dt = clock.tick(60)/1000

        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        

if __name__ == "__main__":
    main()
