

class Settings():

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 0.5
        self.ship_limit = 0

        # bullet settings
        self.bullets_allowed = 5
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)

        # alien settings
        self.alien_speed = 0.2
        self.fleet_drop_speed = 30
        # FOR DIRECTION: 1 = top, -1 = bottom 
        self.fleet_direction = 1