# Import des modules nécessaires
from tkinter import *
from PIL import ImageTk, Image
import simpleaudio as sa
import time

# Initialisation de la fenêtre
fenetre = Tk()
fenetre.title("Piano - 2021")
fenetre.geometry("1300x700")
fenetre.minsize(1200, 200)
icon = PhotoImage(file='piano.gif')
fenetre.tk.call('wm', 'iconphoto', fenetre._w, icon)


# Déclaration des fonctions


    # DO - Octave 1
do1_note = sa.WaveObject.from_wave_file("Notes/DO1.wav")
do1_isPressed = 0

def do1_app(event=True) :

    piano.itemconfigure(DO1, fill='red')
    print("down")

    global do1_isPressed
    if do1_isPressed < 1 :
        global do1_joue
        do1_joue = do1_note.play()
        print("playing")

    do1_isPressed += 1
    print(do1_isPressed)

def do1_rel(event=True) :

    piano.itemconfigure(DO1, fill='white')
    print("up")

    global do1_joue
    do1_joue.stop()
    global do1_isPressed
    do1_isPressed = 0


    # RE - Octave 1
re1_note = sa.WaveObject.from_wave_file("Notes/RE1.wav")
re1_isPressed = 0

def re1_app(event=True) :

    piano.itemconfigure(RE1, fill='red')
    print("down")

    global re1_isPressed
    if re1_isPressed < 1 :
        global re1_joue
        re1_joue = re1_note.play()
        print("playing")

    re1_isPressed += 1
    print(re1_isPressed)

def re1_rel(event=True) :

    piano.itemconfigure(RE1, fill='white')
    print("up")

    global re1_joue
    re1_joue.stop()
    global re1_isPressed
    re1_isPressed = 0


    # MI - Octave 1
mi1_note = sa.WaveObject.from_wave_file("Notes/MI1.wav")
mi1_isPressed = 0

def mi1_app(event=True) :

    piano.itemconfigure(MI1, fill='red')
    print("down")

    global mi1_isPressed
    if mi1_isPressed < 1 :
        global mi1_joue
        mi1_joue = mi1_note.play()
        print("playing")

    mi1_isPressed += 1
    print(mi1_isPressed)

def mi1_rel(event=True) :

    piano.itemconfigure(MI1, fill='white')
    print("up")

    global mi1_joue
    mi1_joue.stop()
    global mi1_isPressed
    mi1_isPressed = 0


    # FA - Octave 1
fa1_note = sa.WaveObject.from_wave_file("Notes/FA1.wav")
fa1_isPressed = 0

def fa1_app(event=True) :

    piano.itemconfigure(FA1, fill='red')
    print("down")

    global fa1_isPressed
    if fa1_isPressed < 1 :
        global fa1_joue
        fa1_joue = fa1_note.play()
        print("playing")

    fa1_isPressed += 1
    print(fa1_isPressed)

def fa1_rel(event=True) :

    piano.itemconfigure(FA1, fill='white')
    print("up")

    global fa1_joue
    fa1_joue.stop()
    global fa1_isPressed
    fa1_isPressed = 0


    # SOL - Octave 1
sol1_note = sa.WaveObject.from_wave_file("Notes/SOL1.wav")
sol1_isPressed = 0

def sol1_app(event=True) :

    piano.itemconfigure(SOL1, fill='red')
    print("down")

    global sol1_isPressed
    if sol1_isPressed < 1 :
        global sol1_joue
        sol1_joue = sol1_note.play()
        print("playing")

    sol1_isPressed += 1
    print(sol1_isPressed)

def sol1_rel(event=True) :

    piano.itemconfigure(SOL1, fill='white')
    print("up")

    global sol1_joue
    sol1_joue.stop()
    global sol1_isPressed
    sol1_isPressed = 0


    # LA - Octave 1
la1_note = sa.WaveObject.from_wave_file("Notes/LA1.wav")
la1_isPressed = 0

