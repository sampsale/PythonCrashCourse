import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard:
    def __init__(self, ai_game):
        # init 
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game

        # font
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_images()

    def prep_images(self):
        # prep score
        self.prep_ships()
        self.prep_score()
        self.prep_highscore()
        self.prep_level()

    def prep_score(self):
        # round to closest 10
        rounded_score = round(self.stats.score, -1)
        # turn score into rendered image
        score_str = "{:,}".format(rounded_score)
        score_str = 'Score: ' + score_str
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        # display the score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highscore(self):
        # get highscore from stats
        high_score = self.stats.get_high_score()
        # round to closest 10
        high_score = round(high_score, -1)
        # format score so _ is between numbers
        score_str = "{:,}".format(high_score)
        score_str = 'Highscore: ' + score_str
        self.highscore_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        # display the hiscore at the top 
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    # check if highschore higher than before
    def check_highscore(self):
        if self.stats.score > self.stats.high_score:
            self.stats.new_high_score(self.stats.score)
            self.prep_highscore()

    # prep level
    def prep_level(self):
        level_str = str(self.stats.level)
        level_str = 'Level: ' + level_str
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        
        # position below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    # prep HP as ships 
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)