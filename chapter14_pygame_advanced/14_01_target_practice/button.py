import pygame.font


class Button():
    def __init__(self, ai_game, msg, button_color):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # buttons styling
        self.width, self.height = 400, 70
        self.button_color = button_color
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # buttons rect 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button message
        points = str(ai_game.stats.squares_missed)
        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        # turn message into a rendered image and center text
        msg = str(msg)
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, msg):
        self.prep_msg(msg)
        # draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)