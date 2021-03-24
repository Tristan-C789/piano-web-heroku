# Import des modules nécessaires
from tkinter import *
from PIL import ImageTk, Image
import simpleaudio as sa
import time
import csv
import os

# Initialisation de la fenêtre
fenetre = Tk()
fenetre.title("Piano - 2021")
fenetre.geometry("1300x500")
fenetre.minsize(1200, 400)
icon = PhotoImage(file='piano.gif')
fenetre.tk.call('wm', 'iconphoto', fenetre._w, icon)


# Déclaration des fonctions

# Déclaration de la fonction permettant d'enregistrer

recordnb = 0
recording = False
def startRecording():
    global recording, recordnb, notif
    if recordnb < 1:
        recording = True
        menuEnregistrer.entryconfigure(0, state=DISABLED)
        menuEnregistrer.entryconfigure(1, state=NORMAL)
        with open('Enregistrements/tempName.csv', 'w', newline='') as file:
            global fieldnames
            fieldnames = ['id', 'note', 'startTime', 'endTime']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
        recordnb += 1
        global id
        id = 0
        notif = Label(fenetre, text="Enregistrement en cours...")
        notif.pack()
    else:
        pass


# Déclaration des fonctions permettant d'arrêter l'enregistrement
def infermable() :
    pass

def sauvegarderEnregistrement() :
    if fileName.get() == "tempName" :
        erreur = Label(save, text="Nom de fichier invalide", bg="red")
        erreur.pack(expand=True)
    else:
        fichierPath = 'Enregistrements/' + fileName.get() + '.csv'
        os.rename('Enregistrements/tempName.csv', fichierPath)
        save.destroy()

def stopRecording() :
    global recording, recordnb, notif, fileName, save
    notif.destroy()
    recording = False
    recordnb = 0
    menuEnregistrer.entryconfigure(0, state=NORMAL)
    menuEnregistrer.entryconfigure(1, state=DISABLED)
    save = Toplevel(fenetre)
    save.protocol("WM_DELETE_WINDOW", test)
    save.title("Sauvergarder")
    save.geometry("250x150")
    save.resizable(False, False)

    text = Label(save, text="Entrez le nom de l'enregistrement")
    text.pack(expand=True)

    fileName = Entry(save)
    fileName.pack(expand=True)

    sauvegarder = Button(save, text="Sauvegarder", command=sauvegarderEnregistrement)
    sauvegarder.pack(expand=True)


# Déclaration de la fonction permettant de parcourir les enregistrements

def creation(nomDuFichier, i) :
    nomDuFichier = [Label(frame, text=nomDuFichier), Button(frame, text="Jouer l'enregistrement"), Button(frame, text="Supprimer")]

    nomDuFichier[0].grid(column=0, row=i, padx = 10, pady = 10)
    nomDuFichier[1].grid(column=1, row=i, padx = 10, pady = 10)
    nomDuFichier[2].grid(column=2, row=i, padx = 10, pady = 10)


    Files.append({'file': nomFichiers[-1], 'play': nomDuFichier[1], 'delete': nomDuFichier[2]})

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


def parcours() :
    global frame, explorer
    explorer = Toplevel(fenetre)
    explorer.title("Parcourir")
    explorer.geometry("500x400")
    explorer.resizable(False, False)
    explorer.grab_set()

    # Permet de scroller
    canvas = Canvas(explorer, borderwidth=0, background="#ffffff")
    scrollbar = Scrollbar(explorer, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    frame = Frame(canvas, background="#ffffff")

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    global Files
    Files = []
    global nomFichiers
    nomFichiers = []
    path = os.getcwd() + "/Enregistrements"
    filename = ""
    if (os.listdir(path)) == [] :
        erreur = Label(canvas, text="Aucun enregistrement disponible")
        erreur.pack(expand=True)
    else:
        for e, files in enumerate(os.listdir(path)) :
            for i in files :
                if i == "." :
                    break
                else:
                    filename += i
            nomFichiers.append(filename)
            creation(filename, e)
            filename = ""

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

        global recording, id
        if recording == True :
            global dict_do1
            dict_do1 = {'id': id, 'note': 'do1', 'startTime': time.time(), 'endTime': ''}
            id += 1

    do1_isPressed += 1
    print(do1_isPressed)

def do1_rel(event=True) :

    piano.itemconfigure(DO1, fill='white')
    print("up")

    global do1_joue
    do1_joue.stop()
    global do1_isPressed
    do1_isPressed = 0

    global recording, dict_do1
    if recording == True :
        dict_do1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_do1)


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

        global recording, id
        if recording == True :
            global dict_re1
            dict_re1 = {'id': id, 'note': 're1', 'startTime': time.time(), 'endTime': ''}
            id += 1

    re1_isPressed += 1
    print(re1_isPressed)

