import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

# sprite group definition
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

# class attributes    
    Player.containers = (drawable,updatable)
    Asteroid.containers = (drawable,updatable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

# create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create player and asteroid field (asteroids are created in AsteroidField.update())
    player = Player(SCREEN_WIDTH*0.5, SCREEN_HEIGHT*0.5)
    asteroidfield = AsteroidField()
    
# MAIN LOOO
######################
    while True:
# quit game?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

# draw background
        screen.fill((0,0,0))

# IMPORTANT - slows game not to run over 60FPS AND return (in miliseconds) how much time passed from previous loop
        dt = clock.tick(60)/1000

# somehow you only have to call update once
        updatable.update(dt)

# colision detection
        for circle in asteroids:
            collision = circle.check_collision(player)
            if collision:
                print ("Game over!")
                return

# but you have to itarate to draw                
        for thing in drawable:
            
            thing.draw(screen)

# refresh screen
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
