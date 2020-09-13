import pygame.font

#settings_image = pygame.image.load("images/settings_menu.bmp")
class SettingsButton:

    def __init__(self, ss_game, msg):
        """Initialize button attributes."""
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.midleft = self.screen_rect.midleft

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

        self.flag = False

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

settings_image = pygame.image.load("images/settings_menu.bmp")
class SettingsMenu:
    
    def __init__(self, ss_game, msg):
        """Initialize button attributes."""
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        #settings_image = pygame.image.load("images/settings_menu.jpg").convert()

        # Set the dimensions and properties of the button
        self.width, self.height = 300, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.midright = self.screen_rect.midright

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

        flag = False

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    #def check_image(self):
        #self.screen.blit(settings_image, (0, 0))

    def draw_button(self):
        # Draw blank button and then draw message.
        #self.screen.fill(self.button_color, self.rect)
        self.screen.blit(settings_image, (0, 0))
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

