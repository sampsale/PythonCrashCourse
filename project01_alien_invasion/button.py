import pygame.font


class Button():
    def __init__(self, ai_game, msg, location):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # buttons styling
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        self.difficulty = location

        # buttons rect 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        print(self.screen_rect.width)

        # if expert or easy, move 300 pixels
        if location == 'expert':
            self.rect.center = ((self.screen_rect.center[0])+300, (self.screen_rect.center[1]))
        elif location == 'easy':
            self.rect.center = ((self.screen_rect.center[0]-300), (self.screen_rect.center[1]))
        # button message
        self.rect.y += 100
        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        # turn message into a rendered image and center text
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)