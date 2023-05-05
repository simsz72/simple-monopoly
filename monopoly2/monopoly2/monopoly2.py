import pyllist, pygame
import monopoly2
import random
from pyllist import sllist, sllistnode

pygame.init()
screen = pygame.display.set_mode((1200, 600))
card_length = 130
card_breadth = 100
inConfig = False
inPos = False
inLenta = False
inZaidimas = False
inInstructions = False
inError = False



name = sllist([])
value = sllist([])

name.append("Kalejimas")
value.append(-1000000)

monopoly2.playercount = 0
monopoly2.ikikiek = 10000
monopoly2.money1 = 100
monopoly2.money2 = 100
monopoly2.money3 = 100
monopoly2.pos1 = 1
monopoly2.pos2 = 1
monopoly2.pos3 = 1
monopoly2.turn = 1
monopoly2.a = 0
monopoly2.gameturn = 0
monopoly2.p1injailturn = 0
monopoly2.p2injailturn = 0
monopoly2.p3injailturn = 0

with open('duom.txt') as openfileobject:
    for line in openfileobject:
        try: 
            int(line)
            value.append(line[:-1])
        except ValueError:
            name.append(line[:-1])

font = pygame.font.Font(None, 20)
korteles_pavadinimas = font.render('hello', True, "Black")

"""SPALVOS"""
kortele = pygame.Surface((card_breadth, card_length))
kortele.fill("White")
hud_line = pygame.Surface((5, 600))
hud_line.fill("Black")
menufill = pygame.Surface((210, 200))
menufill.fill("White")
instructionsfill = pygame.Surface((700, 200))
instructionsfill.fill("White")
clearscreen = pygame.Surface((1200, 600))
clearscreen.fill("Black")
"""TEKSTAI"""
menutext0 = font.render('MENU', True, "Black")
menutext1 = font.render('1 - Pradeti zaidima', True, "Black")
menutext2 = font.render('2 - Konfiguruoti zaidimo lenta', True, "Black")
menutext3 = font.render('0 - Iseiti is zaidimo', True, "Black")
configtext0 = font.render('1 - Prideti kortele', True, "Black")
configtext1 = font.render('2 - Istrinti kortele', True, "Black")
configtext2 = font.render('0 - Grizti i meniu', True, "Black")
menutext4 = font.render('3 - Instrukcijos', True, "Black")
instructionstext0 = font.render('INSTRUKCIJOS', True, "Black")
instructionstext1 = font.render('Žaidimą gali žaisti du arba trys žaidėjai. Metus kauliuką ir paėjus atitinkamą kiekį žingsnių, žaidėjas gauna ', True, "Black")
instructionstext2 = font.render('arba netenka tiek pinigų, kiek nurodyta laukelio informacijoje. Žaidimo lenta keliaujama ratu ir žaidimas', True, "Black")
instructionstext3 = font.render('pasibaigia, kai kuris nors iš žaidėjų pirmas surenka nustatytą kiekį pinigėlių.', True, "Black")
iveskitepavadinima = font.render('Iveskite korteles pavadinima', True, "White")
iveskitereiksme = font.render('Iveskite korteles reiksme', True, "White")
iveskitepozicija = font.render('Iveskite pozicija (1-7)', True, "White")
pagalpavadinima = font.render('1 - Istrinti pagal pavadinima', True, "Black")
pagalpozicija = font.render('2 - istrinti pagal pozicija', True, "Black")
maksimalussk = font.render('Pasiektas maksimalus korteliu skaicius', True, "White")
menutext5 = font.render('4 - Isvalyti lenta', True, "Black")
playertext1 = font.render('Pasirinkite zaideju skaiciu', True, "Black")
playertext2 = font.render('1 - Du zaidejai', True, "Black")
playertext3 = font.render('2 - Trys zaidejai', True, "Black")
playerinfotext1 = font.render('Zaidejas 1', True, "Black")
playerinfoscore1 = font.render('Taskai:', True, "Black")
playerinfotext2 = font.render('Zaidejas 2', True, "Black")
playerinfotext3 = font.render('Zaidejas 3', True, "Black")
iveskitetaskusk = font.render('Iveskite iki kiek tasku bus zaidziama (iki 1000000 (1mln) )', True, "White")
taskai = font.render('Zaidziama iki (tasku):', True, "Black")
eile = font.render('Dabar eile:', True, "Black")
ridentikauliuka = font.render('1 - Mesti kauliuka', True, "Black")
iskrito = font.render('Kauliukas rodo     !', True, "Black")
testi = font.render('Paspauskite 1 kad testi', True, "Black")
pokytis = font.render('Uzlipote ant korteles su reiksme:', True, "Black")
win1 = font.render('1 ZAIDEJAS LAIMEJO!!!!!!!!!!!!!!!!!!!!!!!!!', True, "White")
win2 = font.render('2 ZAIDEJAS LAIMEJO!!!!!!!!!!!!!!!!!!!!!!!!!', True, "White") 
win3 = font.render('3 ZAIDEJAS LAIMEJO!!!!!!!!!!!!!!!!!!!!!!!!!', True, "White")
winmenu = font.render('0 - Grizti i meniu', True, "White")
ohno = font.render('(Praleisite 2 ejimus!!)', True, "Black")