def re1_rel(event=True) :

    piano.itemconfigure(RE1, fill='white')
    print("up")

    global re1_joue
    re1_joue.stop()
    global re1_isPressed
    re1_isPressed = 0

    global recording, dict_re1
    if recording == True:
        dict_re1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_re1)


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

        global recording, id
        if recording == True :
            global dict_mi1
            dict_mi1 = {'id': id, 'note': 'mi1', 'startTime': time.time(), 'endTime': ''}
            id += 1

    mi1_isPressed += 1
    print(mi1_isPressed)

def mi1_rel(event=True) :

    piano.itemconfigure(MI1, fill='white')
    print("up")

    global mi1_joue
    mi1_joue.stop()
    global mi1_isPressed
    mi1_isPressed = 0

    global recording, dict_mi1
    if recording == True:
        dict_mi1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_mi1)



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

        global recording, id
        if recording == True :
            global dict_fa1
            dict_fa1 = {'id': id, 'note': 'fa1', 'startTime': time.time(),'endTime': ''}
            id += 1

    fa1_isPressed += 1
    print(fa1_isPressed)

def fa1_rel(event=True) :

    piano.itemconfigure(FA1, fill='white')
    print("up")

    global fa1_joue
    fa1_joue.stop()
    global fa1_isPressed
    fa1_isPressed = 0

    global recording, dict_fa1
    if recording == True:
        dict_fa1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_fa1)



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

        global recording, id
        if recording == True :
            global dict_sol1
            dict_sol1 = {'id': id, 'note': 'sol1', 'startTime': time.time(),'endTime': ''}
            id += 1

    sol1_isPressed += 1
    print(sol1_isPressed)

def sol1_rel(event=True) :

    piano.itemconfigure(SOL1, fill='white')
    print("up")

    global sol1_joue
    sol1_joue.stop()
    global sol1_isPressed
    sol1_isPressed = 0

    global recording, dict_sol1
    if recording == True:
        dict_sol1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_sol1)



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

        global recording, id
        if recording == True :
            global dict_la1
            dict_la1 = {'id': id, 'note': 'la1', 'startTime': time.time(), 'endTime': ''}
            id += 1

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

    global recording, dict_la1
    if recording == True:
        dict_la1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_la1)



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

        global recording, id
        if recording == True :
            global dict_si1
            dict_si1 = {'id': id, 'note': 'si1', 'startTime': time.time(), 'endTime': ''}
            id += 1

    si1_isPressed += 1
    print(si1_isPressed)

def si1_rel(event=True) :

    piano.itemconfigure(SI1, fill='white')
    print("up")

    global si1_joue
    si1_joue.stop()
    global si1_isPressed
    si1_isPressed = 0

    global recording, dict_si1
    if recording == True:
        dict_si1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_si1)



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

        global recording, id
        if recording == True :
            global dict_do_n1
            dict_do_n1 = {'id': id, 'note': 'do_n1', 'startTime': time.time(), 'endTime': ''}
            id += 1


    do1_n_isPressed += 1
    print(do1_n_isPressed)

def do1_n_rel(event=True) :

    piano.itemconfigure(DO1_n, fill='black')
    print("up")

    global do1_n_joue
    do1_n_joue.stop()
    global do1_n_isPressed
    do1_n_isPressed = 0

    global recording, dict_do_n1
    if recording == True:
        dict_do_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_do_n1)



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

        global recording, id
        if recording == True :
            global dict_re_n1
            dict_re_n1 = {'id': id, 'note': 're_n1', 'startTime': time.time(), 'endTime': ''}
            id += 1


    re1_n_isPressed += 1
    print(re1_n_isPressed)

def re1_n_rel(event=True) :

    piano.itemconfigure(RE1_n, fill='black')
    print("up")

    global re1_n_joue
    re1_n_joue.stop()
    global re1_n_isPressed
    re1_n_isPressed = 0

    global recording, dict_re_n1
    if recording == True:
        dict_re_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_re_n1)


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

        global recording, id
        if recording == True :
            global dict_fa_n1
            dict_fa_n1 = {'id': id, 'note': 'fa_n1', 'startTime': time.time(), 'endTime': ''}
            id += 1


    fa1_n_isPressed += 1
    print(fa1_n_isPressed)