def la1_app(event=True) :

    piano.itemconfigure(LA1, fill='red')
    print("down")

    global la1_isPressed
    if la1_isPressed < 1 :
        global la1_joue
        la1_joue = la1_note.play()
        print("playing")

    la1_isPressed += 1
    print(la1_isPressed)

def la1_rel(event=True) :

    piano.itemconfigure(LA1, fill='white')
    print("up")

    time.sleep(0.1)
    global la1_joue
    la1_joue.stop()
    global la1_isPressed
    la1_isPressed = 0


    # SI - Octave 1
si1_note = sa.WaveObject.from_wave_file("Notes/SI1.wav")
si1_isPressed = 0

def si1_app(event=True) :

    piano.itemconfigure(SI1, fill='red')
    print("down")

    global si1_isPressed
    if si1_isPressed < 1 :
        global si1_joue
        si1_joue = si1_note.play()
        print("playing")

    si1_isPressed += 1
    print(si1_isPressed)

def si1_rel(event=True) :

    piano.itemconfigure(SI1, fill='white')
    print("up")

    global si1_joue
    si1_joue.stop()
    global si1_isPressed
    si1_isPressed = 0


    # DO# - Octave 1
do1_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
do1_n_isPressed = 0

def do1_n_app(event=True) :

    piano.itemconfigure(DO1_n, fill='red')
    print("down")

    global do1_n_isPressed
    if do1_n_isPressed < 1 :
        global do1_n_joue
        do1_n_joue = do1_n_note.play()
        print("playing")

    do1_n_isPressed += 1
    print(do1_n_isPressed)

def do1_n_rel(event=True) :

    piano.itemconfigure(DO1_n, fill='black')
    print("up")

    global do1_n_joue
    do1_n_joue.stop()
    global do1_n_isPressed
    do1_n_isPressed = 0


    # RE# - Octave 1
re1_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
re1_n_isPressed = 0

def re1_n_app(event=True) :

    piano.itemconfigure(RE1_n, fill='red')
    print("down")

    global re1_n_isPressed
    if re1_n_isPressed < 1 :
        global re1_n_joue
        re1_n_joue = re1_n_note.play()
        print("playing")

    re1_n_isPressed += 1
    print(re1_n_isPressed)

def re1_n_rel(event=True) :

    piano.itemconfigure(RE1_n, fill='black')
    print("up")

    global re1_n_joue
    re1_n_joue.stop()
    global re1_n_isPressed
    re1_n_isPressed = 0


    # FA# - Octave 1
fa1_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
fa1_n_isPressed = 0

def fa1_n_app(event=True) :

    piano.itemconfigure(FA1_n, fill='red')
    print("down")

    global fa1_n_isPressed
    if fa1_n_isPressed < 1 :
        global fa1_n_joue
        fa1_n_joue = fa1_n_note.play()
        print("playing")

    fa1_n_isPressed += 1
    print(fa1_n_isPressed)

def fa1_n_rel(event=True) :

    piano.itemconfigure(FA1_n, fill='black')
    print("up")

    global fa1_n_joue
    fa1_n_joue.stop()
    global fa1_n_isPressed
    fa1_n_isPressed = 0


    # SOL# - Octave 1
sol1_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
sol1_n_isPressed = 0

def sol1_n_app(event=True) :

    piano.itemconfigure(SOL1_n, fill='red')
    print("down")

    global sol1_n_isPressed
    if sol1_n_isPressed < 1 :
        global sol1_n_joue
        sol1_n_joue = sol1_n_note.play()
        print("playing")

    sol1_n_isPressed += 1
    print(sol1_n_isPressed)

def sol1_n_rel(event=True) :

    piano.itemconfigure(SOL1_n, fill='black')
    print("up")

    global sol1_n_joue
    sol1_n_joue.stop()
    global sol1_n_isPressed
    sol1_n_isPressed = 0


    # LA# - Octave 1
la1_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
la1_n_isPressed = 0