text = ""
input_active = True
test_surface = pygame.image.load('b.png')
player_hud = pygame.image.load('hud.png')
kortele1 = pygame.image.load('kortele1.png')
kortele2 = pygame.image.load('kortele2.png')
kortele3 = pygame.image.load('kortele3.png')
kortele4 = pygame.image.load('kortele4.png')
kortele5 = pygame.image.load('kortele5.png')
kortele6 = pygame.image.load('kortele6.png')
kortele7 = pygame.image.load('kortele7.png')
player1 = pygame.image.load('figura1.png')
player2 = pygame.image.load('figura2.png')
player3 = pygame.image.load('figura3.png')
playercard = pygame.image.load('player.png')

def zaidejuKiekis():
    screen.blit(clearscreen, (0,0))
    if name.size == 0:
        menu()
    else:
        screen.blit(menufill, (10,10))
        screen.blit(playertext1, (30,30))
        screen.blit(playertext2, (20,60))
        screen.blit(playertext3, (20,80))
        screen.blit(configtext2, (20,180))
        inPlayerCount = True
        while inPlayerCount is True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            monopoly2.playercount = 2
                            inPlayerCount = False
                        elif event.key == pygame.K_2:
                            monopoly2.playercount = 3
                            inPlayerCount = False
                        elif event.key == pygame.K_0:
                            menu()
                            inPlayerCount = False
                        else:
                            zaidejuKiekis()
                            inPlayerCount = False
        taskukiekis()

def taskukiekis():
        ok = True
        input_active = True
        text = ""
        while ok is True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                        ok = False
                    elif event.key == pygame.K_BACKSPACE:
                        text =  text[:-1]
                    else:
                        text += event.unicode
                screen.fill(0)
                text_surf = font.render(text, True, (255, 255, 255))
                screen.blit(iveskitetaskusk, (450,250))
                screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
                pygame.display.flip()
        if int(text) <= 1000000 and int(text) >= 0:
            monopoly2.ikikiek = int(text)
            zaidimas()
        else:
            taskukiekis()

def lenta():
    screen.blit(clearscreen, (0,0))
    screen.blit(menufill, (10,10))
    screen.blit(configtext0, (20,30))
    screen.blit(configtext1, (20,50))
    screen.blit(configtext2, (20,180))
    inLenta = True
    while inLenta is True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        addCard()
                        inLenta = False
                    elif event.key == pygame.K_2:
                        deleteCard()
                        inLenta = False
                    elif event.key == pygame.K_0:
                        menu()
                        inLenta = False
                    else:
                        lenta()
                        inLenta = False


def deleteCard():

    screen.blit(clearscreen, (0,0))
    screen.blit(menufill, (10,10))
    screen.blit(pagalpavadinima, (20,30))
    screen.blit(pagalpozicija, (20,50))
    screen.blit(configtext2, (20,180))
    indeleteCard = True
    while indeleteCard is True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        deleteName()
                        indeleteCard = False
                    elif event.key == pygame.K_2:
                        deleteValue()
                        indeleteCard = False
                    elif event.key == pygame.K_0:
                        lenta()
                        indeleteCard = False
                    else:
                        deleteCard()
                        indeletCard = False