def fa1_n_rel(event=True) :

    piano.itemconfigure(FA1_n, fill='black')
    print("up")

    global fa1_n_joue
    fa1_n_joue.stop()
    global fa1_n_isPressed
    fa1_n_isPressed = 0

    global recording, dict_fa_n1
    if recording == True:
        dict_fa_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_fa_n1)


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

        global recording, id
        if recording == True :
            global dict_sol_n1
            dict_sol_n1 = {'id': id, 'note': 'sol_n1', 'startTime': time.time(), 'endTime': ''}
            id += 1


    sol1_n_isPressed += 1
    print(sol1_n_isPressed)

def sol1_n_rel(event=True) :

    piano.itemconfigure(SOL1_n, fill='black')
    print("up")

    global sol1_n_joue
    sol1_n_joue.stop()
    global sol1_n_isPressed
    sol1_n_isPressed = 0

    global recording, dict_sol_n1
    if recording == True:
        dict_sol_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_sol_n1)


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

        global recording, id
        if recording == True :
            global dict_la_n1
            dict_la_n1 = {'id': id, 'note': 'la_n1', 'startTime': time.time(), 'endTime': ''}
            id += 1


    la1_n_isPressed += 1
    print(la1_n_isPressed)

def la1_n_rel(event=True) :

    piano.itemconfigure(LA1_n, fill='black')
    print("up")

    global la1_n_joue
    la1_n_joue.stop()
    global la1_n_isPressed
    la1_n_isPressed = 0

    global recording, dict_la_n1
    if recording == True:
        dict_la_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_la_n1)


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

        global recording, id
        if recording == True :
            global dict_do2
            dict_do2 = {'id': id, 'note': 'do2', 'startTime': time.time(),'endTime': ''}
            id += 1

    do2_isPressed += 1
    print(do1_isPressed)

def do2_rel(event=True) :

    piano.itemconfigure(DO2, fill='white')
    print("up")

    global do2_joue
    do2_joue.stop()
    global do2_isPressed
    do2_isPressed = 0

    global recording, dict_do2
    if recording == True:
        dict_do2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_do2)


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

        global recording, id
        if recording == True :
            global dict_re2
            dict_re2 = {'id': id, 'note': 're2', 'startTime': time.time(),'endTime': ''}
            id += 1

    re2_isPressed += 1
    print(re2_isPressed)

def re2_rel(event=True) :

    piano.itemconfigure(RE2, fill='white')
    print("up")

    global re2_joue
    re2_joue.stop()
    global re2_isPressed
    re2_isPressed = 0

    global recording, dict_re2
    if recording == True:
        dict_re2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_re2)


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

        global recording, id
        if recording == True :
            global dict_mi2
            dict_mi2 = {'id': id, 'note': 'mi2', 'startTime': time.time(),'endTime': ''}
            id += 1

    mi2_isPressed += 1
    print(do1_isPressed)

def mi2_rel(event=True) :

    piano.itemconfigure(MI2, fill='white')
    print("up")

    global mi2_joue
    mi2_joue.stop()
    global mi2_isPressed
    mi2_isPressed = 0

    global recording, dict_mi2
    if recording == True:
        dict_mi2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_mi2)


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

        global recording, id
        if recording == True :
            global dict_fa2
            dict_fa2 = {'id': id, 'note': 'fa2', 'startTime': time.time(),'endTime': ''}
            id += 1

    fa2_isPressed += 1
    print(fa2_isPressed)

def fa2_rel(event=True) :

    piano.itemconfigure(FA2, fill='white')
    print("up")

    global fa2_joue
    fa2_joue.stop()
    global fa2_isPressed
    fa2_isPressed = 0

    global recording, dict_fa2
    if recording == True:
        dict_fa2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_fa2)


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

        global recording, id
        if recording == True :
            global dict_sol2
            dict_sol2 = {'id': id, 'note': 'sol2', 'startTime': time.time(),'endTime': ''}
            id += 1

    sol2_isPressed += 1
    print(sol2_isPressed)

