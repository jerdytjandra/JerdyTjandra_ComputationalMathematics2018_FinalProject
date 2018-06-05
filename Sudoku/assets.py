from pygame import *
from pygame.sprite import *
from pygame.font import *

class Background(Sprite):
    def __init__(self,pos,imagefile):
        Sprite.__init__(self)
        self.image = image.load(imagefile).convert()
        self.width,self.height = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = pos

class Sign(Sprite):
    def __init__(self,imagefile,pos,x_size,y_size):
        Sprite.__init__(self)
        self.image = image.load(imagefile)
        self.image = transform.scale(self.image,(x_size,y_size))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def draw(self,screen):
        screen.blit(self.image,self.rect)

class Button(Sprite):
    def __init__(self,imagefile,pos,x_size,y_size,oversize_x,oversize_y):
        Sprite.__init__(self)
        self.position = pos
        self.normalsize_x,self.normalsize_y = [x_size,y_size]
        self.oversize_x,self.oversize_y = [oversize_x,oversize_y]
        self.image = image.load(imagefile)
        self.image = transform.scale(self.image,(self.normalsize_x,self.normalsize_y))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def mouseover(self):
        self.image = transform.scale(self.image,(self.oversize_x,self.oversize_y))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def mouseout(self):
        self.image = transform.scale(self.image,(self.normalsize_x,self.normalsize_y))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def draw(self,screen):
        screen.blit(self.image,self.rect)

class Value(Sprite):
    def __init__(self,x_pos,y_pos,value):
        Sprite.__init__(self)
        self.font = SysFont(None,35)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.score = value
        self.color = (0,0,0)
        self.image = self.font.render("%s" % self.score,True,self.color)
        self.rect = self.image.get_rect()
        self.rect.center = [self.x_pos,self.y_pos]

    def renew(self):
        if self.score == "  ":
            self.score = 1
            self.image = self.font.render("%s" % self.score,True,(0,0,0))
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_pos,self.y_pos]
        elif self.score == 9:
            self.score = "  "
            self.image = self.font.render("%s" % self.score,True,(0,0,0))
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_pos,self.y_pos]
        else:
            self.score += 1
            self.image = self.font.render("%s" % self.score,True,(0,0,0))
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_pos,self.y_pos]

    def answer_false(self):
        self.color = (255,0,0)
        self.image = self.font.render("%s" % self.score,True,self.color)

    def get_score(self):
        return self.score

    def getrect(self):
        return self.rect

    # def reset(self):
    #     self.score = 0
    #     self.image = self.font.render("%s" % self.score,True,(255,255,0))

# class Text(Sprite):
#     def __init__(self,text,pos,fontsize,color):
#         Sprite.__init__(self)
#         self.font = SysFont(None,fontsize)
#         self.image = self.font.render("%s" % text,True,color)
#         self.rect = self.image.get_rect()
#         self.rect.center = pos
#
# class Scorelist(Sprite):
#     def __init__(self,text,pos,fontsize,color):
#         Sprite.__init__(self)
#         self.font = SysFont(None,fontsize)
#         self.image = self.font.render("%s" % text,True,color)
#         self.rect = self.image.get_rect()
#         self.rect.left,self.rect.centery = pos
#
# class nameboard(Sprite):
#     def __init__(self,pos):
#         Sprite.__init__(self)
#         self.font = SysFont(None,40)
#         self.name_list = []
#         self.name_str = "".join(self.name_list)
#         self.image = self.font.render(self.name_str,True,(0,0,0))
#         self.rect = self.image.get_rect()
#         self.rect.center = pos
#
#     def update(self,letter,pos = [200,180]):
#         if len(self.name_list) < 7:
#             self.name_list.append(letter)
#             self.name_str = "".join(self.name_list)
#             self.image = self.font.render(self.name_str,True,(0,0,0))
#             self.rect = self.image.get_rect()
#             self.rect.center = pos
#
#     def remove(self,pos = [200,180]):
#         if self.name_list:
#             del self.name_list[-1]
#             self.name_str = "".join(self.name_list)
#             self.image = self.font.render(self.name_str,True,(0,0,0))
#             self.rect = self.image.get_rect()
#             self.rect.center = pos
#
#     def get_name(self):
#         return self.name_str