def deleteValue():
    ok = True
    input_active = True
    text = ""
    while ok is True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    ok = False
                elif event.key == pygame.K_BACKSPACE:
                    text =  text[:-1]
                else:
                    text += event.unicode
            screen.fill(0)
            text_surf = font.render(text, True, (255, 255, 255))
            screen.blit(iveskitepozicija, (550,250))
            screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
            pygame.display.flip()
    num = int(text)
    if num <= 0:
        deleteValue()
    if name.size is 7:
        while num > 7:
            num = num - 7
    if name.size is 6:
        while num > 6:
            num = num - 6
    if name.size is 5:
        while num > 5:
            num = num - 5
    if name.size is 4:
        while num > 4:
            num = num - 4
    if name.size is 3:
        while num > 3:
            num = num - 3
    if name.size is 2:
        while num > 2:
            num = num - 2
    if name.size is 1:
        while num > 1:
            num = num - 1
    if name.size is 0:
        deleteCard()
    else:
        node = value.nodeat(num-1)
        value.remove(node)
        node = name.nodeat(num-1)
        name.remove(node)
        deleteCard()
        


def deleteName():
    ok = True
    input_active = True
    text = ""
    while ok is True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    ok = False
                elif event.key == pygame.K_BACKSPACE:
                    text =  text[:-1]
                else:
                    text += event.unicode
            screen.fill(0)
            text_surf = font.render(text, True, (255, 255, 255))
            screen.blit(iveskitepavadinima, (515,250))
            screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
            pygame.display.flip()
    x = 0
    for i in name:
        if i == text:
            node = value.nodeat(x)
            value.remove(node)
            node = name.nodeat(x)
            name.remove(node)
        x = x+1
    deleteCard()



def addCard():

    if name.size >= 7:
        screen.blit(clearscreen, (0,0))
        screen.blit(maksimalussk, (515,250))
        pygame.display.update()
        inError = True
        while inError is True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    screen.blit(clearscreen, (0,0))
                    lenta()
                    inError = False
    else:
        """PAVADINIMAS"""
        ok = True
        input_active = True
        text = ""
        while ok is True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                        ok = False
                    elif event.key == pygame.K_BACKSPACE:
                        text =  text[:-1]
                    else:
                        text += event.unicode
                screen.fill(0)
                text_surf = font.render(text, True, (255, 255, 255))
                screen.blit(iveskitepavadinima, (515,250))
                screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
                pygame.display.flip()

        name.append(text)
        if text == "Kalejimas":
            value.append(-1000000)
            screen.blit(clearscreen, (0,0))
            lenta()
        else:
            ok = True
            input_active = True
            text = ""
            while ok is True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and input_active:
                        if event.key == pygame.K_RETURN:
                            input_active = False
                            ok = False
                        elif event.key == pygame.K_BACKSPACE:
                            text =  text[:-1]
                        else:
                            text += event.unicode
                    screen.fill(0)
                    text_surf = font.render(text, True, (255, 255, 255))
                    screen.blit(iveskitereiksme, (520,250))
                    screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))
                    pygame.display.flip()

            value.append(int(text))
            screen.blit(clearscreen, (0,0))
            lenta()


def menu():
    screen.blit(clearscreen, (0,0)) 
    screen.blit(menufill, (10,10))
    screen.blit(menutext0, (95,30))
    screen.blit(menutext1, (20,60))
    screen.blit(menutext2, (20,80))
    screen.blit(menutext4, (20,100))
    screen.blit(menutext5, (20,120))
    screen.blit(menutext3, (20,180))

