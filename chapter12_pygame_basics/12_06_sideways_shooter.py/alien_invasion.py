import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

# Overall class to manage game assets and behavior


class AlienInvasion:

    # init the game and create game resources
    def __init__(self):
        pygame.init()
        # get screen widht, height, color from settings class
        self.settings = Settings()

        # custom screen size
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # full screen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_height = self.screen.get_rect().height
        # self.settings.screen_width = self.screen.get_rect().width


        pygame.display.set_caption('Alien Invasion')

        # ship
        self.ship = Ship(self)
        # bullets
        self.bullets = pygame.sprite.Group()



    # start the main loop for the game
    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_screen()

    # check events, such as user inputs
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # check for keydown events
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q :
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()


    def check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False

    def fire_bullet(self):
        # if more than allowed bullets, don't fire 
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    def update_bullets(self):
        self.bullets.update()
        # draw each bullet in sprite group
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets.copy():
            if bullet.rect.left <= 0:
                self.bullets.remove(bullet)
        

    def update_screen(self):
        # update images on the screen and flip to the new screen
        pygame.display.flip()
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
                

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
