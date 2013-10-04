import pygame
from pygame.locals import *
from sys import exit
background_image_filename = 'BG_MM.png'
hoja=pygame.image.load('8bitmm.gif')
balas=pygame.image.load('balas.png')
pygame.init()
screen = pygame.display.set_mode((640, 600), 0, 32)
background = pygame.image.load(background_image_filename).convert()
xbg=0
ybg=-3600
x, y = 640/2-18/2, 0
move_x, move_y = 0, 0
speed=250
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
pygame.display.set_caption("hola!!!")
mem="no"
balena=[]
framesbal=0
haybala=0
cdbal=0
velbal=1000
salto=0
disalto=0
tanim=0
frames=0
pantalla=1
vel_caida=1500
bcai=0 #bloqueo caida
vista="der"
caminar="salto"
pygame.mixer.music.load("dr willy castle magaman 2 mio.mp3")
pygame.mixer.music.play(-1)
while True:
    
    cdbal+=framesbal
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    tanim=time_passed_seconds
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
############################## movimiento teclas ##############################
        if vel_caida!=1500:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    vista="izk"
                    mem="izk"
                    if "salto+fuego"!=caminar!="salto":
                        if "+fuego" in caminar:
                            caminar="izk+fuego"
                        else:
                            caminar="izk"
                    distance_moved = time_passed_seconds * speed
                    move_x = -distance_moved
                elif event.key == K_RIGHT:
                    vista="der"
                    mem="der"
                    if "salto+fuego"!=caminar!="salto":
                        if "+fuego" in caminar:
                            caminar="der+fuego"
                        else:
                            caminar="der"
                    distance_moved = time_passed_seconds * speed
                    move_x = +distance_moved
                elif event.key == K_UP:
                    if "salto+fuego"!=caminar!="salto":
                        if "+fuego" in caminar:
                            caminar="salto+fuego"
                        else:
                            caminar="salto"
                        bcai=1
                        salto = time_passed_seconds * vel_caida
                        move_y = -salto
                elif event.key == K_DOWN:
                    distance_moved = time_passed_seconds * speed
                    move_y = +distance_moved
                  ################## disparar #################
                elif event.key == K_SPACE:
                    caminar+="+fuego"
                    cdbal=0
                    framesbal=time_passed_seconds
         ###################### teclas al levantarse #####################           
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    mem="no"
                    if "salto+fuego"!=caminar!="salto":
                        if "+fuego" in caminar:
                            caminar="no+fuego"
                        else:
                            caminar="no"
                    move_x = 0
                elif event.key == K_RIGHT:
                    mem="no"
                    if "salto+fuego"!=caminar!="salto":
                        if "+fuego" in caminar:
                            caminar="no+fuego"
                        else:
                            caminar="no"
                    move_x = 0
                elif event.key == K_UP:
                    disalto=0
                    salto=0
                    bcai=0
                    move_y = 0
                elif event.key == K_DOWN:
                    move_y = 0
                elif event.key == K_SPACE:
                    caminar=caminar.replace("+fuego","")
                    mem=mem.replace("+fuego","")
################################## disparos ###################################
    
    if "+fuego" in caminar:
        if 0==cdbal:
            if len(balena)<1:
                balena.append(len(balena)+1)
        elif 0<cdbal<=0.15:
            pass
        else:
            cdbal=0
            if len(balena)<1:
                balena.append(len(balena)+1)
