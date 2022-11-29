
import pygame

class GameStats():
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.squares_missed = 0
        self.squares_hit = 0 
        self.lost = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.squares_hit = 0
        self.squares_missed = 0