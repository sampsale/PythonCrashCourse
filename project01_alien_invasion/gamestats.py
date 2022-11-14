
import pygame

import json


class GameStats():
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.get_high_score()
        
    def reset_stats(self):        
        self.score = 0
        self.ships_left = self.settings.ship_limit
        self.level = 1

    def new_high_score(self, highscore):
        with open("highscore.json", 'w') as f:
            json.dump(highscore, f)

    def get_high_score(self):
        with open("highscore.json", 'r') as f:
            self.high_score = json.load(f)
        return self.high_score