def sol2_rel(event=True) :

    piano.itemconfigure(SOL2, fill='white')
    print("up")

    global sol2_joue
    sol2_joue.stop()
    global sol2_isPressed
    sol2_isPressed = 0

    global recording, dict_sol2
    if recording == True:
        dict_sol2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_sol2)


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

        global recording, id
        if recording == True :
            global dict_la2
            dict_la2 = {'id': id, 'note': 'la2', 'startTime': time.time(),'endTime': ''}
            id += 1

    la2_isPressed += 1
    print(la2_isPressed)

def la2_rel(event=True) :

    piano.itemconfigure(LA2, fill='white')
    print("up")

    global la2_joue
    la2_joue.stop()
    global la2_isPressed
    la2_isPressed = 0

    global recording, dict_la2
    if recording == True:
        dict_la2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_la2)


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

        global recording, id
        if recording == True :
            global dict_si2
            dict_si2 = {'id': id, 'note': 'si2', 'startTime': time.time(),'endTime': ''}
            id += 1

    si2_isPressed += 1
    print(si2_isPressed)

def si2_rel(event=True) :

    piano.itemconfigure(SI2, fill='white')
    print("up")

    global si2_joue
    si2_joue.stop()
    global si2_isPressed
    si2_isPressed = 0

    global recording, dict_si2
    if recording == True:
        dict_si2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_si2)


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

        global recording, id
        if recording == True :
            global dict_do_n2
            dict_do_n2 = {'id': id, 'note': 'do_n2', 'startTime': time.time(), 'endTime': ''}
            id += 1

    do2_n_isPressed += 1
    print(do2_n_isPressed)

def do2_n_rel(event=True) :

    piano.itemconfigure(DO2_n, fill='black')
    print("up")

    global do2_n_joue
    do2_n_joue.stop()
    global do2_n_isPressed
    do2_n_isPressed = 0

    global recording, dict_do_n2
    if recording == True:
        dict_do_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_do_n2)


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

        global recording, id
        if recording == True :
            global dict_re_n2
            dict_re_n2 = {'id': id, 'note': 're_n2', 'startTime': time.time(), 'endTime': ''}
            id += 1

    re2_n_isPressed += 1
    print(re2_n_isPressed)

def re2_n_rel(event=True) :

    piano.itemconfigure(RE2_n, fill='black')
    print("up")

    global re2_n_joue
    re2_n_joue.stop()
    global re2_n_isPressed
    re2_n_isPressed = 0

    global recording, dict_re_n2
    if recording == True:
        dict_re_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_re_n2)


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

        global recording, id
        if recording == True :
            global dict_fa_n2
            dict_fa_n2 = {'id': id, 'note': 'fa_n2', 'startTime': time.time(), 'endTime': ''}
            id += 1

    fa2_n_isPressed += 1
    print(fa2_n_isPressed)

def fa2_n_rel(event=True) :

    piano.itemconfigure(FA2_n, fill='black')
    print("up")

    global fa2_n_joue
    fa2_n_joue.stop()
    global fa2_n_isPressed
    fa2_n_isPressed = 0

    global recording, dict_fa_n2
    if recording == True:
        dict_fa_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_fa_n2)


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

        global recording, id
        if recording == True :
            global dict_sol_n2
            dict_sol_n2 = {'id': id, 'note': 'sol_n2', 'startTime': time.time(), 'endTime': ''}
            id += 1

    sol2_n_isPressed += 1
    print(sol2_n_isPressed)

def sol2_n_rel(event=True) :

    piano.itemconfigure(SOL2_n, fill='black')
    print("up")

    global sol2_n_joue
    sol2_n_joue.stop()
    global sol2_n_isPressed
    sol2_n_isPressed = 0

    global recording, dict_sol_n2
    if recording == True:
        dict_sol_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_sol_n2)


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

        global recording, id
        if recording == True :
            global dict_la_n2
            dict_la_n2 = {'id': id, 'note': 'la_n2', 'startTime': time.time(), 'endTime': ''}
            id += 1

    la2_n_isPressed += 1
    print(la2_n_isPressed)

def la2_n_rel(event=True) :

    piano.itemconfigure(LA2_n, fill='black')
    print("up")

    global la2_n_joue
    la2_n_joue.stop()
    global la2_n_isPressed
    la2_n_isPressed = 0

    global recording, dict_la_n2
    if recording == True:
        dict_la_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(dict_la_n2)



# Création du piano
piano = Canvas(fenetre, height=fenetre.winfo_height()/1.5, width=fenetre.winfo_width(), bg='blue')
piano.pack(expand=True)


# Création de chaque touches indépendemment pour plus de contrôle
y, x = fenetre.winfo_height()/1.5, fenetre.winfo_width()/14