################################ animaciones ##################################
    
    if vel_caida==1500:
        hoja.set_clip(pygame.Rect(83,8, 18, 80))
        draw_me = hoja.subsurface(hoja.get_clip())
        if caminar=="no":
            x=640/2-65/2
            if 0<=frames<0.1:
                hoja.set_clip(pygame.Rect(113,13, 65, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
            elif 0.1<=frames<=0.2:
                hoja.set_clip(pygame.Rect(183,13, 65, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
                vel_caida=400
            else:
                frames=0
            

    elif caminar=="no":
        if vista=="der":
            if 0<=frames<=1.7:
                hoja.set_clip(pygame.Rect(257,13, 65, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
            elif 1.7<frames<=1.8:
                hoja.set_clip(pygame.Rect(332,13, 65, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
            else:
                frames=0
        if vista=="izk":
            if 0<=frames<=1.7:
                hoja.set_clip(pygame.Rect(501,757, 65, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
            elif 1.7<frames<=1.8:
                hoja.set_clip(pygame.Rect(426,757, 65, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
            else:
                frames=0
    elif caminar=="der":
        if 0<frames<0.15:
            hoja.set_clip(pygame.Rect(398,13, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.15<=frames<=0.3:
            hoja.set_clip(pygame.Rect(473,13, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.3<frames<=0.45:
            hoja.set_clip(pygame.Rect(537,13, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.45<frames<=0.6:
            hoja.set_clip(pygame.Rect(598,13, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.6<frames<=0.75:
            hoja.set_clip(pygame.Rect(537,13, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        else:
            frames=0.15
    elif caminar=="izk":
        if 0<frames<0.15:
            hoja.set_clip(pygame.Rect(358,757, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.15<=frames<=0.3:
            hoja.set_clip(pygame.Rect(285,757, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.3<frames<=0.45:
            hoja.set_clip(pygame.Rect(221,757, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.45<frames<=0.6:
            hoja.set_clip(pygame.Rect(160,757, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.6<frames<=0.75:
            hoja.set_clip(pygame.Rect(221,757, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        else:
            frames=0.15
    elif caminar=="salto":
        if vista=="der":
            hoja.set_clip(pygame.Rect(668,13, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif vista=="izk":
            hoja.set_clip(pygame.Rect(90,757, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        ########################## + fuego ########################
    elif caminar=="no+fuego":
        if vista=="der":
            if 0<=frames<=0.7:
                hoja.set_clip(pygame.Rect(37,103, 81, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                    balas.set_clip(pygame.Rect(0,0, 24, 75))
                    draw_bala = balas.subsurface(balas.get_clip())
            elif 0.7<frames<=1:            
                hoja.set_clip(pygame.Rect(257,13, 65, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
            else:
                frames=0
        if vista=="izk":
            if 0<=frames<=0.7:
                hoja.set_clip(pygame.Rect(705,847, 81, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                    balas.set_clip(pygame.Rect(0,0, 24, 75))
                    draw_bala = balas.subsurface(balas.get_clip())
            elif 0.7<frames<=1:
                hoja.set_clip(pygame.Rect(485,757, 81, 75))
                draw_me = hoja.subsurface(hoja.get_clip())
            else:
                frames=0
    elif caminar=="der+fuego":
        if 0<=frames<0.15:
            hoja.set_clip(pygame.Rect(398,13, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.15<=frames<=0.3:
            hoja.set_clip(pygame.Rect(125,103, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(24,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
        elif 0.3<frames<=0.45:
            hoja.set_clip(pygame.Rect(205,103, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(48,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
        elif 0.45<frames<=0.6:
            hoja.set_clip(pygame.Rect(285,103, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(24,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
        elif 0.6<frames<=0.75:
            hoja.set_clip(pygame.Rect(205,103, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(48,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
        else:
            frames=0.15
    elif caminar=="izk+fuego":
        if 0<frames<0.15:
            hoja.set_clip(pygame.Rect(358,757, 65, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
        elif 0.15<=frames<=0.3:
            hoja.set_clip(pygame.Rect(617,847, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(24,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
        elif 0.3<frames<=0.45:
            hoja.set_clip(pygame.Rect(537,847, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(48,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
        elif 0.45<frames<=0.6:
            hoja.set_clip(pygame.Rect(457,847, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(24,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
        elif 0.6<frames<=0.75:
            hoja.set_clip(pygame.Rect(537,847, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(48,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
        else:
            frames=0.15
    elif caminar=="salto+fuego":
        if vista=="der":
            hoja.set_clip(pygame.Rect(366,103, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(72,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
        elif vista=="izk":
            hoja.set_clip(pygame.Rect(376,847, 81, 75))
            draw_me = hoja.subsurface(hoja.get_clip())
            if haybala!=1:
                balas.set_clip(pygame.Rect(72,0, 24, 75))
                draw_bala = balas.subsurface(balas.get_clip())
########################## restricciones de movimiento ########################

    if bcai==0:
        y+=time_passed_seconds*vel_caida
    disalto+=salto
    if disalto>=75*2:
        bcai=0
        move_y=0
        disalto=0
    frames+=tanim
    x+= move_x
    y+= move_y
    if pantalla>=9:
        if y<0:
            ybg+=600
            y=600-75
            pantalla+=1
        if y+75>600:
            ybg-=600
            y=0
            pantalla-=1
    if pantalla<=9:
        if x+65>=640:
            xbg-=640
            pantalla+=1
            x=0
        if x<0 and pantalla!=1:
            xbg+=640
            pantalla-=1
            x=575
        
        if y+75>=480:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=480-75
            ################## pantallas ##################        
    if pantalla==1:
        if x<=0:
            x=0
    if pantalla==2:
        if x<465 and y+75>=440:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=440-75
        if x<480 and y+75>457:
            x=480
        if 110<x<305 and y+75>=400:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=400-75
        if 95<x<320 and y+75>417:
            if 290<x<=320:
                x=320
            if 95<=x<120:
                x=95
    if pantalla==3:
        if x<140 and y+75>=440:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=440-75
        if x<160 and y+75>=450:
            x=160
        if x>255 and y+75>457:
            x=255
        if x>255 and y+75>=450:
            x=255
        if x>265 and y+75>=440:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=440-75
        if x>430 and y+75>=400:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=400-75
        if x>415 and y+75>417:
            x=415
        if x>2415 and y+75>=410:
            x=415
    if pantalla==4:
        if x<145 and y+75>=440:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=440-75
        if x<160 and y+75>457:
            x=160
    if pantalla==6:
        if 270<x<470 and y+75>=440:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=440-75
        if 255<x<480 and y+75>447:
            if 450<x<=480:
                x=480
            if 270>x>=255:
                x=255
    if pantalla==7:
        if y+75>=440:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=440-75
        if 110<x<305 and y+75>=400:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=400-75
        if 95<x<320 and y+75>417:
            if 290<x<=320:
                x=320
            if 120>x>=95:
                x=95
        if x>430 and y+75>=400:
            if caminar=="salto":
                caminar=mem
            elif caminar=="salto+fuego":
                caminar=mem+"+fuego"
            y=400-75
        if x>415 and y+75>417:
            x=415
        if x>2415 and y+75>=410:
            x=415
    if pantalla==9:
        if x>415:
            x=415
    if pantalla>=9:
        bcai=1                 ## para poder subir
        disalto=0              ##
        caminar="no"           ## 

    screen.fill((0, 0, 0))
    screen.blit(background, (xbg, ybg))
    if (caminar=="no+fuego" or caminar=="der+fuego" or caminar=="izk+fuego" or caminar=="salto+fuego") and vista=="izk":
        screen.blit(draw_me,(x-18,y))
    else:
        screen.blit(draw_me,(x,y))
    if len(balena)>0:
        if vista=="der" and haybala!=1:
            xbal1,ybal1=x+81,y
            haybala=1
            if velbal<0:
                velbal=-velbal
        elif vista=="izk" and haybala!=1:
            xbal1,ybal1=x-24,y
            haybala=1
            if velbal>0:
                velbal=-velbal            
        xbal1+=time_passed_seconds*velbal
        screen.blit(draw_bala,(xbal1,ybal1))
        if xbal1+24>=640 or xbal1<0:
            haybala=0
            del balena[-1]

        
    pygame.display.update()