def la1_n_app(event=True) :

    piano.itemconfigure(LA1_n, fill='red')
    print("down")

    global la1_n_isPressed
    if la1_n_isPressed < 1 :
        global la1_n_joue
        la1_n_joue = la1_n_note.play()
        print("playing")

    la1_n_isPressed += 1
    print(la1_n_isPressed)

def la1_n_rel(event=True) :

    piano.itemconfigure(LA1_n, fill='black')
    print("up")

    global la1_n_joue
    la1_n_joue.stop()
    global la1_n_isPressed
    la1_n_isPressed = 0


    # DO - Octave 2
do2_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
do2_isPressed = 0

def do2_app(event=True) :

    piano.itemconfigure(DO2, fill='red')
    print("down")

    global do2_isPressed
    if do2_isPressed < 1 :
        global do2_joue
        do2_joue = do2_note.play()
        print("playing")

    do2_isPressed += 1
    print(do1_isPressed)

def do2_rel(event=True) :

    piano.itemconfigure(DO2, fill='white')
    print("up")

    global do2_joue
    do2_joue.stop()
    global do2_isPressed
    do2_isPressed = 0


    # RE - Octave 2
re2_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
re2_isPressed = 0

def re2_app(event=True) :

    piano.itemconfigure(RE2, fill='red')
    print("down")

    global re2_isPressed
    if re2_isPressed < 1 :
        global re2_joue
        re2_joue = re2_note.play()
        print("playing")

    re2_isPressed += 1
    print(re2_isPressed)

def re2_rel(event=True) :

    piano.itemconfigure(RE2, fill='white')
    print("up")

    global re2_joue
    re2_joue.stop()
    global re2_isPressed
    re2_isPressed = 0


    # MI - Octave 2
mi2_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
mi2_isPressed = 0

def mi2_app(event=True) :

    piano.itemconfigure(MI2, fill='red')
    print("down")

    global mi2_isPressed
    if mi2_isPressed < 1 :
        global mi2_joue
        mi2_joue = mi2_note.play()
        print("playing")

    mi2_isPressed += 1
    print(do1_isPressed)

def mi2_rel(event=True) :

    piano.itemconfigure(MI2, fill='white')
    print("up")

    global mi2_joue
    mi2_joue.stop()
    global mi2_isPressed
    mi2_isPressed = 0


    # FA - Octave 2
fa2_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
fa2_isPressed = 0

def fa2_app(event=True) :

    piano.itemconfigure(FA2, fill='red')
    print("down")

    global fa2_isPressed
    if fa2_isPressed < 1 :
        global fa2_joue
        fa2_joue = fa2_note.play()
        print("playing")

    fa2_isPressed += 1
    print(fa2_isPressed)

def fa2_rel(event=True) :

    piano.itemconfigure(FA2, fill='white')
    print("up")

    global fa2_joue
    fa2_joue.stop()
    global fa2_isPressed
    fa2_isPressed = 0


    # SOL - Octave 2
sol2_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
sol2_isPressed = 0

def sol2_app(event=True) :

    piano.itemconfigure(SOL2, fill='red')
    print("down")

    global sol2_isPressed
    if sol2_isPressed < 1 :
        global sol2_joue
        sol2_joue = sol2_note.play()
        print("playing")

    sol2_isPressed += 1
    print(sol2_isPressed)

def sol2_rel(event=True) :

    piano.itemconfigure(SOL2, fill='white')
    print("up")

    global sol2_joue
    sol2_joue.stop()
    global sol2_isPressed
    sol2_isPressed = 0


    # LA - Octave 2
la2_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
la2_isPressed = 0

def la2_app(event=True) :

    piano.itemconfigure(LA2, fill='red')
    print("down")

    global la2_isPressed
    if la2_isPressed < 1 :
        global la2_joue
        la2_joue = la2_note.play()
        print("playing")

    la2_isPressed += 1
    print(la2_isPressed)

def la2_rel(event=True) :

    piano.itemconfigure(LA2, fill='white')
    print("up")

    global la2_joue
    la2_joue.stop()
    global la2_isPressed
    la2_isPressed = 0


    # SI - Octave 2