def drawBoard():
     sk = name.size
     screen.blit(clearscreen, (0,0)) 
     screen.blit(test_surface, (0, 0))
     screen.blit(player_hud, (900, 0))
     screen.blit(hud_line, (900, 0))
     screen.blit(configtext2, (1000,570))
     screen.blit(ridentikauliuka, (1000,550))
     screen.blit(playercard, (925,75))
     screen.blit(playercard, (925,240))
     screen.blit(playercard, (925,400))
     screen.blit(player1, (950, 120))
     screen.blit(playerinfotext1, (938, 100))
     screen.blit(playerinfoscore1, (1050, 150))
     screen.blit(player2, (945, 290))
     screen.blit(playerinfotext2, (938, 265))
     screen.blit(playerinfoscore1, (1050, 315))
     screen.blit(taskai, (925,10))
     screen.blit(eile, (925,30))
     if monopoly2.playercount == 2 and monopoly2.turn > 2:
        monopoly2.turn = monopoly2.turn-2
     if monopoly2.turn == 1:
        screen.blit(playerinfotext1, (1000, 30))
     elif monopoly2.turn == 2:
        screen.blit(playerinfotext2, (1000, 30))
     temp = str(monopoly2.ikikiek).encode("utf-8").decode("utf-8") 
     temp = font.render(temp, True, "Black")
     screen.blit(temp, (1062, 11))
     if monopoly2.playercount == 3:
        screen.blit(player3, (945, 445))
        screen.blit(playerinfotext3, (938, 420))
        screen.blit(playerinfoscore1, (1050, 470))
        if monopoly2.turn == 3:
            screen.blit(playerinfotext3, (1000, 30))
        if monopoly2.turn > 3:
            monopoly2.turn = monopoly2.turn-3
     if sk >= 1:
        screen.blit(kortele1, (7, 100))
        temp = font.render('1. '+name[0], True, "Black")
        screen.blit(temp, (7+8, 100+20))
        temp = str(value[0]).encode("utf-8").decode("utf-8") 
        temp = font.render(temp, True, "Black")
        screen.blit(temp, (7+8, 100+45))
     if sk >= 2:
        screen.blit(kortele2, (220, 100))
        temp = font.render('2. '+name[1], True, "Black")
        screen.blit(temp, (220+8, 100+20))
        temp = str(value[1]).encode("utf-8").decode("utf-8") 
        temp = font.render(temp, True, "Black")
        screen.blit(temp, (220+8, 100+45))
     if sk >= 3:
        screen.blit(kortele3, (440, 80))
        temp = font.render('3. '+name[2], True, "Black")
        screen.blit(temp, (440+8, 80+20))
        temp = str(value[2]).encode("utf-8").decode("utf-8") 
        temp = font.render(temp, True, "Black")
        screen.blit(temp, (440+8, 80+45))
     if sk >= 4:
        screen.blit(kortele4, (660, 80))
        temp = font.render('4. '+name[3], True, "Black")
        screen.blit(temp, (660+8, 80+20))
        temp = str(value[3]).encode("utf-8").decode("utf-8") 
        temp = font.render(temp, True, "Black")
        screen.blit(temp, (660+8, 80+45))
     if sk >= 5:
        screen.blit(kortele5, (620, 400))
        temp = font.render('5. '+name[4], True, "Black")
        screen.blit(temp, (620+8, 400+20))
        temp = str(value[4]).encode("utf-8").decode("utf-8") 
        temp = font.render(temp, True, "Black")
        screen.blit(temp, (620+8, 400+45))
     if sk >= 6:
        screen.blit(kortele6, (380, 400))
        temp = font.render('6. '+name[5], True, "Black")
        screen.blit(temp, (380+8, 400+20))
        temp = str(value[5]).encode("utf-8").decode("utf-8") 
        temp = font.render(temp, True, "Black")
        screen.blit(temp, (380+8, 400+45))
     if sk >= 7:
        screen.blit(kortele7, (50, 350))
        temp = font.render('7. '+name[6], True, "Black")
        screen.blit(temp, (50+8, 350+20))
        temp = str(value[6]).encode("utf-8").decode("utf-8") 
        temp = font.render(temp, True, "Black")
        screen.blit(temp, (50+8, 350+45))
    
def p1pos():
    if monopoly2.pos1 == 1:
        screen.blit(player1, (15, 175))
    if monopoly2.pos1 == 2:
        screen.blit(player1, (228, 175))
    if monopoly2.pos1 == 3:
        screen.blit(player1, (448, 155))
    if monopoly2.pos1 == 4:
        screen.blit(player1, (668, 155))
    if monopoly2.pos1 == 5:
        screen.blit(player1, (628, 475))
    if monopoly2.pos1 == 6:
        screen.blit(player1, (388, 475))
    if monopoly2.pos1 == 7:
        screen.blit(player1, (58, 425))

