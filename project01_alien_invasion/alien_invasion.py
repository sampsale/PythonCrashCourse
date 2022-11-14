import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from gamestats import GameStats
from key_events import check_keydown_events, check_keyup_events, check_play_button
from button import Button
from scoreboard import ScoreBoard

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
        # button
        self.play_button_easy = Button(self, 'Play easy', 'easy')
        self.play_button_normal = Button(self, 'Play normal', 'normal')
        self.play_button_expert = Button(self, 'Play expert', 'expert')
        # buttons
        self.buttons = (self.play_button_easy, self.play_button_normal, self.play_button_expert)
        # scoreboard
        self.sb = ScoreBoard(self)
        self.create_fleet()
        


    # start the main loop for the game

    def run_game(self):
        while True:
            self.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_aliens()
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
        self.check_bullet_alien_collisions()
        # make dictionary of overlapping bullets and aliens
        # True, True = delete bullet, delete alien if collided

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

    def update_screen(self):
        # update images on the screen and flip to the new screen
        pygame.display.flip()
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # draw scores
        self.sb.show_score()
        # look for aliens hitting the bottom
        self.alien_hit_bottom()
        # draw play button if game is inactive
        if not self.stats.game_active:
            self.play_button_easy.draw_button()
            self.play_button_normal.draw_button()
            self.play_button_expert.draw_button()

    # make aliens fleet
    def create_fleet(self):
        # determine alien
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        # determine ship
        ship_height = self.ship.rect.height
        #print(f"Alien width: {alien_width} Alien height: {alien_height}")
        # available space x is screen width - 2*alien width
        available_space_x = self.settings.screen_width - (2*alien_width)
        # number of aliens per row available space divided by (2 * alien_width). Use // to make in an integer and remove the reminder
        aliens_per_row = available_space_x // (2*alien_width)
        # available space y == number of rows
        available_space_y = self.settings.screen_height - \
            (3*alien_height) - ship_height
        number_rows = available_space_y // (2*alien_height)

        #print(f"Rows: {number_rows} Aliens per row: {aliens_per_row}")
        # do as many times as number of rows
        for row_number in range(number_rows):
            # do as many times as number of aliens per row
            for alien_number in range(aliens_per_row):
                self.create_alien(alien_number, row_number)

    # create aliens
    def create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        # assign position
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = (alien_height + 2 * alien_height * row_number) - 30
        print(
            f"Alien {alien_number+1} on row {row_number+1} X position: {alien.rect.x} Y position: {alien.rect.y}")
        self.aliens.add(alien)

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_if_hit_edge():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        # if collisions, give score
        if collisions:
            # give score for each alien hit 
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_highscore()
        # if no aliens in group, reset screen and increase next wave's speed
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()
            # increase level
            self.stats.level += 1
            self.sb.prep_level()
    
    def ship_hit(self):
        if self.stats.ships_left > 0:
            # respond to ship being hit by an alien
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # remove remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            # create new fleet and center ship
            self.create_fleet()
            self.ship.center_ship()
            # pause
            sleep(0.5)
        else: 
            pygame.mouse.set_visible(True)
            self.stats.game_active = False
            

    def alien_hit_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    # STATS
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit



            

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