si2_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
si2_isPressed = 0

def si2_app(event=True) :

    piano.itemconfigure(SI2, fill='red')
    print("down")

    global si2_isPressed
    if si2_isPressed < 1 :
        global si2_joue
        si2_joue = si2_note.play()
        print("playing")

    si2_isPressed += 1
    print(si2_isPressed)

def si2_rel(event=True) :

    piano.itemconfigure(SI2, fill='white')
    print("up")

    global si2_joue
    si2_joue.stop()
    global si2_isPressed
    si2_isPressed = 0


    # DO# - Octave 2
do2_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
do2_n_isPressed = 0

def do2_n_app(event=True) :

    piano.itemconfigure(DO2_n, fill='red')
    print("down")

    global do2_n_isPressed
    if do2_n_isPressed < 1 :
        global do2_n_joue
        do2_n_joue = do2_n_note.play()
        print("playing")

    do2_n_isPressed += 1
    print(do2_n_isPressed)

def do2_n_rel(event=True) :

    piano.itemconfigure(DO2_n, fill='black')
    print("up")

    global do2_n_joue
    do2_n_joue.stop()
    global do2_n_isPressed
    do2_n_isPressed = 0


    # RE# - Octave 2
re2_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
re2_n_isPressed = 0

def re2_n_app(event=True) :

    piano.itemconfigure(RE2_n, fill='red')
    print("down")

    global re2_n_isPressed
    if re2_n_isPressed < 1 :
        global re2_n_joue
        re2_n_joue = re2_n_note.play()
        print("playing")

    re2_n_isPressed += 1
    print(re2_n_isPressed)

def re2_n_rel(event=True) :

    piano.itemconfigure(RE2_n, fill='black')
    print("up")

    global re2_n_joue
    re2_n_joue.stop()
    global re2_n_isPressed
    re2_n_isPressed = 0


    # FA# - Octave 2
fa2_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
fa2_n_isPressed = 0

def fa2_n_app(event=True) :

    piano.itemconfigure(FA2_n, fill='red')
    print("down")

    global fa2_n_isPressed
    if fa2_n_isPressed < 1 :
        global fa2_n_joue
        fa2_n_joue = fa2_n_note.play()
        print("playing")

    fa2_n_isPressed += 1
    print(fa2_n_isPressed)

def fa2_n_rel(event=True) :

    piano.itemconfigure(FA2_n, fill='black')
    print("up")

    global fa2_n_joue
    fa2_n_joue.stop()
    global fa2_n_isPressed
    fa2_n_isPressed = 0


    # SOL# - Octave 2
sol2_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
sol2_n_isPressed = 0

def sol2_n_app(event=True) :

    piano.itemconfigure(SOL2_n, fill='red')
    print("down")

    global sol2_n_isPressed
    if sol2_n_isPressed < 1 :
        global sol2_n_joue
        sol2_n_joue = sol2_n_note.play()
        print("playing")

    sol2_n_isPressed += 1
    print(sol2_n_isPressed)

def sol2_n_rel(event=True) :

    piano.itemconfigure(SOL2_n, fill='black')
    print("up")

    global sol2_n_joue
    sol2_n_joue.stop()
    global sol2_n_isPressed
    sol2_n_isPressed = 0


    # LA# - Octave 2
la2_n_note = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")
la2_n_isPressed = 0

def la2_n_app(event=True) :

    piano.itemconfigure(LA2_n, fill='red')
    print("down")

    global la2_n_isPressed
    if la2_n_isPressed < 1 :
        global la2_n_joue
        la2_n_joue = la2_n_note.play()
        print("playing")

    la2_n_isPressed += 1
    print(la2_n_isPressed)

def la2_n_rel(event=True) :

    piano.itemconfigure(LA2_n, fill='black')
    print("up")

    global la2_n_joue
    la2_n_joue.stop()
    global la2_n_isPressed
    la2_n_isPressed = 0


