from assets import *
from Game import *
from pygame.mixer import *

#Initialize
pygame.init()
screen_width,screen_height = [540,540]
screen = display.set_mode([screen_width,screen_height])
menu_background = Background([0,0],"background.jpg")
# mixer.music.load(".mp3") #loading the backgroud music

#Title and Button
title = Sign("title.png",[270,100],*[180,70])
start = Button("start.png",[270,250],*[120,40],*[140,60])
terminate = Button("stop.png",[270,350],*[120,40],*[140,60])

menu = Group(title,start,terminate)
# music.play(loops=-1)#to make sure the music loops infinitely
# music.set_volume(0.2)
running = True

while running:
    screen.blit(menu_background.image,menu_background.rect)
    menu.draw(screen)

    for command in event.get():
        if command.type == QUIT:
            running = False
            pygame.quit()
        if command.type == MOUSEBUTTONDOWN and command.button == 1:
            if start.rect.collidepoint(mouse.get_pos()):
                # try:
                game(screen,screen_width,screen_height)#execute game function
                # except (TypeError, AttributeError):
                #     print("error")
                # music.set_volume(0.2) #set bg music back to normal

                #try and except is used to handle error in case the player decides to cancel the gameplay midway
                #even though the gameplay is cancelled, player and result still need value to be assigned, which would create error if None is assigned
                #the error is handled by except, which would just pass the error and avoid stopping the menu loop

            elif terminate.rect.collidepoint(mouse.get_pos()):
                running = False
                pygame.quit()

    if start.rect.collidepoint(mouse.get_pos()):
        start.mouseover()
    else:
        start.mouseout()

    if terminate.rect.collidepoint(mouse.get_pos()):
        terminate.mouseover()
    else:
        terminate.mouseout()
    #the mouseover function is to create an oversized button effect when mouse is hovered over the button
    #the mouseout function is to make the oversized button back to normal when mouse is out of the button

    display.update()



#this game is created based on the original flappy bird by Dong Nguyen
#all rights goes to rightful person, I dont have any intention to commercialize it nor any intent to gain profit out of it
#except for educatonal purpose
#I want to say my gratitude to Aldy,Georgius,Pier,Radhiatama who have helped me finishing this project
#below are the link where I get all the raw material:
    #https://www.wired.com/images_blogs/gamelife/2014/02/title.jpg
    #http://piq.codeus.net/static/media/userpics/piq_179527_400x400.png
    #http://www.ellison.rocks/clumsy-bird/data/img/bg.png
    #https://www.sounds-resource.com/mobile/flappybird/sound/5309/
    #http://www.pygame.org/news
    #https://stackoverflow.com/
#My code is inspired from this:
	#https://www.youtube.com/watch?v=h2Uhla6nLDU&t=100s