def p2pos():
    if monopoly2.pos2 == 1:
        screen.blit(player2, (55, 165))
    if monopoly2.pos2 == 2:
        screen.blit(player2, (268, 165))
    if monopoly2.pos2 == 3:
        screen.blit(player2, (488, 145))
    if monopoly2.pos2 == 4:
        screen.blit(player2, (708, 145))
    if monopoly2.pos2 == 5:
        screen.blit(player2, (668, 465))
    if monopoly2.pos2 == 6:
        screen.blit(player2, (428, 465))
    if monopoly2.pos2 == 7:
        screen.blit(player2, (98, 415))

def p3pos():
    if monopoly2.pos3 == 1:
        screen.blit(player3, (60, 200))
    if monopoly2.pos3 == 2:
        screen.blit(player3, (273, 200))
    if monopoly2.pos3 == 3:
        screen.blit(player3, (493, 180))
    if monopoly2.pos3 == 4:
        screen.blit(player3, (713, 180))
    if monopoly2.pos3 == 5:
        screen.blit(player3, (673, 500))
    if monopoly2.pos3 == 6:
        screen.blit(player3, (433, 500))
    if monopoly2.pos3 == 7:
        screen.blit(player3, (103, 450))

def kauliukas():
    a = random.randrange(1,7)
    screen.blit(iskrito, (400,300))
    temp = str(a).encode("utf-8").decode("utf-8") 
    temp = font.render(temp, True, "Black")
    screen.blit(temp, (500, 300))
    screen.blit(testi, (385, 375))
    screen.blit(pokytis, (350, 325))
    if monopoly2.turn == 1:
         monopoly2.pos1 = monopoly2.pos1 + a
         if monopoly2.pos1 > name.size:
            while pos1 > name.size:
                monopoly2.pos1 = monopoly2.pos1-name.size
         if name[monopoly2.pos1-1] == "Kalejimas":
            screen.blit(ohno, (390, 350))
         tempm = int(value[monopoly2.pos1-1])
         monopoly2.money1 = monopoly2.money1 + tempm
         if monopoly2.money1 < 0:
            monopoly2.money1 = 0
         monopoly2.p1injailturn = 0
    elif monopoly2.turn == 2:
         monopoly2.pos2 = monopoly2.pos2 + a
         if monopoly2.pos2 > name.size:
            while pos2 > name.size:
                monopoly2.pos2 = monopoly2.pos2-name.size
         if name[monopoly2.pos2-1] == "Kalejimas":
            screen.blit(ohno, (390, 350))
         tempm = int(value[monopoly2.pos2-1])
         monopoly2.money2 = monopoly2.money2 + tempm
         if monopoly2.money2 < 0:
             monopoly2.money2 = 0
         monopoly2.p2injailturn = 0
    elif monopoly2.turn == 3:
         monopoly2.pos3 = monopoly2.pos3 + a
         if monopoly2.pos3 > name.size:
            while pos3 > name.size:
                monopoly2.pos3 = monopoly2.pos3-name.size
         if name[monopoly2.pos3-1] == "Kalejimas":
            screen.blit(ohno, (390, 350))
         tempm = int(value[monopoly2.pos3-1])
         monopoly2.money3 = monopoly2.money3 + tempm
         if monopoly2.money3 < 0:
             monopoly2.money3 = 0
         monopoly2.p3injailturn = 0
    temp = str(tempm).encode("utf-8").decode("utf-8") 
    temp = font.render(temp, True, "Black")
    screen.blit(temp, (558, 325))
    inKauliukas = True
    while inKauliukas is True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        monopoly2.turn = monopoly2.turn + 1
                        inKauliukas = False
                    if event.key == pygame.K_0:
                        menu()
                        inKauliukas = False
                        inZaidimas = False
    monopoly2.gameturn = monopoly2.gameturn + 1

def zaidimas():
    monopoly2.money1 = 100
    monopoly2.money2 = 100
    monopoly2.money3 = 100
    monopoly2.pos1 = 1
    monopoly2.pos2 = 1
    monopoly2.pos3 = 1
    monopoly2.turn = 1
    monopoly2.a = 0
    monopoly2.gameturn = 0
    inZaidimas = True
    while inZaidimas is True:
        drawBoard()
        playerMoney()
        isInJail()
        p1pos()
        p2pos()
        if monopoly2.playercount == 3:
            p3pos()
        isWin()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    kauliukas()
                if event.key == pygame.K_0:
                    screen.blit(clearscreen, (0,0)) 
                    menu()
                    inZaidimas = False

