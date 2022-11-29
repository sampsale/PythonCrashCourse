import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from square import Square
from gamestats import GameStats
from time import sleep
from button import Button
import json

# Overall class to manage game assets and behavior


class TargetPractice:

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

        pygame.display.set_caption('Target practice for alien invasion')
        # stats
        self.stats = GameStats(self)
        # ship
        self.ship = Ship(self)
        # bullets
        self.bullets = pygame.sprite.Group()
        # squares
        self.squares = pygame.sprite.Group()
        # button
        self.play_button = Button(self, 'Play', (0, 255, 0))
        self.lose_button = Button(self, f'You lose! Points ', (255,0,0))
        # create fleet
        self.create_square()

    # start the main loop for the game

    def run_game(self):
        while True:
            self.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_squares()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_r:
            self.__init__()
        elif event.key == pygame.K_p:
            self.play()

    def check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False

    def check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.reset_stats()
            self.play()
    
    def play(self):
        self.stats.reset_stats()
        self.stats.game_active = True

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
                self.stats.squares_missed += 1
                print(self.stats.squares_missed)
                if self.stats.squares_missed == 3:
                    print("you lose")
                    self.bullets.empty()
                    self.stats.lost = True
                    self.stats.game_active = False
        # make dictionary of overlapping bullets and aliens
        # True, True = delete bullet, delete alien if collided
        self.check_bullet_square_collisions()

    def update_screen(self):
        # update images on the screen and flip to the new screen
        pygame.display.flip()
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.squares.draw(self.screen)
        if not self.stats.game_active and not self.stats.lost:
            self.play_button.draw_button("Play")
            self.reset_stats()
        elif not self.stats.game_active and self.stats.lost:
            self.lose_button.draw_button(f"You lost! Points: {self.stats.squares_hit}")
            
        
    # update aliens

    def update_squares(self):
        self.check_fleet_edges()
        self.squares.update()
        if pygame.sprite.spritecollideany(self.ship, self.squares):
            self.ship_hit()
        

    # make target square
    def create_square(self):
        square = Square(self)
        square.rect.x += 25
        self.squares.add(square)
       

    def check_fleet_edges(self):
        for square in self.squares.sprites():
            if square.check_if_hit_edge():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        self.settings.fleet_direction *= -1

    def check_bullet_square_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.squares, True, True)
        if collisions:
            self.stats.squares_hit += 1
            self.settings.alien_speed += 0.1
            print(f'hit square {self.stats.squares_hit}')
        if not self.squares:
            self.bullets.empty()
            self.create_square()


 
    def reset_stats(self):
        self.settings.alien_speed = 0.2
        self.ship.center_ship()
        self.stats.squares_missed = 0
        self.stats.squares_hit = 0


if __name__ == '__main__':
    # make a game instance and run the game
    tp = TargetPractice()
    tp.run_game()
