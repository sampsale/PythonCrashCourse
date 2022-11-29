

class Settings():

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullets_allowed = 5
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)

        # alien bomb settings
        self.bomb_speed = 0.3
        self.bomb_height = 15
        self.bomb_width = 12
        self.bomb_color = (207, 10, 27)

        # alien settings
        self.fleet_drop_speed = 10

        # FOR DIRECTION: 1 = right, -1 = left
        self.fleet_direction = 1

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the score multiplier grows
        self.score_scale = 1.5

        self.initialize_dynamic_settings('easy')

    # settings to be sped up (subject to change)
    def initialize_dynamic_settings(self, difficulty):

        self.alien_points = 20

        if difficulty == 'easy':
            self.bomb_frequency = 1200
            self.ship_speed = 1.5
            self.bullet_speed = 2.0
            self.alien_speed = 0.2
        elif difficulty == 'normal':
            self.bomb_frequency = 800
            self.ship_speed = 1.5
            self.bullet_speed = 2.0
            self.alien_speed = 0.4
        elif difficulty == 'expert':
            self.bomb_frequency = 200
            self.ship_speed = 2
            self.bullet_speed = 2.0
            self.alien_speed = 0.8

    # increase DIFFICULTY
    def increase_speed(self):
        self.alien_points = int(self.alien_points * self.score_scale)
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bomb_frequency *= self.speedup_scale