# Création de la fonction permettant d'afficher l'aide

def aideFunc() :
    aideFen = Toplevel(fenetre)
    aideFen.title("Aide")
    aideFen.config(height=200, width=200)

# Création du menu

def test() :
    print("Test")

mainMenu = Menu(fenetre, tearoff=0, activebackground='red')
fenetre.config(menu=mainMenu)


menuEnregistrer = Menu(fenetre, tearoff=0, activebackground='red')
mainMenu.add_cascade(label="Fichier", menu=menuEnregistrer)

menuEnregistrer.add_command(label="Commencer l'enregistrement", command=test)
menuEnregistrer.add_command(label="Arrêter l'enregistrement", command=test)

menuFichier = Menu(fenetre, tearoff=0, activebackground='red')
menuEnregistrer.add_cascade(label="Parcourir les enregistrements", menu=menuFichier)

menuFichier.add_command(label="Jouer un enregistrement", command=test)
menuFichier.add_command(label="Supprimer un enregistrement", command=test)


mainMenu.add_command(label="Aide", command=aideFunc)


# menuMetronome = Menu(fenetre,tearoff=0, activeforeground='red')
# mainmenu.add_cascade(label= "Metronome", menu=menuMetronome)

# Création du piano
piano = Canvas(fenetre, height=fenetre.winfo_height()/2, width=fenetre.winfo_width(), bg='blue')
piano.pack(expand=True)


# Création de chaque touches indépendemment pour plus de contrôle
y, x = fenetre.winfo_height()/2, fenetre.winfo_width()/14
DO1 = piano.create_rectangle(0, 0, x, y, outline="black", fill="white", width=4)
RE1 = piano.create_rectangle(x, 0, 2 * x, y, outline="black", fill="white", width=4)
MI1 = piano.create_rectangle(2 * x, 0, 3 * x, y, outline="black", fill="white", width=4)
FA1 = piano.create_rectangle(3 * x, 0, 4 * x, y, outline="black", fill="white", width=4)
SOL1 = piano.create_rectangle(4 * x, 0, 5 * x, y, outline="black", fill="white", width=4)
LA1 = piano.create_rectangle(5 * x, 0, 6 * x, y, outline="black", fill="white", width=4)
SI1 = piano.create_rectangle(6 * x, 0, 7 * x, y, outline="black", fill="white", width=4)

DO1_n = piano.create_rectangle(x * 3/4, 0, x * 5/4, y * 2/3, outline="black", fill="black", width=4)
RE1_n = piano.create_rectangle(x * 7/4 , 0, x * 9/4, y * 2/3, outline="black", fill="black", width=4)
FA1_n = piano.create_rectangle(x * 15/4, 0, x * 17/4, y * 2/3, outline="black", fill="black", width=4)
SOL1_n = piano.create_rectangle(x * 19/4, 0, x * 21/4, y * 2/3, outline="black", fill="black", width=4)
LA1_n = piano.create_rectangle(x * 23/4, 0, x * 25/4, y * 2/3, outline="black", fill="black", width=4)

DO2 = piano.create_rectangle(7 * x, 0, 8 * x, y, outline="black", fill="white", width=4)
RE2 = piano.create_rectangle(8 * x, 0, 9 * x, y, outline="black", fill="white", width=4)
MI2 = piano.create_rectangle(9 * x, 0, 10 * x, y, outline="black", fill="white", width=4)
FA2 = piano.create_rectangle(10 * x, 0, 11 * x, y, outline="black", fill="white", width=4)
SOL2 = piano.create_rectangle(11 * x, 0, 12 * x, y, outline="black", fill="white", width=4)
LA2 = piano.create_rectangle(12 * x, 0, 13 * x, y, outline="black", fill="white", width=4)
SI2 = piano.create_rectangle(13 * x, 0, 14 * x, y, outline="black", fill="white", width=4)

