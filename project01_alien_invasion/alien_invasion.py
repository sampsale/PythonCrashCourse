import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from gamestats import GameStats
from key_events_module import check_keydown_events, check_keyup_events, check_play_button
from button import Button
from scoreboard import ScoreBoard
from alien_module import update_aliens, create_fleet
from collision_module import check_bomb_ship_collisions, check_bullet_alien_collisions, alien_hit_bottom

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

        self.fullScreen = False

        # full screen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_height = self.screen.get_rect().height
        # self.settings.screen_width = self.screen.get_rect().width
        # self.fullScreen = True

        # create alien fleet

        pygame.display.set_caption('Alien Invasion')

        # stats
        self.stats = GameStats(self)
        # aliens
        self.aliens = pygame.sprite.Group()
        # ship
        self.ship = Ship(self)
        # bullets
        self.bullets = pygame.sprite.Group()
        # bombs dropped by aliens
        self.bombs = pygame.sprite.Group()
        # button
        self.play_button_easy = Button(self, 'Play easy', 'easy')
        self.play_button_normal = Button(self, 'Play normal', 'normal')
        self.play_button_expert = Button(self, 'Play expert', 'expert')
        # buttons
        self.buttons = (self.play_button_easy,
                        self.play_button_normal, self.play_button_expert)
        # scoreboard
        self.sb = ScoreBoard(self)
        create_fleet(self)

    # start the main loop for the game

    def run_game(self):
        while True:
            self.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_bombs()
                update_aliens(self)
            self.update_screen()

    # check events, such as user inputs
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # check for keydown events

            elif event.type == pygame.KEYDOWN:
                check_keydown_events(self, event)
            elif event.type == pygame.KEYUP:
                check_keyup_events(self, event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                check_play_button(self, mouse_pos)

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
            if bullet.rect.top <= 0:
                self.bullets.remove(bullet)
        check_bullet_alien_collisions(self)


    def update_bombs(self):
        self.bombs.update()
        # draw each bomb in sprite group
        for bomb in self.bombs.sprites():
            bomb.draw_bomb()
        for bomb in self.bombs.copy():
            if bomb.rect.bottom >= self.screen.get_height():
                self.bombs.remove(bomb)
        check_bomb_ship_collisions(self)
        # make dictionary of overlapping bullets and aliens
        # True, True = delete bullet, delete alien if collided

    def update_screen(self):
        # update images on the screen and flip to the new screen
        pygame.display.flip()
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # draw scores
        self.sb.show_score()
        # look for aliens hitting the bottom
        alien_hit_bottom(self)
        # draw play button if game is inactive
        if not self.stats.game_active:
            self.play_button_easy.draw_button()
            self.play_button_normal.draw_button()
            self.play_button_expert.draw_button()

    # do this if ship collides with alien or with alien bomb or if alien gets to the bottom
    def ship_hit(self):
        if self.stats.ships_left > 0:
            # respond to ship being hit by an alien
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # remove remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            self.bombs.empty()
            # create new fleet and center ship
            create_fleet(self)
            self.ship.center_ship()
            # pause
            sleep(0.5)
        else:
            pygame.mouse.set_visible(True)
            self.stats.game_active = False

    # STATS
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit


if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
