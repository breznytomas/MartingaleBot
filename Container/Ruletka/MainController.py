import pyautogui
import keyboard;
from time import sleep;
from pynput.mouse import Button, Controller
from playsound import playsound



import xml.etree.ElementTree as ET
filename = "Analysis/analysis.xml"
tree = ET.parse(filename)
root = tree.getroot()
rootPocitanie = 0





# ||||||||||||| values to change|||||||||||||
t_start = [1508, 921]  # t je skratka pre tlacitko
t_start_color = [247, 255, 18]
t_clear = [1550, 429]
t_stavka_na_cervenu = [794, 625]
t_zeton_10_centov = [733, 971]
t_sipka_dolava = [610, 987]
pozicia_odcitania_farby = [349, 212]
cervena_farba = [134, 45, 5]
cierna_farba = [1, 26, 21]
zelena_farba = [17, 78, 20]

# ||||||||||||||||||||||||||||||||||


mouse = Controller()
def Click(x_pos, y_pos):
    mouse.position = (x_pos, y_pos)
    mouse.click(Button.left, 1)






def doYouWantToHear():
    while True:
        if keyboard.is_pressed('q'):
            while keyboard.is_pressed('q'):
                continue
            doYouWantSound = True
            FirstSpin(doYouWantSound)

        elif keyboard.is_pressed('w'):
            while keyboard.is_pressed('q'):
                continue
            doYouWantSound = False
            FirstSpin(doYouWantSound)


def FirstSpin(doYouWantSound):
    if doYouWantSound==True:
        playsound('sounds/Toumi/zacinameHru.mp3')

    Click(t_clear[0], t_clear[1])  # clear
    Click(t_sipka_dolava[0], t_sipka_dolava[1])  # click na sipku
    Click(t_sipka_dolava[0], t_sipka_dolava[1])  # click na sipku
    Click(t_zeton_10_centov[0], t_zeton_10_centov[1])  # zeton
    Click(t_stavka_na_cervenu[0], t_stavka_na_cervenu[1])  # stavka na cervenu
    Click(t_stavka_na_cervenu[0], t_stavka_na_cervenu[1])  # stavka na cervenu
    Click(t_start[0], t_start[1])  # zapni masinu
    sleep(2)
    MartingaleDecisionmaking(doYouWantSound)

 # ||||||||||||||||||faza rozhodovania|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def MartingaleDecisionmaking(doYouWantSound):
        pocitadloprejebov = 2;
        clickCounterprejebov = 2
        xmlRootLevelCounter=2
        while True:

            # ||||||||||||||ked padne cervena|||||||||||||
            if pyautogui.pixelMatchesColor(pozicia_odcitania_farby[0], pozicia_odcitania_farby[1],
                                           (cervena_farba[0], cervena_farba[1], cervena_farba[2])):
                if pyautogui.pixelMatchesColor(t_start[0], t_start[1], (t_start_color[0], t_start_color[1], t_start_color[2])):
                    print("jebla cervena")
                    if doYouWantSound==True:
                        playsound("sounds/Toumi/vyhralSiLove.mp3")
                    Click(t_clear[0], t_clear[1])  # clear
                    Click(t_sipka_dolava[0], t_sipka_dolava[1])  # click na sipku
                    Click(t_sipka_dolava[0], t_sipka_dolava[1])  # click na sipku
                    Click(t_zeton_10_centov[0], t_zeton_10_centov[1])  # zeton
                    Click(t_stavka_na_cervenu[0], t_stavka_na_cervenu[1])
                    Click(t_stavka_na_cervenu[0], t_stavka_na_cervenu[1])
                    Click(t_start[0], t_start[1])  # zapni masinu

                    xmlValueTakenFromXmlFile=int(root[xmlRootLevelCounter].text) #zapisovanie do xml
                    xmlValueTakenFromXmlFile=xmlValueTakenFromXmlFile+1
                    root[xmlRootLevelCounter].text = str(xmlValueTakenFromXmlFile)

                    xmlTotalSpinsCounter = int(root[0].text)  # zapisovanie do xml
                    xmlTotalSpinsCounter = xmlTotalSpinsCounter + 1
                    root[0].text = str(xmlTotalSpinsCounter)

                    xmlTotalWinningSpinsCounter = int(root[1].text)  # zapisovanie do xml
                    xmlTotalWinningSpinsCounter = xmlTotalWinningSpinsCounter + 1
                    root[0].text = str(xmlTotalWinningSpinsCounter)

                    tree.write(filename)

                    xmlRootLevelCounter=1
                    clickCounterprejebov = 2
                    pocitadloprejebov = 2
                    sleep(3)

            # ||||||||||||||||||||||jebla cierna alebo zelena||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

            elif ((pyautogui.pixelMatchesColor(pozicia_odcitania_farby[0], pozicia_odcitania_farby[1],
                                               (cierna_farba[0], cierna_farba[1], cierna_farba[2]))) or (
                  pyautogui.pixelMatchesColor(pozicia_odcitania_farby[0], pozicia_odcitania_farby[1],
                                              (zelena_farba[0], zelena_farba[1], zelena_farba[2])))):
                print("prave padla cierna alebo zelena")
                sleep(1)
                if doYouWantSound==True:
                    playsound('sounds/Toumi/prejebalSi.mp3')

                clickCounterprejebov = clickCounterprejebov * 2
                pocitadloprejebov = clickCounterprejebov
                xmlRootLevelCounter=xmlRootLevelCounter+1
                print("xmlRootLevelCalculator :" + str(xmlRootLevelCounter))

                sleep(0.3)
                Click(t_clear[0], t_clear[1])  # clear
                Click(t_sipka_dolava[0], t_sipka_dolava[1])  # click na sipku
                Click(t_sipka_dolava[0], t_sipka_dolava[1])  # click na sipku
                Click(t_zeton_10_centov[0], t_zeton_10_centov[1])  # zeton

                if (pocitadloprejebov*0.2) > 51.2:
                    clickCounterprejebov = 2
                    pocitadloprejebov = 2
                    print("o kurwa")

                while clickCounterprejebov > 0:
                    Click(t_stavka_na_cervenu[0], t_stavka_na_cervenu[1])  # stavka na cervenu
                    clickCounterprejebov = clickCounterprejebov - 1


                Click(t_start[0], t_start[1])  # zapni masinu

                xmlTotalSpinsCounter = int(root[0].text)  # zapisovanie do xml
                xmlTotalSpinsCounter = xmlTotalSpinsCounter + 1
                root[0].text = str(xmlTotalSpinsCounter)

                tree.write(filename)

                clickCounterprejebov = pocitadloprejebov
                print(pocitadloprejebov * 0.2)
                sleep(3)



            # ||||||||||||||||||tolerancia cholerstva||||||||||||||||||||||||||||||||||||||||||||||||||
            else:
                #print("pokracujem")
                # sleep(0.2)
                continue;


doYouWantToHear()
