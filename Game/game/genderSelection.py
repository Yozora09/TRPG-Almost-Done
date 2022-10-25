#pili ka boy or girl sa character
from characterModel import *
from pygame import mixer

pygame.mixer.init()
bgm = mixer.Sound(r'sfx\bgm.ogg')
sfx = mixer.Sound(r'sfx\select.mp3')


def genderSelect():
    genderChoice = True
    while genderChoice == True:
        print("\n\n")
        print(" ╔██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╗ ")
        print("██ ╔██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╗ ██")
        print(" ║██ ╔██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╗ ██║ ")
        print("██ ║██                                                                                                                                                              ██║ ██")
        print(" ║██ ║                                                                                                                                                              ║ ██║ ")
        print("██ ║██     ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗      ██║ ██")
        print(" ║██ ║     ║ ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗ ║      ║ ██║ ")
        print("██ ║██     ║ ║              ██████╗██╗  ██╗ ██████╗  ██████╗ ███████╗███████╗     █████╗      ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗            ║ ║      ██║ ██")
        print(" ║██ ║     ║ ║             ██╔════╝██║  ██║██╔═══██╗██╔═══██╗██╔════╝██╔════╝    ██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗           ║ ║      ║ ██║ ")
        print("██ ║██     ║ ║             ██║     ███████║██║   ██║██║   ██║███████╗█████╗      ███████║    ██║  ███╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝           ║ ║      ██║ ██")
        print(" ║██ ║     ║ ║             ██║     ██╔══██║██║   ██║██║   ██║╚════██║██╔══╝      ██╔══██║    ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗           ║ ║      ║ ██║ ")
        print("██ ║██     ║ ║             ╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████║███████╗    ██║  ██║    ╚██████╔╝███████╗██║ ╚████║██████╔╝███████╗██║  ██║           ║ ║      ██║ ██")
        print(" ║██ ║     ║ ║              ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝           ║ ║      ║ ██║ ")
        print("██ ║██     ║ ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝ ║      ██║ ██")
        print(" ║██ ║     ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝      ║ ██║ ")
        print("██ ║██                                                                                                                                                              ██║ ██")
        print(" ║██ ║                                                                                                                                                              ║ ██║ ")
        print("██ ║██                                                                                                                                                              ██║ ██")
        print(" ║██ ║                                                                                                                                                              ║ ██║ ")
        print("██ ║██                                                                                                                                                              ██║ ██")
        print(" ║██ ║                                                  ╔═══════════════════╗                   ╔══════════════════╗                                                ║ ██║ ")
        print("██ ║██                                                  ║ ╔═══════════════╗ ║                   ║ ╔══════════════╗ ║                                                ██║ ██")
        print(" ║██ ║                                                  ║ ║               ║ ║                   ║ ║              ║ ║                                                ║ ██║ ")
        print("██ ║██                                                  ║ ║    ██████╗    ║ ║                   ║ ║    ██████╗   ║ ║                                                ██║ ██")
        print(" ║██ ║                                                  ║ ║    ██╔══██╗   ║ ║       ┌─┐┬─┐      ║ ║   ██╔════╝   ║ ║                                                ║ ██║ ")
        print("██ ║██                                                  ║ ║    ██████╔╝   ║ ║       │ │├┬┘      ║ ║   ██║  ███╗  ║ ║                                                ██║ ██")
        print(" ║██ ║                                                  ║ ║    ██╔══██╗   ║ ║       └─┘┴└─      ║ ║   ██║   ██║  ║ ║                                                ║ ██║ ")
        print("██ ║██                                                  ║ ║    ██████╔╝   ║ ║                   ║ ║   ╚██████╔╝  ║ ║                                                ██║ ██")
        print(" ║██ ║                                                  ║ ║    ╚═════╝    ║ ║                   ║ ║    ╚═════╝   ║ ║                                                ║ ██║ ")
        print("██ ║██                                                  ║ ╚═══════════════╝ ║                   ║ ╚══════════════╝ ║                                                ██║ ██")
        print(" ║██ ║                                                  ╚═══════════════════╝                   ╚══════════════════╝                                                ║ ██║ ")
        print("██ ║██                                                                                                                                                              ██║ ██")
        print(" ║██ ║                                                                                                                                                              ║ ██║ ")
        print("██ ║██                                                                                                                                                              ██║ ██")
        print(" ║██ ╚██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╝ ██║ ")
        print("██ ╚██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╝ ██")
        print(" ╚██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██══██╝ ")
        bgm.play(10)
        bgm.set_volume(0.5)
        gender = input("\n\nPress [B] for BOY and [G] for GIRL: ").upper()
        match gender:
            case "B":
                sfx.play()
                bgm.stop()
                genderBoy()
                genderChoice = False

            case "G":
                sfx.play()
                bgm.stop()
                genderGirl()
                genderChoice = False

            case other:
                bgm.stop()
                genderChoice = True