def isInJail():
    if monopoly2.turn == 1 and name[monopoly2.pos1-1] == "Kalejimas" and monopoly2.gameturn > monopoly2.playercount and monopoly2.p1injailturn != 2:
        if monopoly2.p1injailturn == 0:
            monopoly2.turn = monopoly2.turn + 1
            monopoly2.p1injailturn = monopoly2.p1injailturn + 1
        elif monopoly2.p1injailturn == 1:
            monopoly2.turn = monopoly2.turn + 1
            monopoly2.p1injailturn = 2
    if monopoly2.turn == 2 and name[monopoly2.pos2-1] == "Kalejimas" and monopoly2.gameturn > monopoly2.playercount and monopoly2.p2injailturn != 2:
        if monopoly2.p2injailturn == 0:
            monopoly2.turn = monopoly2.turn + 1
            monopoly2.p2injailturn = monopoly2.p2injailturn + 1
        elif monopoly2.p2injailturn == 1:
            monopoly2.turn = monopoly2.turn + 1
            monopoly2.p2injailturn = 2
    if monopoly2.turn == 3 and name[monopoly2.pos3-1] == "Kalejimas" and monopoly2.gameturn > monopoly2.playercount and monopoly2.p3injailturn != 2:
        if monopoly2.p3injailturn == 0:
            monopoly2.turn = monopoly2.turn + 1
            monopoly2.p3injailturn = monopoly2.p3injailturn + 1
        elif monopoly2.p3injailturn == 1:
            monopoly2.turn = monopoly2.turn + 1
            monopoly2.p3injailturn = 2
def isWin():
    if monopoly2.money1 >= monopoly2.ikikiek:
        screen.blit(clearscreen, (0,0))
        screen.blit(win1, (515,250))
        screen.blit(winmenu, (550, 350))
        inZaidimas = False
    if monopoly2.money2 >= monopoly2.ikikiek:
        screen.blit(clearscreen, (0,0)) 
        screen.blit(win2, (515,250))
        screen.blit(winmenu, (550, 350))
        inZaidimas = False
    if monopoly2.money3 >= monopoly2.ikikiek and monopoly2.playercount == 3:
        screen.blit(clearscreen, (0,0)) 
        screen.blit(win3, (515,250))
        screen.blit(winmenu, (550, 350))
        inZaidimas = False


def playerMoney():
     temp = str(monopoly2.money1).encode("utf-8").decode("utf-8") 
     temp = font.render(temp, True, "Black")
     screen.blit(temp, (1100, 151))
     temp = str(monopoly2.money2).encode("utf-8").decode("utf-8") 
     temp = font.render(temp, True, "Black")
     screen.blit(temp, (1100, 316))
     if(monopoly2.playercount == 3):
        temp = str(monopoly2.money3).encode("utf-8").decode("utf-8") 
        temp = font.render(temp, True, "Black")
        screen.blit(temp, (1100, 471))

def instrukcijos():
    screen.blit(instructionsfill, (10,10))
    screen.blit(instructionstext0, (300,30))
    screen.blit(instructionstext1, (20,60))
    screen.blit(instructionstext2, (20,80))
    screen.blit(instructionstext3, (20,100))
    screen.blit(configtext2, (20,180))
    inInstructions = True
    while inInstructions is True:
        clock = pygame.time.Clock()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    screen.blit(clearscreen, (0,0)) 
                    menu()
                    inInstructions = False

def isvalyti():
    while value.size != 0:
        node = value.nodeat(value.size-1)
        value.remove(node)
        node = name.nodeat(value.size-1)
        name.remove(node)
    
open = True
menu()
while open:
    inConfig = False
    inLenta = False
    inPos = False
    inZaidimas = False
    inInstructions = False
    inKauliukas = False
    clock = pygame.time.Clock()
    pygame.display.set_caption("Supaprastintas monopolis")
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    zaidejuKiekis()
                if event.key == pygame.K_2:
                    lenta()
                if event.key == pygame.K_3:
                    instrukcijos()
                if event.key == pygame.K_4:
                    isvalyti()
                if event.key == pygame.K_0:
                        pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()
            open = False
