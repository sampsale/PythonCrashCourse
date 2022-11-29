import pygame
import sys


def check_keydown_events(self, event):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        self.ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_r:
        self.__init__()
        pygame.mouse.set_visible(True)
    elif event.key == pygame.K_SPACE:
        self.fire_bullet()
    elif event.key == pygame.K_p:
        play(self)


def check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        self.ship.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        self.ship.moving_left = False


def check_play_button(self, mouse_pos):
    # loop through button list
    for button in self.buttons:
        button_clicked = button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # give difficulty to init dynamic settings
            self.sb.prep_level()
            self.sb.prep_ships()
            self.settings.initialize_dynamic_settings(button.difficulty)
            play(self)


def play(self):
    self.stats.reset_stats()
    pygame.mouse.set_visible(False)
    self.stats.game_active = True