# Création de la fonction permettant d'afficher l'aide

aideActive = False
def aideFunc() :
    global aideActive, A, Z, E, R, T, Y, U, I, O, P, S, D, F, G, H, J, K, W, X, C, V, B, N, comma
    if aideActive == False :
        A = piano.create_text(x, y/2, text="A", fill="white", font=("Helvetica", 18))
        Z = piano.create_text(x*2, y/2, text="Z", fill="white", font=("Helvetica", 18))
        E = piano.create_text(x*4, y/2, text="E", fill="white", font=("Helvetica", 18))
        R = piano.create_text(x*5, y/2, text="R", fill="white", font=("Helvetica", 18))
        T = piano.create_text(x*6, y/2, text="T", fill="white", font=("Helvetica", 18))
        Y = piano.create_text(x*8, y/2, text="Y", fill="white", font=("Helvetica", 18))
        U = piano.create_text(x*9, y/2, text="U", fill="white", font=("Helvetica", 18))
        I = piano.create_text(x*11, y/2, text="I", fill="white", font=("Helvetica", 18))
        O = piano.create_text(x*12, y/2, text="O", fill="white", font=("Helvetica", 18))
        P = piano.create_text(x*13, y/2, text="P", fill="white", font=("Helvetica", 18))

        S = piano.create_text(x*1/2, y*3/4, text="S", fill="black", font=("Helvetica", 18))
        D = piano.create_text(x*3/2, y*3/4, text="D", fill="black", font=("Helvetica", 18))
        F = piano.create_text(x*5/2, y*3/4, text="F", fill="black", font=("Helvetica", 18))
        G = piano.create_text(x*7/2, y*3/4, text="G", fill="black", font=("Helvetica", 18))
        H = piano.create_text(x*9/2, y*3/4, text="H", fill="black", font=("Helvetica", 18))
        J = piano.create_text(x*11/2, y*3/4, text="J", fill="black", font=("Helvetica", 18))
        K = piano.create_text(x*13/2, y*3/4, text="K", fill="black", font=("Helvetica", 18))

        W = piano.create_text(x*15/2, y*3/4, text="W", fill="black", font=("Helvetica", 18))
        X = piano.create_text(x*17/2, y*3/4, text="X", fill="black", font=("Helvetica", 18))
        C = piano.create_text(x*19/2, y*3/4, text="C", fill="black", font=("Helvetica", 18))
        V = piano.create_text(x*21/2, y*3/4, text="V", fill="black", font=("Helvetica", 18))
        B = piano.create_text(x*23/2, y*3/4, text="B", fill="black", font=("Helvetica", 18))
        N = piano.create_text(x*25/2, y*3/4, text="N", fill="black", font=("Helvetica", 18))
        comma = piano.create_text(x*27/2, y*3/4, text=",", fill="black", font=("Helvetica", 18))

        aideActive = True

    else:
        piano.delete(A)
        piano.delete(Z)
        piano.delete(E)
        piano.delete(R)
        piano.delete(T)
        piano.delete(Y)
        piano.delete(U)
        piano.delete(I)
        piano.delete(O)
        piano.delete(P)

        piano.delete(S)
        piano.delete(D)
        piano.delete(F)
        piano.delete(G)
        piano.delete(H)
        piano.delete(J)
        piano.delete(K)

        piano.delete(W)
        piano.delete(X)
        piano.delete(C)
        piano.delete(V)
        piano.delete(B)
        piano.delete(N)
        piano.delete(comma)

        aideActive = False


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

border = piano.create_rectangle(0,0,fenetre.winfo_width(),fenetre.winfo_height() / 1.5,outline="black",width=10)

# Création du menu

def test() :
    print("Test")

mainMenu = Menu(fenetre, tearoff=0, activebackground='red')
fenetre.config(menu=mainMenu)


menuEnregistrer = Menu(fenetre, tearoff=0, activebackground='red')
mainMenu.add_cascade(label="Fichier", menu=menuEnregistrer)

menuEnregistrer.add_command(label="Commencer l'enregistrement", command=startRecording)
menuEnregistrer.add_command(label="Arrêter l'enregistrement", command=stopRecording)
menuEnregistrer.entryconfigure(1, state=DISABLED)
menuEnregistrer.add_command(label="Parcourir les enregistrements", command=parcours)


mainMenu.add_command(label="Aide", command=aideFunc)


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