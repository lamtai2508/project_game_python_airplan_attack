import pygame.font


class Question:

    def __init__(self, game_settings, screen,msg,ans1,ans2,ans3,ans4):
        """Initialize button attributes."""
        #thiet lap man hinh
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Set the dimensions and properties of the button.
        #thiet lap nut bat dau
        self.x,self.y=60,10
        self.x1,self.y1=10,200
        self.x2,self.y2=10,280
        self.x3,self.y3=10,360
        self.x4,self.y4=10,440
        self.width, self.height = 800, 50
        self.width1, self.height1 = 800, 50
        self.width2, self.height2 = 800, 50
        self.width3, self.height3 = 800, 50
        self.width4, self.height4 = 800, 50
        
        self.button_color = (0,0,205)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect1 = pygame.Rect(self.x1, self.y1, self.width1, self.height1)
        self.rect2 = pygame.Rect(self.x2, self.y2, self.width2, self.height2)
        self.rect3 = pygame.Rect(self.x3, self.y3, self.width3, self.height3)
        self.rect4 = pygame.Rect(self.x4, self.y4, self.width4, self.height4)
        # self.rect.center = self.screen_rect.center
        # The button message needs to be prepped only once.
        self.prep_msg(msg)
        self.prep_ans1(ans1)
        self.prep_ans2(ans2)
        self.prep_ans3(ans3)
        self.prep_ans4(ans4)
    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
        
    def prep_ans1(self,ans1):
        self.ans1_image = self.font.render(ans1, True, self.text_color, self.button_color)
        self.ans1_image_rect = self.ans1_image.get_rect()
    def prep_ans2(self,ans2):
        self.ans2_image = self.font.render(ans2, True, self.text_color, self.button_color)
        self.ans2_image_rect = self.ans2_image.get_rect()
    def prep_ans3(self,ans3):
        self.ans3_image = self.font.render(ans3, True, self.text_color, self.button_color)
        self.ans3_image_rect = self.ans3_image.get_rect()
    def prep_ans4(self,ans4):
        self.ans4_image = self.font.render(ans4, True, self.text_color, self.button_color)
        self.ans4_image_rect = self.ans4_image.get_rect()
    
    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        self.screen.fill(self.button_color, self.rect1)
        self.screen.blit(self.ans1_image, self.rect1)
        
        self.screen.fill(self.button_color, self.rect2)
        self.screen.blit(self.ans2_image, self.rect2)
        
        self.screen.fill(self.button_color, self.rect3)
        self.screen.blit(self.ans3_image, self.rect3)
        
        self.screen.fill(self.button_color, self.rect4)
        self.screen.blit(self.ans4_image, self.rect4)
        


if __name__ == '__main__':
    print("Go to main file and run from there.")