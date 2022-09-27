class Settings():

    def __init__(self, screen_width, screen_height, bg_color):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg_color =  bg_color
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3