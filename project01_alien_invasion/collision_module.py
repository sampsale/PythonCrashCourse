from time import sleep
import pygame 
from alien_module import create_fleet


# check if alien hit bottom
def alien_hit_bottom(self):
    screen_rect = self.screen.get_rect()
    for alien in self.aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            self.ship_hit()
            break

# check if alien bomb collides with ship
def check_bomb_ship_collisions(self):
    collisions = pygame.sprite.spritecollide(self.ship, self.bombs, True)
    if collisions:
        self.ship_hit()


# check if alien bomb collides with ship
def check_bomb_ship_collisions(self):
    collisions = pygame.sprite.spritecollide(self.ship, self.bombs, True)
    if collisions:
        self.ship_hit()

# check if bullet collides with alien
def check_bullet_alien_collisions(self):
    # make dictionary of overlapping bullets and aliens
    # True, True = delete bullet, delete alien if collided
    collisions_to_alien = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)
    # if collisions, give score
    if collisions_to_alien:
        # give score for each alien hit
        for aliens in collisions_to_alien.values():
            self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_highscore()
    # if no aliens in group, reset screen and increase next wave's speed
    if not self.aliens:
        self.bullets.empty()
        self.bombs.empty()
        create_fleet(self)
        self.settings.increase_speed()
        # increase level
        self.stats.level += 1
        self.sb.prep_level()
