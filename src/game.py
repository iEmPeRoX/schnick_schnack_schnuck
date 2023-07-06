from tkinter import *
import random
import time 

fenster = Tk()
fenster.title("Schnick Schnack Schnuck")
fenster.geometry("640x480")
time.sleep(0)
game_is_running = True
runde = 0
auswahl = ["Schere", "Stein", "Papier"]
gegner = random.choice(auswahl)
meine_punkte = 0
gegner_punkte = 0
du = ""
deine_auswahl = False
global gegnger_label
gegnger_label = Label(fenster, text="")
gegner_number = 0
global game_status_label
global anweisungs_label



def run_game():
    global gegner
    global du
    global meine_punkte
    global gegner_punkte
    
    if gegner == "Stein":
        gegner_number=1
        if du == "Schere":
            gegner_punkte = lost(gegner_punkte)
        elif du == "Stein":
            tie()
        elif du == "Papier":
            meine_punkte = won(meine_punkte)
        else:
            error()

    if gegner == "Papier":
        gegner_number=0
        if du == "Schere":
            meine_punkte = won(meine_punkte)
        elif du == "Stein":
            gegner_punkte = lost(gegner_punkte)
        elif du == "Papier":
            tie()
        else:
            error()

    if gegner == "Schere":
        gegner_number=2
        if du == "Schere":
            tie()
        elif du == "Stein":
            meine_punkte = won(meine_punkte)
        elif du == "Papier":
            gegner_punkte = lost(gegner_punkte)
        else:
            error()
    gegner = random.choice(auswahl)
    gegner_selection.config(image=imageListe[gegner_number])
    gegnger_label.config(text="Du hast " + str(meine_punkte) + " und dein Gegner " + str(gegner_punkte))

def won(punkte):
    global gegner
    game_status_label.config(text="Gewonnen! Dein Gegner hatte " + gegner + "!")
    punkte += 1
    meine_punkte_label.config(text=str(meine_punkte))
    feedback.config(image=imageListe[4])
    return punkte

def lost(punkte):
    global gegner
    game_status_label.config(text="Verloren! Dein Gegner hatte " + gegner + "!")
    punkte += 1
    gegner_punkte_label.config(text=str(gegner_punkte))
    feedback.config(image=imageListe[5])
    return punkte

def tie():
    global gegner
    game_status_label.config(text="Unentschieden! Dein Gegner hatte auch " + gegner + "!")
    feedback.config(image=imageListe[6])
def error():
    game_status_label.config(text="Error! Wähle: Schere, Stein, Papier!")

def a_stein():
    global du
    your_selection.config(image=imageListe[1])
    du="Stein"
    run_game()


def a_papier():
    global du
    your_selection.config(image=imageListe[0])
    du="Papier"
    run_game()

def a_schere():
    your_selection.config(image=imageListe[2])
    global du
    du="Schere"
    run_game()


def draw_ui(gegnger_label):
    
    global game_status_label
    global gegner_selection
    global meine_punkte_label
    global gegner_punkte_label
    global imageListe
    global your_selection
    global feedback
    imageListe = [
        PhotoImage(file='img//papier.gif'),
        PhotoImage(file='img//stein.gif'),
        PhotoImage(file='img//schere.gif'),
        PhotoImage(file="img//question_mark.png"),
        PhotoImage(file="img//win.png"),
        PhotoImage(file="img//lose.png"),
        PhotoImage(file="img//tie.png")
    ]

    Schere_button = Button(fenster, image=imageListe[2], command=a_schere)
    Stein_button = Button(fenster, image=imageListe[1], command=a_stein)
    Papier_button = Button(fenster, image=imageListe[0], command=a_papier)

    your_selection = Label(fenster, image=imageListe[3])
    gegner_selection = Label(fenster, image=imageListe[3])
    anweisungs_label = Label(fenster, text="Willkommen zu Schnick Schnack Schnuck:\nWähle zwischen 'Schere', 'Stein', 'Papier'.")
    game_status_label = Label(fenster, text="")
    feedback = Label(fenster, image=imageListe[6])
    meine_punkte_label = Label(fenster, text="0")
    gegner_punkte_label = Label(fenster, text="0")
    #anweisungs_label.place(x=100, y=0)
    #gegnger_label.place(x=100,y=130)
    #game_status_label.place(x=320, y=240)
    
    meine_punkte_label.place(x=40, y=20)
    gegner_punkte_label.place(x=600, y=20)
    feedback.place(x=280, y=185)
    your_selection.place(x=270, y=250)
    gegner_selection.place(x=270, y=70,)
    Schere_button.place(x=150, y=370, width=100, height=100)
    Papier_button.place(x=390, y=370, width=100, height=100)
    Stein_button.place(x=270, y=370, width=100, height=100)

    fenster.mainloop()

draw_ui(gegnger_label)