DO2_n = piano.create_rectangle(x * 31/4, 0, x * 33/4, y * 2/3, outline="black", fill="black", width=4)
RE2_n = piano.create_rectangle(x * 35/4 , 0, x * 37/4, y * 2/3, outline="black", fill="black", width=4)
FA2_n = piano.create_rectangle(x * 43/4, 0, x * 45/4, y * 2/3, outline="black", fill="black", width=4)
SOL2_n = piano.create_rectangle(x * 47/4, 0, x * 49/4, y * 2/3, outline="black", fill="black", width=4)
LA2_n = piano.create_rectangle(x * 51/4, 0, x * 53/4, y * 2/3, outline="black", fill="black", width=4)

border = piano.create_rectangle(0,0,fenetre.winfo_width(),fenetre.winfo_height() / 2,outline="black",width=10)

# Bind des touches aux fonctions
fenetre.bind('<KeyPress-s>', do1_app)
fenetre.bind('<KeyRelease-s>', do1_rel)
fenetre.bind('<KeyPress-d>', re1_app)
fenetre.bind('<KeyRelease-d>', re1_rel)
fenetre.bind('<KeyPress-f>', mi1_app)
fenetre.bind('<KeyRelease-f>', mi1_rel)
fenetre.bind('<KeyPress-g>', fa1_app)
fenetre.bind('<KeyRelease-g>', fa1_rel)
fenetre.bind('<KeyPress-h>', sol1_app)
fenetre.bind('<KeyRelease-h>', sol1_rel)
fenetre.bind('<KeyPress-j>', la1_app)
fenetre.bind('<KeyRelease-j>', la1_rel)
fenetre.bind('<KeyPress-k>', si1_app)
fenetre.bind('<KeyRelease-k>', si1_rel)

fenetre.bind('<KeyPress-a>', do1_n_app)
fenetre.bind('<KeyRelease-a>', do1_n_rel)
fenetre.bind('<KeyPress-z>', re1_n_app)
fenetre.bind('<KeyRelease-z>', re1_n_rel)
fenetre.bind('<KeyPress-e>', fa1_n_app)
fenetre.bind('<KeyRelease-e>', fa1_n_rel)
fenetre.bind('<KeyPress-r>', sol1_n_app)
fenetre.bind('<KeyRelease-r>', sol1_n_rel)
fenetre.bind('<KeyPress-t>', la1_n_app)
fenetre.bind('<KeyRelease-t>', la1_n_rel)

fenetre.bind('<KeyPress-w>', do2_app)
fenetre.bind('<KeyRelease-w>', do2_rel)
fenetre.bind('<KeyPress-x>', re2_app)
fenetre.bind('<KeyRelease-x>', re2_rel)
fenetre.bind('<KeyPress-c>', mi2_app)
fenetre.bind('<KeyRelease-c>', mi2_rel)
fenetre.bind('<KeyPress-v>', fa2_app)
fenetre.bind('<KeyRelease-v>', fa2_rel)
fenetre.bind('<KeyPress-b>', sol2_app)
fenetre.bind('<KeyRelease-b>', sol2_rel)
fenetre.bind('<KeyPress-n>', la2_app)
fenetre.bind('<KeyRelease-n>', la2_rel)
fenetre.bind('<KeyPress-,>', si2_app)
fenetre.bind('<KeyRelease-,>', si2_rel)

fenetre.bind('<KeyPress-y>', do2_n_app)
fenetre.bind('<KeyRelease-y>', do2_n_rel)
fenetre.bind('<KeyPress-u>', re2_n_app)
fenetre.bind('<KeyRelease-u>', re2_n_rel)
fenetre.bind('<KeyPress-i>', fa2_n_app)
fenetre.bind('<KeyRelease-i>', fa2_n_rel)
fenetre.bind('<KeyPress-o>', sol2_n_app)
fenetre.bind('<KeyRelease-o>', sol2_n_rel)
fenetre.bind('<KeyPress-p>', la2_n_app)
fenetre.bind('<KeyRelease-p>', la2_n_rel)


fenetre.mainloop()