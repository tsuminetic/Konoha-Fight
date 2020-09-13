import pygame
from pygame import mixer

mixer.pre_init(44100, -16, 1, 512)
pygame.init()

game = True

while game is True:

    # the loading screen
    loading = True

    # the loading screen after you press the play button
    playloading = False

    # the controls page
    controls = False

    # the exiting page
    exiting = False

    # the main menu, if true shows if false doesnt
    intro = False

    # actual game's counddown
    actualgame_cd = False
    gamecountdown = True
    countshow = 30
    counttext = ""

    # actual game after clicking play button:
    actualgame = False

    # to turn music on or off
    speaker = True
    # to load the background music
    mixer.music.load('sounds/song.wav')

    # size and title of screen
    pygame.display.set_caption("Konoha Fight!")

    win = pygame.display.set_mode((1200, 675))

    iconimg = pygame.image.load("icon.jpg").convert_alpha()
    pygame.display.set_icon(iconimg)

    # main background img
    backgroundimg = pygame.image.load(
        "gameimages/Naruto-Hidden-Leaf-Village-Beautiful-Foto-Capture-Village.jpg").convert_alpha()

    # sppiral img
    spiralimg = pygame.image.load("gameimages/spiral.png").convert_alpha()

    # konoha fight! img
    konohaimg = pygame.image.load("gameimages/konoha.png").convert_alpha()

    # position of konoha img
    konohaposx = 200
    konohaposy = 85

    # to make animation affect for konoha img
    lolx = True
    loly = True

    # the play button image
    scrollimg1 = pygame.image.load("buttons/scroll1.png").convert_alpha()

    # the settings button imgae
    scrollimg2 = pygame.image.load("buttons/scroll2.png").convert_alpha()

    # the exit button image
    scrollimg3 = pygame.image.load("buttons/scroll3.png").convert_alpha()

    scrollimg4 = pygame.image.load("buttons/scroll4.png").convert_alpha()

    scrollimg5 = pygame.image.load("buttons/scroll5.png").convert_alpha()

    # x pos of play button
    scr1posx = 450

    # x pos of settings button
    scr2posx = 450

    # xpos of exit button
    scr3posx = 450

    scr4posx = 450

    scr5posx = 450

    # image of charecters in the background
    mainmenubackgroundcharecter1 = pygame.image.load("boy/Attack__009.png").convert_alpha()

    mainmenubackgroundcharecter2 = pygame.image.load("girl/Throw__009.png").convert_alpha()
    mainmenubackgroundcharecter2 = pygame.transform.flip(mainmenubackgroundcharecter2, True, False)

    kunaiimg = pygame.image.load("girl/Kunai.png").convert_alpha()
    kunaiimg = pygame.transform.flip(kunaiimg, True, False)

    # speaker on img
    speakeronimg = pygame.image.load("buttons/speaker on.png").convert_alpha()
    speakeronimg = pygame.transform.scale(speakeronimg, (120, 120))

    # speaker off img
    speakeroffimg = pygame.image.load("buttons/speaker off.png").convert_alpha()
    speakeroffimg = pygame.transform.scale(speakeroffimg, (120, 120))

    # company logo img lmao
    mitsuimg = pygame.image.load("gameimages/mitsu.png").convert_alpha()

    # for loading the "loading" screen
    frameno = 0

    # game stuffs

    # trees
    tree1 = pygame.image.load("gameimages/tree.png").convert_alpha()
    tree2 = pygame.image.load("gameimages/tree.png").convert_alpha()

    # location of player 1
    plr1x = 180
    plr1y = 490

    # location of player 2
    plr2x = 950
    plr2y = 490

    # jumping `up 1
    jumpup1 = False
    jumpdown1 = False

    # jumping `up 2
    jumpup2 = False
    jumpdown2 = False

    # attacking for plr1
    swordout1 = True
    swording1 = False
    swordfrm1 = 0

    # attacking for plr2
    swordout2 = True
    swording2 = False
    swordfrm2 = 0

    # kunai images (adding)
    kunai1img = pygame.image.load("girl/Kunai.png").convert_alpha()
    kunai1img = pygame.transform.flip(kunai1img, True, False)
    kunai1img = pygame.transform.scale(kunai1img, (50, 14))

    kunai2img = pygame.image.load("girl/Kunai.png").convert_alpha()
    kunai2img = pygame.transform.flip(kunai2img, True, False)
    kunai2img = pygame.transform.scale(kunai2img, (50, 14))

    # throwing kunai for plr 1
    kunai1 = False
    kunaicnt1 = True
    kunaithrwlonger1 = False
    kunai1x = ""
    kunai1y = ""
    goingback1 = False

    # throwing kunai for plr 2
    kunai2 = False
    kunaicnt2 = True
    kunaithrwlonger2 = False
    kunai2x = ""
    kunai2y = ""
    goingback2 = False

    # poofing for player 1
    poof1 = False
    poofcnt1 = 0

    # poofing for player 2
    poof2 = False
    poofcnt2 = 0

    # damage icon
    minus3 = pygame.image.load("gameimages/-3.png").convert_alpha()
    minus3 = pygame.transform.scale(minus3, (40, 40))

    minus4 = pygame.image.load("gameimages/-4.png").convert_alpha()
    minus4 = pygame.transform.scale(minus4, (40, 40))

    # health of player1
    health_1 = 100

    # health of player2
    health_2 = 100

    # if invisible
    invisible1 = False
    invisible2 = False

    # loading potrait photos
    potimg1 = pygame.image.load("gameimages/potraitphoto1.png").convert_alpha()
    potimg1 = pygame.transform.scale(potimg1, (85, 85))
    potimg2 = pygame.image.load("gameimages/potraitphoto2.png").convert_alpha()

    potimg2 = pygame.transform.flip(potimg2, True, False)
    potimg2 = pygame.transform.scale(potimg2, (85, 85))

    # gameover screen
    gameover = False
    overcnt = 0

    # wins image
    boywin = pygame.image.load("gameimages/boywins.png").convert_alpha()
    boywinx = 230
    boywiny = 90

    girlwin = pygame.image.load("gameimages/girlwins.png").convert_alpha()
    girlwinx = 200
    girlwiny = 90

    # the quitting image
    extimg = pygame.image.load("gameimages/exitingimg.png").convert_alpha()
    lmao = 0

    # the back button
    backbut = pygame.image.load("buttons/backbutton.png").convert_alpha()
    backbutx = 100
    backbuty = 100

    # the c0ntrols
    controlstxt = pygame.image.load("controlsfiles/controlstxt.png").convert_alpha()

    boytxt = pygame.image.load("controlsfiles/boytxt.png").convert_alpha()
    girltxt = pygame.image.load("controlsfiles/girltxt.png").convert_alpha()

    run1img = pygame.image.load("controlsfiles/run1.png").convert_alpha()
    jump1img = pygame.image.load("controlsfiles/jump1.png").convert_alpha()
    attack1img = pygame.image.load("controlsfiles/attack1.png").convert_alpha()
    poof1img = pygame.image.load("controlsfiles/poof1.png").convert_alpha()

    run2img = pygame.image.load("controlsfiles/run2.png").convert_alpha()
    jump2img = pygame.image.load("controlsfiles/jump2.png").convert_alpha()
    attack2img = pygame.image.load("controlsfiles/attack2.png").convert_alpha()
    poof2img = pygame.image.load("controlsfiles/poof2.png").convert_alpha()

    lineimg = pygame.image.load("controlsfiles/line.png").convert_alpha()

    # sounds
    gameoversnd = True

    jumpsnd1 = True
    jumpsnd2 = True

    kunaisnd1 = True
    kunaisnd2 = True

    poofsnd1 = True
    poofsnd2 = True

    swordsnd1 = True
    swordsnd2 = True

    fight321 = True
    # the actual game,runs if true
    run = True

    while run:
        # time interval between update in ms
        pygame.time.delay(15)

        # adding the background color
        win.fill((255, 255, 255))

        if playloading:

            # adding the play loading images
            plloadingbar = pygame.image.load("loading/load-" + str(frameno) + ".png")
            plloadingbar = pygame.transform.scale(plloadingbar, (700, 400))
            win.blit(plloadingbar, (239, 180))

            # loading text
            loadfont = pygame.font.Font('fonts/njnaruto.ttf', 40)
            loadtext = loadfont.render("Loading..", True, (0, 0, 0))
            win.blit(loadtext, (360, 260))

            # the animation effect lmao
            if frameno != 16:
                frameno += 1
            else:

                frameno = 0
                playloading = False
                actualgame_cd = True

        if loading:

            # loading the "loading bar"
            loadingbar = pygame.image.load("loading/load-" + str(frameno) + ".png")
            loadingbar = pygame.transform.scale(loadingbar, (700, 400))
            win.blit(loadingbar, (239, 360))

            # loading the mitsu logo
            mitsuimg = pygame.transform.scale(mitsuimg, (550, 170))
            win.blit(mitsuimg, (320, 100))

            # adding to the frame no until it becomes 16
            if frameno != 16:
                frameno += 1
            else:

                # if it is 16
                frameno = 0
                loading = False
                intro = True
                # playing the background music
                if speaker:
                    mixer.music.play(-1)

        if intro:

            # adding the background image
            win.blit(backgroundimg, (0, 0))

            # adding the spiral
            spiralimg = pygame.transform.scale(spiralimg, (500, 500))
            win.blit(spiralimg, (370, -90))

            # adding the konoha logo
            win.blit(konohaimg, (konohaposx, konohaposy))

            # the animation affect for koniha logo
            if lolx:
                konohaposx += 0.5
                if konohaposx == 220:
                    lolx = False
            else:
                konohaposx -= 0.5
                if konohaposx == 180:
                    lolx = True

            if loly:
                konohaposy += 1
                if konohaposy == 105:
                    loly = False
            else:
                konohaposy -= 1
                if konohaposy == 65:
                    loly = True

            # adding the copyright text in the top right corner
            font1 = pygame.font.Font('fonts/njnaruto.ttf', 10)
            code1 = font1.render("A fan-made naruto game made by mitsu-senpai, ", True, (0, 0, 0))
            code2 = font1.render("Included images might be subject to copyright!", True, (0, 0, 0))
            code3 = font1.render("none of the images are owned by the creator! ", True, (0, 0, 0))
            win.blit(code1, (940, 8))
            win.blit(code2, (940, 8 + 13))
            win.blit(code3, (940, 8 + (13 * 2)))

            # adding the charecters in the background
            win.blit(mainmenubackgroundcharecter1, (-30, 300))
            win.blit(mainmenubackgroundcharecter2, (870, 270))
            win.blit(kunaiimg, (765, 544))

            # adding speaker on or off button
            if speaker:
                win.blit(speakeronimg, (1081, 559))
            else:
                win.blit(speakeroffimg, (1081, 559))

            # adding the play button
            scrollimg1 = pygame.transform.scale(scrollimg1, (330, 75))
            win.blit(scrollimg1, (scr1posx, 285))

            # adding the settings button
            scrollimg2 = pygame.transform.scale(scrollimg2, (330, 75))
            win.blit(scrollimg2, (scr2posx, 285 + 100))

            # adding the exit button
            scrollimg3 = pygame.transform.scale(scrollimg3, (330, 75))
            win.blit(scrollimg3, (scr3posx, 285 + 200))

            # getting the position of moouse
            x, y = pygame.mouse.get_pos()

            # slide effect for play button
            if x >= 489 and x <= 741 and y >= 286 and y <= 359:
                scr1posx = 437
            else:
                scr1posx = 450

            # slide effect for settings button
            if x >= 489 and x <= 741 and y >= 386 and y <= 459:
                scr2posx = 437
            else:
                scr2posx = 450

            # slide effect for exit button
            if x >= 489 and x <= 741 and y >= 486 and y <= 559:
                scr3posx = 437
            else:
                scr3posx = 450

            # to detect the mouse click
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()

                # getting the mouse click and the x and y coordinates of the clicked area
                if e.type == pygame.MOUSEBUTTONDOWN:
                    cx, cy = pygame.mouse.get_pos()

                    # if clicked in play button
                    if cx >= 489 and cx <= 741 and cy >= 286 and cy <= 359:
                        mixer.Sound("sounds/button.wav").play()
                        intro = False
                        playloading = True

                    # if clicked in controls button
                    if cx >= 489 and cx <= 741 and cy >= 386 and cy <= 459:
                        mixer.Sound("sounds/button.wav").play()
                        intro = False
                        controls = True

                    # if clicked in exit button
                    if cx >= 489 and cx <= 741 and cy >= 486 and cy <= 559:
                        mixer.Sound("sounds/button.wav").play()
                        intro = False
                        exiting = True

                    # if clicked on speaker button
                    if cx >= 1109 and cx <= 1171 and cy >= 588 and cy <= 651:
                        mixer.Sound("sounds/button.wav").play()
                        if speaker:
                            speaker = False

                            # turn speaker off
                            mixer.music.pause()
                        else:
                            speaker = True

                            # turn speaker on
                            mixer.music.unpause()

        if controls:
            # adding the background image
            win.blit(backgroundimg, (0, 0))

            # adding the back button
            backbut = pygame.transform.scale(backbut, (backbutx, backbuty))
            win.blit(backbut, (20, 20))

            # getting the position of moouse
            bx, by = pygame.mouse.get_pos()

            # enlarge effect for back button
            if bx >= 35 and bx <= 120 and by >= 35 and by <= 105:
                backbutx = 106
                backbuty = 106
                backbut = pygame.image.load("buttons/backbutton.png").convert_alpha()

            else:
                backbutx = 100
                backbuty = 100

            # to detect the mouse click
            for cunt in pygame.event.get():
                if cunt.type == pygame.QUIT:
                    quit()

                # getting the mouse click and the x and y coordinates of the clicked area
                if cunt.type == pygame.MOUSEBUTTONDOWN:
                    cbx, cby = pygame.mouse.get_pos()

                    # if clicked in back button
                    if cbx >= 35 and cbx <= 120 and cby >= 35 and cby <= 105:
                        mixer.Sound("sounds/button.wav").play()
                        controls = False
                        intro = True
            #
            win.blit(controlstxt, (375, 30))

            win.blit(boytxt, (240, 150))
            win.blit(girltxt, (800, 150))

            win.blit(run1img, (35, 250))
            win.blit(jump1img, (305, 250))
            win.blit(attack1img, (35, 425))
            win.blit(poof1img, (305, 425))

            win.blit(run2img, (600, 250))
            win.blit(jump2img, (600 + 270, 250))
            win.blit(attack2img, (600, 425))
            win.blit(poof2img, (600 + 270, 425))

            lineimg = pygame.transform.scale(lineimg, (5, 500))
            win.blit(lineimg, (590, 150))

        # the exitting page lol
        if exiting:

            win.blit(extimg, (400, 265))
            lmao += 1
            if lmao == 10:
                quit()

        # actual game countdown
        if actualgame_cd:

            # reducing the background music's volume
            mixer.music.set_volume(0.14)

            if fight321:
                mixer.Sound("sounds/321fight.wav").play()
                fight321 = False

            # adding background in game
            win.blit(backgroundimg, (0, 0))

            # adding countdown in the game
            countx = 500
            county = 200

            if gamecountdown:

                if countshow == 30:
                    counttext = "3"

                if countshow == 20:
                    counttext = "2"

                if countshow == 10:
                    counttext = "1"

                if countshow == 0:
                    counttext = "Fight!"

                if counttext == "Fight!":
                    countx = 90
                    county = 200
                else:
                    countx = 500
                    county = 200

                # adding tree images
                win.blit(tree1, (-300, 20))
                win.blit(tree1, (860, 20))

                # blitting the countdown
                fontcd = pygame.font.Font('fonts/njnaruto.ttf', 300)
                textcd = fontcd.render(counttext, True, (0, 0, 0))
                win.blit(textcd, (countx, county))

                # slowing it and stuff
                if countshow != -10:
                    countshow -= 0.5
                else:
                    countshow = 30
                    fight321 = True
                    actualgame_cd = False
                    actualgame = True

        if actualgame:
            # adding background in game
            win.blit(backgroundimg, (0, 0))

            # changing action  -- idle,main action
            actionimg1 = "boy/Idle__0.png"
            actionimg2 = "girl/Idle__000.png"

            # scaling difference1
            xofscaling1 = 60
            xofscaling2 = 65

            # scaling difference2
            yofscaling1 = 140
            yofscaling2 = 140

            # getting events for mouse and quitting
            for evnt in pygame.event.get():
                if evnt.type == pygame.QUIT:
                    quit()

            # getting events
            keys = pygame.key.get_pressed()

            # running for plr1
            if keys[pygame.K_a] and plr1x > -35:
                actionimg1 = "boy/Run__000.png"
                xofscaling1 = 93
                plr1x -= 15

            if keys[pygame.K_d] and plr1x < 1150:
                actionimg1 = "boy/Run__000.png"
                xofscaling1 = 93
                plr1x += 15

            # running for plr2
            if keys[pygame.K_LEFT] and plr2x > -35:
                actionimg2 = "girl/Run__000.png"
                xofscaling2 = 93
                plr2x -= 15

            if keys[pygame.K_RIGHT] and plr2x < 1150:
                actionimg2 = "girl/Run__000.png"
                xofscaling2 = 93
                plr2x += 15

            # jumping for plr1 if pressed detecting
            if keys[pygame.K_w]:

                if jumpup1 == False and jumpdown1 == False:
                    jumpup1 = True

            # jumping for plr2 if pressed detecting
            if keys[pygame.K_UP]:

                if jumpup2 == False and jumpdown2 == False:
                    jumpup2 = True

            # jumping for player 1
            if jumpup1:
                if jumpsnd1:
                    mixer.Sound("sounds/jump.wav").play()
                    jumpsnd1 = False
                xofscaling1 = 93
                actionimg1 = "boy/Jump__003.png"

                if plr1y > 410:
                    plr1y -= 10

                if plr1y == 410:
                    jumpup1 = False
                    jumpdown1 = True

            if jumpdown1:
                xofscaling1 = 93
                actionimg1 = "boy/Jump__001.png"

                if plr1y < 490:
                    plr1y += 10

                if plr1y == 490:
                    jumpdown1 = False
                    jumpsnd1 = True

            # jumping for player 2
            if jumpup2:
                if jumpsnd2:
                    mixer.Sound("sounds/jump.wav").play()
                    jumpsnd2 = False
                xofscaling2 = 93
                actionimg2 = "girl/Jump__003.png"

                if plr2y > 410:
                    plr2y -= 10
                if plr2y == 410:
                    jumpup2 = False
                    jumpdown2 = True

            if jumpdown2:
                xofscaling2 = 93
                actionimg2 = "girl/Jump__001.png"

                if plr2y < 490:
                    plr2y += 10

                if plr2y == 490:
                    jumpdown2 = False
                    jumpsnd2 = True

            # attack for player1
            if keys[pygame.K_q]:
                if swordout1:
                    swording1 = True

                if plr2x > plr1x:

                    if keys[pygame.K_a]:
                        swording1 = False
            else:
                swordout1 = True

            if swording1:

                if plr2x > plr1x:
                    if swordsnd1:
                        mixer.Sound("sounds/sword.wav").play()
                        swordsnd1 = False
                    actionimg1 = "boy/Attack__005.png"
                    xofscaling1 = 140
                    if swordfrm1 == 1:
                        if not invisible2:
                            if plr2x < plr1x + 120:
                                win.blit(minus4, (plr2x, plr2y - 45))
                                health_2 -= 4

                if plr2x < plr1x:
                    if kunaicnt1:
                        if not keys[pygame.K_d]:
                            kunai1 = True
                            kunaithrwlonger1 = True

                if kunaithrwlonger1:
                    actionimg1 = "boy/Throw__007.png"
                    xofscaling1 = 93

                swordfrm1 += 1

                if swordfrm1 == 3:
                    swordfrm1 = 0
                    swordsnd1 = True

                    kunaithrwlonger1 = False
                    swording1 = False
                    swordout1 = False

            # attack for player2
            if keys[pygame.K_SLASH]:

                if swordout2:
                    swording2 = True

                if plr1x > plr2x:
                    if keys[pygame.K_LEFT]:
                        swording2 = False
            else:
                swordout2 = True

            if swording2:
                if plr1x < plr2x:
                    if kunaicnt2:
                        if not keys[pygame.K_RIGHT]:
                            kunai2 = True
                            kunaithrwlonger2 = True

                if plr1x > plr2x:
                    if swordsnd2:
                        mixer.Sound("sounds/jump.wav").play()
                        swordsnd2 = False
                    actionimg2 = "girl/Attack__005.png"
                    xofscaling2 = 120
                    if swordfrm2 == 1:
                        if not invisible1:
                            if plr1x < plr2x + 104:
                                win.blit(minus4, (plr1x, plr1y - 45))
                                health_1 -= 4

                if kunaithrwlonger2:
                    xofscaling2 = 93
                    actionimg2 = "girl/Throw__007.png"

                swordfrm2 += 1

                if swordfrm2 == 3:
                    swordfrm2 = 0
                    swordsnd2 = True

                    kunaithrwlonger2 = False
                    swording2 = False
                    swordout2 = False

            # throwing kunai for player1
            if kunai1:
                if kunaisnd1:
                    mixer.Sound("sounds/kunai.wav").play()
                    kunaisnd1 = False
                if kunaicnt1:
                    kunai1x = plr1x - 15
                    kunai1y = plr1y + 75
                    kunaicnt1 = False

                win.blit(kunai1img, (kunai1x, kunai1y))

                kunai1x -= 45

                if kunai1x <= plr2x + 5:
                    if plr2y <= 430:
                        goingback1 = True

                    if goingback1:
                        if kunai1x <= 0:
                            kunai1 = False
                            kunaicnt1 = True
                            goingback1 = False
                            kunaisnd1 = True
                    else:
                        if not invisible2:
                            win.blit(minus3, (plr2x + 3, plr2y - 45))
                            health_2 -= 2
                            kunai1 = False
                            kunaicnt1 = True
                            kunaisnd1 = True
                        else:
                            goingback1 = True

            # throwing kunai for player2
            if kunai2:
                if kunaisnd2:
                    mixer.Sound("sounds/kunai.wav").play()
                    kunaisnd2 = False
                if kunaicnt2:
                    kunai2x = plr2x - 15
                    kunai2y = plr2y + 75
                    kunaicnt2 = False

                win.blit(kunai2img, (kunai2x, kunai2y))

                kunai2x -= 45

                if kunai2x <= plr1x + 5:
                    if plr1y <= 430:
                        goingback2 = True

                    if goingback2:
                        if kunai2x <= 0:
                            kunai2 = False
                            kunaicnt2 = True
                            goingback2 = False
                            kunaisnd2 = True
                    else:
                        if not invisible1:
                            win.blit(minus3, (plr1x, plr1y - 45))
                            health_1 -= 2
                            kunai2 = False
                            kunaicnt2 = True
                            kunaisnd2 = True
                        else:
                            goingback2 = True

            # poofing lol for plr1
            if keys[pygame.K_s]:
                poof1 = True

            if poof1:
                if poofcnt1 == 0:
                    invisible1 = True
                poofcnt1 += 1

                if poofcnt1 < 3:
                    if poofsnd1:
                        mixer.Sound("sounds/poof.wav").play()
                        poofsnd1 = False
                    actionimg1 = "gameimages/poof.png"
                    xofscaling1 = 90
                    yofscaling1 = 100

                if poofcnt1 > 2 and poofcnt1 < 14:
                    actionimg1 = "gameimages/invis.png"

                if poofcnt1 == 14 or poofcnt1 == 15:
                    actionimg1 = "gameimages/poof.png"
                    xofscaling1 = 90
                    yofscaling1 = 100

                if poofcnt1 == 16:
                    invisible1 = False

                if poofcnt1 == 45:
                    poof1 = False
                    poofsnd1 = True
                    poofcnt1 = 0

            # poofing lol for plr2
            if keys[pygame.K_DOWN]:
                poof2 = True

            if poof2:
                if poofcnt2 == 0:
                    invisible2 = True
                poofcnt2 += 1

                if poofcnt2 < 3:
                    if poofsnd2:
                        mixer.Sound("sounds/poof.wav").play()
                        poofsnd2 = False
                    actionimg2 = "gameimages/poof.png"
                    xofscaling2 = 90
                    yofscaling2 = 100

                if poofcnt2 > 2 and poofcnt2 < 14:
                    actionimg2 = "gameimages/invis.png"

                if poofcnt2 == 14 or poofcnt2 == 15:
                    actionimg2 = "gameimages/poof.png"
                    xofscaling2 = 90
                    yofscaling2 = 100

                if poofcnt2 == 16:
                    invisible2 = False

                if poofcnt2 == 45:
                    poof2 = False
                    poofsnd2 = True
                    poofcnt2 = 0

            # adding player 1 img and player 2 img
            player1img = pygame.image.load(actionimg1).convert_alpha()

            player2img = pygame.image.load(actionimg2).convert_alpha()

            # scaling to flip it for plr 1 and plr 2
            if keys[pygame.K_a]:
                player1img = pygame.transform.flip(player1img, True, False)

            if keys[pygame.K_RIGHT]:
                player2img = pygame.transform.flip(player2img, True, False)

            # looking where player 2 is for plr1
            if not keys[pygame.K_a]:
                if not keys[pygame.K_d]:
                    if plr2x < plr1x:
                        player1img = pygame.transform.flip(player1img, True, False)

            # scaling and blitting player1 img
            player1img = pygame.transform.scale(player1img, (xofscaling1, yofscaling1))
            win.blit(player1img, (plr1x, plr1y))

            # looking where player 1 is for plr2
            if not keys[pygame.K_LEFT]:
                if not keys[pygame.K_RIGHT]:
                    if plr1x > plr2x:
                        player2img = pygame.transform.flip(player2img, True, False)

            # scaling and blitting player2 img
            player2img = pygame.transform.scale(player2img, (xofscaling2, yofscaling2))
            player2img = pygame.transform.flip(player2img, True, False)
            win.blit(player2img, (plr2x, plr2y))

            # adding tree images
            win.blit(tree1, (-300, 20))
            win.blit(tree1, (860, 20))

            # adding health and potrait phtoto img for player1

            if health_1 < 0:
                health_1 = 0
            healthimg1 = pygame.image.load("health/" + str(health_1) + ".png").convert_alpha()
            healthimg1 = pygame.transform.scale(healthimg1, (400, 80))
            win.blit(healthimg1, (10, 5))

            win.blit(potimg1, (10, 10))

            # adding health and potrait phtoto img for player2

            if health_2 < 0:
                health_2 = 0
            healthimg2 = pygame.image.load("health/" + str(health_2) + ".png").convert_alpha()
            healthimg2 = pygame.transform.flip(healthimg2, True, False)
            healthimg2 = pygame.transform.scale(healthimg2, (400, 80))
            win.blit(healthimg2, (789, 5))

            win.blit(potimg2, (1105, 10))

            if health_1 == 0 or health_2 == 0:
                actualgame = False
                gamecountdown = True
                gameover = True

        if gameover:
            win.blit(backgroundimg, (0, 0))
            if gameoversnd:
                mixer.Sound("sounds/gameover.wav").play()
                gameoversnd = False

            # scaling difference1
            xofscaling1 = 60
            xofscaling2 = 65

            # scaling difference2
            yofscaling1 = 140
            yofscaling2 = 140

            # action idle after killing another player
            actionimg1 = "boy/Idle__0.png"
            actionimg2 = "girl/Idle__000.png"

            # boy dying after player 2 wins
            if health_1 == 0:
                actionimg1 = "boy/Dead__" + str(overcnt) + ".png"
                xofscaling1 = 135
                yofscaling1 = 130
                if overcnt == 0:
                    plr1y = 505
                    plr2y = 490

            # girl dying after player 1 wins
            if health_2 == 0:
                actionimg2 = "girl/Dead__00" + str(overcnt) + ".png"
                xofscaling2 = 140
                if overcnt == 0:
                    plr2y = 505
                    plr1y = 490

            # deadimg plr1 and plr2
            player1img = pygame.image.load(actionimg1).convert_alpha()
            if plr2x < plr1x:
                player1img = pygame.transform.flip(player1img, True, False)
            player1img = pygame.transform.scale(player1img, (xofscaling1, yofscaling1))
            win.blit(player1img, (plr1x, plr1y))

            player2img = pygame.image.load(actionimg2).convert_alpha()
            if plr1x > plr2x:
                player2img = pygame.transform.flip(player2img, True, False)
            player2img = pygame.transform.scale(player2img, (xofscaling2, yofscaling2))
            player2img = pygame.transform.flip(player2img, True, False)
            win.blit(player2img, (plr2x, plr2y))

            # adding tree images
            win.blit(tree1, (-300, 20))
            win.blit(tree1, (860, 20))

            # adding health img and potraitong for plr1
            healthimg1 = pygame.image.load("health/" + str(health_1) + ".png").convert_alpha()
            healthimg1 = pygame.transform.scale(healthimg1, (400, 80))
            win.blit(healthimg1, (10, 5))
            win.blit(potimg1, (10, 10))

            # adding health img and potraitong for plr2
            healthimg2 = pygame.image.load("health/" + str(health_2) + ".png").convert_alpha()
            healthimg2 = pygame.transform.flip(healthimg2, True, False)
            healthimg2 = pygame.transform.scale(healthimg2, (400, 80))
            win.blit(healthimg2, (789, 5))
            win.blit(potimg2, (1105, 10))

            if health_1 == 0:
                win.blit(girlwin, (girlwinx, girlwiny))

            if health_2 == 0:
                win.blit(boywin, (boywinx, boywiny))

            # over buttons
            # adding the play again button
            scrollimg4 = pygame.transform.scale(scrollimg4, (330, 75))
            win.blit(scrollimg4, (scr4posx, 285))

            # adding the mainmenu button
            scrollimg5 = pygame.transform.scale(scrollimg5, (330, 75))
            win.blit(scrollimg5, (scr5posx, 285 + 100))

            # adding the exit button
            scrollimg6 = pygame.transform.scale(scrollimg3, (330, 75))
            win.blit(scrollimg6, (scr3posx, 285 + 200))

            # getting the position of mouse
            x, y = pygame.mouse.get_pos()

            # slide effect for play again button
            if x >= 489 and x <= 741 and y >= 286 and y <= 359:
                scr4posx = 437
            else:
                scr4posx = 450

            # slide effect for main menu button
            if x >= 489 and x <= 741 and y >= 386 and y <= 459:
                scr5posx = 437
            else:
                scr5posx = 450

            # slide effect for exit button
            if x >= 489 and x <= 741 and y >= 486 and y <= 559:
                scr3posx = 437
            else:
                scr3posx = 450

            # to detect the mouse click
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()

                # getting the mouse click and the x and y coordinates of the clicked area
                if e.type == pygame.MOUSEBUTTONDOWN:
                    cx, cy = pygame.mouse.get_pos()

                    # if clicked in play again button
                    if cx >= 489 and cx <= 741 and cy >= 286 and cy <= 359:
                        mixer.Sound("sounds/button.wav").play()
                        # for the next time
                        health_1 = 100

                        health_2 = 100

                        plr1y = 490
                        plr2y = 490

                        plr1x = 180
                        plr2x = 950

                        overcnt = -1
                        #

                        # disabling current jump for next round
                        jumpup1 = False
                        jumpdown1 = False
                        jumpup2 = False
                        jumpdown2 = False
                        #
                        # disabling kunai for new game
                        kunai1 = False
                        kunaicnt1 = True
                        kunai2 = False
                        kunaicnt2 = True
                        #

                        # disabling poof for new session
                        invisible1 = False
                        poof1 = False
                        poofcnt1 = 0
                        invisible2 = False
                        poof2 = False
                        poofcnt2 = 0
                        #

                        # disabling sword for next session
                        swordfrm1 = 0

                        kunaithrwlonger1 = False
                        swording1 = False
                        swordout1 = False

                        swordfrm2 = 0

                        kunaithrwlonger2 = False
                        swording2 = False
                        swordout2 = False
                        #

                        gameoversnd = True

                        gameover = False
                        playloading = True

                    # if clicked in main menu button
                    if cx >= 489 and cx <= 741 and cy >= 386 and cy <= 459:
                        mixer.Sound("sounds/button.wav").play()
                        # for the next time
                        health_1 = 100
                        health_2 = 100

                        plr1y = 490
                        plr2y = 490

                        plr1x = 180
                        plr2x = 950

                        overcnt = -1
                        #
                        # disabling current jump for next round
                        jumpup1 = False
                        jumpdown1 = False
                        jumpup2 = False
                        jumpdown2 = False
                        #
                        # disabling kunai for new game
                        kunai1 = False
                        kunaicnt1 = True
                        kunai2 = False
                        kunaicnt2 = True
                        #

                        # disabling poof for new session
                        invisible1 = False
                        poof1 = False
                        poofcnt1 = 0
                        invisible2 = False
                        poof2 = False
                        poofcnt2 = 0
                        #

                        # disabling sword for next session
                        swordfrm1 = 0

                        kunaithrwlonger1 = False
                        swording1 = False
                        swordout1 = False

                        swordfrm2 = 0

                        kunaithrwlonger2 = False
                        swording2 = False
                        swordout2 = False
                        #

                        gameoversnd = True

                        gameover = False
                        loading = True

                    # if clicked in exit button
                    if cx >= 489 and cx <= 741 and cy >= 486 and cy <= 559:
                        mixer.Sound("sounds/button.wav").play()
                        gameover = False
                        exiting = True

            # adding to the over counter
            if overcnt < 9:
                overcnt += 1

        # general exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # updating the screen every 20 ms
        pygame.display.update()

    # general exit function
    pygame.quit()
