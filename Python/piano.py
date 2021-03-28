# Import des modules nécessaires
from tkinter import *
from tkinter import ttk
import simpleaudio as sa, time, csv, os

# Déclaration des variables correspondant à chaque fichier son
do1_note = sa.WaveObject.from_wave_file("Notes/Do 1.wav")
re1_note = sa.WaveObject.from_wave_file("Notes/Re 1.wav")
mi1_note = sa.WaveObject.from_wave_file("Notes/Mi 1.wav")
fa1_note = sa.WaveObject.from_wave_file("Notes/Fa 1.wav")
sol1_note = sa.WaveObject.from_wave_file("Notes/Sol 1.wav")
la1_note = sa.WaveObject.from_wave_file("Notes/La 1.wav")
la1_note = sa.WaveObject.from_wave_file("Notes/La 1.wav")
si1_note = sa.WaveObject.from_wave_file("Notes/Si 1.wav")

do1_n_note = sa.WaveObject.from_wave_file("Notes/Do dièse 1.wav")
re1_n_note = sa.WaveObject.from_wave_file("Notes/Re dièse 1.wav")
fa1_n_note = sa.WaveObject.from_wave_file("Notes/Fa dièse 1.wav")
sol1_n_note = sa.WaveObject.from_wave_file("Notes/Sol dièse 1.wav")
la1_n_note = sa.WaveObject.from_wave_file("Notes/La dièse 1.wav")

do2_note = sa.WaveObject.from_wave_file("Notes/Do 2.wav")
re2_note = sa.WaveObject.from_wave_file("Notes/Re 2.wav")
mi2_note = sa.WaveObject.from_wave_file("Notes/Mi 2.wav")
fa2_note = sa.WaveObject.from_wave_file("Notes/Fa 2.wav")
sol2_note = sa.WaveObject.from_wave_file("Notes/Sol 2.wav")
la2_note = sa.WaveObject.from_wave_file("Notes/La 2.wav")
si2_note = sa.WaveObject.from_wave_file("Notes/Si 2.wav")

do2_n_note = sa.WaveObject.from_wave_file("Notes/Do dièse 2.wav")
re2_n_note = sa.WaveObject.from_wave_file("Notes/Re dièse 2.wav")
fa2_n_note = sa.WaveObject.from_wave_file("Notes/Fa dièse 2.wav")
sol2_n_note = sa.WaveObject.from_wave_file("Notes/Sol dièse 2.wav")
la2_n_note = sa.WaveObject.from_wave_file("Notes/La dièse 2.wav")

# Initialisation de la fenêtre
fenetre = Tk()
fenetre.title("Piano - 2021")
fenetre.geometry("1300x500")
fenetre.minsize(1200, 500)
icon = PhotoImage(file='piano.gif')
fenetre.tk.call('wm', 'iconphoto', fenetre._w, icon)

# --- Déclaration des fonctions ---

# Déclaration de la fonction permettant d'enregistrer

recordnb = 0
recording = False

if not os.path.exists("Enregistrements") :
    print("Dossier manquant, création en cours...")
    os.mkdir('Enregistrements')
        
def startRecording():
    try:
        os.makedirs(os.getcwd() + "/Enregistrements")
    except FileExistsError:
        pass
    global recording, recordnb
    if recordnb < 1:
        recording = True
        print("Enregistrement débuté")
        menuEnregistrer.entryconfigure(0, state=DISABLED)
        menuEnregistrer.entryconfigure(1, state=NORMAL)
        recordnb += 1
        with open('Enregistrements/tempName.csv', 'w', newline='') as file:
            global clefs
            clefs = ['note', 'startTime', 'endTime']
            writer = csv.writer(file)
            writer.writerow(clefs)
        global notif
        notif = Label(fenetre, text="Enregistrement en cours...")
        notif.pack()
    else:
        pass


# Déclaration des fonctions permettant d'arrêter l'enregistrement
def infermable():
    pass


def sauvegarderEnregistrement():
    if fileName.get() == "tempName":
        erreur = Label(save, text="Nom de fichier invalide", bg="red")
        erreur.pack(expand=True)
    else:
        fichierPath = 'Enregistrements/' + fileName.get() + '.csv'
        os.rename('Enregistrements/tempName.csv', fichierPath)
        print("Fichier enregistré")
        save.destroy()


def stopRecording():
    global recording, recordnb, notif, fileName, save
    notif.destroy()
    recording = False
    print("Fin de l'enregistrement")
    recordnb = 0
    menuEnregistrer.entryconfigure(0, state=NORMAL)
    menuEnregistrer.entryconfigure(1, state=DISABLED)
    save = Toplevel(fenetre)
    save.protocol("WM_DELETE_WINDOW", infermable)
    save.title("Sauvergarder")
    save.geometry("250x150")
    save.resizable(False, False)

    text = Label(save, text="Entrez le nom de l'enregistrement")
    text.pack(expand=True)

    fileName = Entry(save)
    fileName.pack(expand=True)

    sauvegarder = Button(save,
                         text="Sauvegarder",
                         command=sauvegarderEnregistrement)
    sauvegarder.pack(expand=True)


# Déclaration de la fonction permettant de supprimer un fichier
def suppr(fichier):
    path = os.getcwd() + '\Enregistrements\\' + fichier + ".csv"
    os.remove(path)
    for i in Files:
        if i["file"] == fichier:
            i["label"].destroy()
            i["play"].destroy()
            i["delete"].destroy()
            print("Enregistrement", fichier, "supprimé")


# Déclaration de la fonction permettant de jouer les morceaux
def play(fichier):
    global isPlaying
    isPlaying = True
    path = os.getcwd() + '\Enregistrements\\' + fichier + ".csv"
    morceaux = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            morceaux.append(ligne)
    print(len(morceaux), morceaux)
    maxEndTime = 0
    maxEndTimeNb = 0
    for i, notes in enumerate(morceaux):
        if float(notes["endTime"]) > float(maxEndTime):
            maxEndTime = notes["endTime"]
            maxEndTimeNb = i

    duration = round((float(morceaux[maxEndTimeNb]["endTime"]) -
                      float(morceaux[0]["startTime"])), 2)
    print("Durée de l'enregistrement :", round(duration, 2),
          "secondes\nDébut de l'écoute de l'enregistrement...")
    start = time.time() + 1 # Le + 1 permet d'éviter beaucoup de bug - aussi responsable du petit silence en début de replay
    do1rec = 0
    re1rec = 0
    mi1rec = 0
    fa1rec = 0
    sol1rec = 0
    la1rec = 0
    si1rec = 0

    do1Nrec = 0
    re1Nrec = 0
    fa1Nrec = 0
    sol1Nrec = 0
    la1Nrec = 0

    do2rec = 0
    re2rec = 0
    mi2rec = 0
    fa2rec = 0
    sol2rec = 0
    la2rec = 0
    si2rec = 0

    do2Nrec = 0
    re2Nrec = 0
    fa2Nrec = 0
    sol2Nrec = 0
    la2Nrec = 0

    whatsPlaying = fichier + " est en train de jouer"
    canvas.destroy()
    playing = Label(explorer, text=whatsPlaying)
    playing.pack(expand=True)
    playing.config(font=("Bahnschrift", 13))

    info = Label(
        explorer,
        text=
        "Fermez la fenêtre pour arrêter le replay. La fenêtre sera automatiquement fermée à la fin du replay."
    )
    info.pack(side=BOTTOM)
    info.config(font=("Roboto", 8))

    progress = ttk.Progressbar(explorer,
                               orient=HORIZONTAL,
                               mode="determinate",
                               length=300)
    progress.pack(expand=True)
    times = 0.01
    i = 0
    while time.time() < (start + duration):
        i+=1
        fenetre.update()
        if time.time() > (start + (times * duration)):
            times += 0.01
            progress.step(times * 2)

        if isPlaying == False:
            break
        for notes in morceaux:
            a = round((
                (float(notes["startTime"]) - float(morceaux[0]["startTime"])) +
                start), 1)
            # La somme entre la différence entre t(début absolu de la note enregistrée) et t(début absolu de la première note jouée), et t(début du replay)
            b = round(time.time(), 1)
            # Temps actuel
            c = round(
                ((float(notes["endTime"]) - float(morceaux[0]["startTime"])) +
                 start), 1)
            # La somme entre la différence entre t(fin absolue de la note enregistrée) et t(début absolu de la première note jouée), et t(début du replay)

            if a == b:  # ==> Permet de déterminer si le temps actuel correspond à un début de note

                # Détermine quelle touche est jouée et si elle est déjà en train d'être jouée

                # Première Octave
                if notes["note"] == "do1":
                    if do1rec < 1:
                        do1rec_play = do1_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        do1rec += 1

                if notes["note"] == "re1":
                    if re1rec < 1:
                        re1rec_play = re1_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        re1rec += 1

                if notes["note"] == "mi1":
                    if mi1rec < 1:
                        mi1rec_play = mi1_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        mi1rec += 1

                if notes["note"] == "fa1":
                    if fa1rec < 1:
                        fa1rec_play = fa1_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        fa1rec += 1

                if notes["note"] == "sol1":
                    if sol1rec < 1:
                        sol1rec_play = sol1_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        sol1rec += 1

                if notes["note"] == "la1":
                    if la1rec < 1:
                        la1rec_play = la1_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        la1rec += 1

                if notes["note"] == "si1":
                    if si1rec < 1:
                        si1rec_play = si1_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        si1rec += 1

                # Première Octave - Dièse
                if notes["note"] == "do_n1":
                    if do1Nrec < 1:
                        do1Nrec_play = do1_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        do1Nrec += 1

                if notes["note"] == "re_n1":
                    if re1Nrec < 1:
                        re1Nrec_play = re1_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        re1Nrec += 1

                if notes["note"] == "fa_n1":
                    if fa1Nrec < 1:
                        fa1Nrec_play = fa1_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        fa1Nrec += 1

                if notes["note"] == "sol_n1":
                    if sol1Nrec < 1:
                        sol1Nrec_play = sol1_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        sol1Nrec += 1

                if notes["note"] == "la_n1":
                    if la1Nrec < 1:
                        la1Nrec_play = la1_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        la1Nrec += 1

                # Deuxième Octave
                if notes["note"] == "do2":
                    if do2rec < 1:
                        do2rec_play = do2_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        do2rec += 1

                if notes["note"] == "re2":
                    if re2rec < 1:
                        re2rec_play = re2_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        re2rec += 1

                if notes["note"] == "mi2":
                    if mi2rec < 1:
                        mi2rec_play = mi2_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        mi2rec += 1

                if notes["note"] == "fa2":
                    if fa2rec < 1:
                        fa2rec_play = fa2_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        fa2rec += 1

                if notes["note"] == "sol2":
                    if sol2rec < 1:
                        sol2rec_play = sol2_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        sol2rec += 1

                if notes["note"] == "la2":
                    if la2rec < 1:
                        la2rec_play = la2_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        la2rec += 1

                if notes["note"] == "si2":
                    if si2rec < 1:
                        si2rec_play = si2_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        si2rec += 1

                # Deuxième Octave - Dièse
                if notes["note"] == "do_n2":
                    if do2Nrec < 1:
                        do2Nrec_play = do2_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        do2Nrec += 1

                if notes["note"] == "re_n2":
                    if re2Nrec < 1:
                        re2Nrec_play = re2_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        re2Nrec += 1

                if notes["note"] == "fa_n2":
                    if fa2Nrec < 1:
                        fa2Nrec_play = fa2_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        fa2Nrec += 1

                if notes["note"] == "sol_n2":
                    if sol2Nrec < 1:
                        sol2Nrec_play = sol2_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        sol2Nrec += 1

                if notes["note"] == "la_n2":
                    if la2Nrec < 1:
                        la2Nrec_play = la2_n_note.play()
                        print(
                            "Note jouée :", notes["note"], "pendant",
                            round((float(notes["endTime"]) -
                                   float(notes["startTime"])), 2), "secondes")
                        la2Nrec += 1
            if c == b and i > 3:  # Vérification de s'il est temps de stopper une note

                # Première Octave
                if notes["note"] == "do1":
                    do1rec_play.stop()
                    do1rec = 0

                if notes["note"] == "re1":
                    re1rec_play.stop()
                    re1rec = 0

                if notes["note"] == "mi1":
                    mi1rec_play.stop()
                    mi1rec = 0

                if notes["note"] == "fa1":
                    fa1rec_play.stop()
                    fa1rec = 0

                if notes["note"] == "sol1":
                    sol1rec_play.stop()
                    sol1rec = 0

                if notes["note"] == "la1":
                    la1rec_play.stop()
                    la1rec = 0

                if notes["note"] == "si1":
                    si1rec_play.stop()
                    si1rec = 0

                # Première Octave - Dièse
                if notes["note"] == "do_n1":
                    do1Nrec_play.stop()
                    do1Nrec = 0

                if notes["note"] == "re_n1":
                    re1Nrec_play.stop()
                    re1Nrec = 0

                if notes["note"] == "fa_n1":
                    fa1Nrec_play.stop()
                    fa1Nrec = 0

                if notes["note"] == "sol_n1":
                    sol1Nrec_play.stop()
                    sol1Nrec = 0

                if notes["note"] == "la_n1":
                    la1Nrec_play.stop()
                    la1Nrec = 0

                # Deuxième Octave
                if notes["note"] == "do2":
                    do2rec_play.stop()
                    do2rec = 0

                if notes["note"] == "re2":
                    re2rec_play.stop()
                    re2rec = 0

                if notes["note"] == "mi2":
                    mi2rec_play.stop()
                    mi2rec = 0

                if notes["note"] == "fa2":
                    fa2rec_play.stop()
                    fa2rec = 0

                if notes["note"] == "sol2":
                    sol2rec_play.stop()
                    sol2rec = 0

                if notes["note"] == "la2":
                    la2rec_play.stop()
                    la2rec = 0

                if notes["note"] == "si2":
                    si2rec_play.stop()
                    si2rec = 0

                # Première Octave - Dièse
                if notes["note"] == "do_n2":
                    do2Nrec_play.stop()
                    do2Nrec = 0

                if notes["note"] == "re_n2":
                    re2Nrec_play.stop()
                    re2Nrec = 0

                if notes["note"] == "fa_n2":
                    fa2Nrec_play.stop()
                    fa2Nrec = 0

                if notes["note"] == "sol_n2":
                    sol2Nrec_play.stop()
                    sol2Nrec = 0

                if notes["note"] == "la_n2":
                    la2Nrec_play.stop()
                    la2Nrec = 0

    print("Enregistrement", fichier, "terminé")
    explorer.destroy()


# Déclaration de la fonction permettant de parcourir les enregistrements


def creation(nomDuFichier, i):
    nomReel = nomDuFichier
    nomDuFichier = [
        Label(frame, text=nomDuFichier),
        Button(frame,
               text="Jouer l'enregistrement",
               command=lambda: play(nomReel)),
        Button(frame, text="Supprimer", command=lambda: suppr(nomReel))
    ]

    nomDuFichier[0].grid(column=0, row=i, padx=10, pady=10)

    # Uniformisation de la longueur des Labels
    frame.update()
    print("Longueur originale du label", nomReel, ": ",
          nomDuFichier[0].winfo_width())
    while nomDuFichier[0].winfo_width() > 220:
        nomDuFichier[0].config(text=nomDuFichier[0].cget("text")[:-1])
        frame.update()
        if nomDuFichier[0].winfo_width() < 220:
            nomDuFichier[0].config(text=nomDuFichier[0].cget("text") + "...")
    while nomDuFichier[0].winfo_width() < 215:
        nomDuFichier[0].config(text=" " + nomDuFichier[0].cget("text") + " ")
        frame.update()
    print("Longueur finale du label", nomReel, ": ",
          nomDuFichier[0].winfo_width())

    nomDuFichier[1].grid(column=1, row=i, padx=10, pady=10)
    nomDuFichier[2].grid(column=2, row=i, padx=10, pady=10)
    print(nomReel, "chargé")

    Files.append({
        'file': nomFichiers[-1],
        'label': nomDuFichier[0],
        'play': nomDuFichier[1],
        'delete': nomDuFichier[2]
    })


def scrollable(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


def closeExplorer():
    global isPlaying
    isPlaying = False
    print("Explorer fermé")
    frame.update()
    explorer.destroy()


def parcourir():
    global frame, explorer, canvas
    explorer = Toplevel(fenetre)
    explorer.title("Parcourir")
    explorer.geometry("500x400")
    explorer.resizable(False, False)
    explorer.grab_set()
    explorer.protocol("WM_DELETE_WINDOW", closeExplorer)

    # Permet de scroller
    canvas = Canvas(explorer, borderwidth=0, background="#ffffff")
    scrollbar = Scrollbar(explorer, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    frame = Frame(canvas, background="#ffffff")

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: scrollable(canvas))

    global Files
    Files = []
    global nomFichiers
    nomFichiers = []
    path = os.getcwd() + "\\Enregistrements"
    filename = ""
    print(os.listdir(path))
    if (os.listdir(path)) == []:
        erreur = Label(canvas, text="Aucun enregistrement disponible")
        erreur.pack(expand=True)
    else:
        for e, files in enumerate(os.listdir(path)):
            for i in files:
                if i == ".":
                    break
                else:
                    filename += i
            nomFichiers.append(filename)
            creation(filename, e)
            filename = ""

    # DO - Octave 1


do1_isPressed = 0


def do1_app(event=True):

    piano.itemconfigure(DO1, fill='red')

    global do1_isPressed
    if do1_isPressed < 1:
        global do1_joue
        do1_joue = do1_note.play()
        print("DO1 appuyé")

        global recording
        if recording == True:
            global dict_do1
            dict_do1 = {'note': 'do1', 'startTime': time.time(), 'endTime': ''}

    do1_isPressed += 1


def do1_rel(event=True):

    piano.itemconfigure(DO1, fill='white')
    print("DO1 relevé")

    global do1_joue
    do1_joue.stop()
    global do1_isPressed
    do1_isPressed = 0

    global recording, dict_do1
    if recording == True:
        dict_do1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_do1)

    # RE - Octave 1


re1_isPressed = 0


def re1_app(event=True):

    piano.itemconfigure(RE1, fill='red')

    global re1_isPressed
    if re1_isPressed < 1:
        global re1_joue
        re1_joue = re1_note.play()
        print("RE1 appuyé")

        global recording
        if recording == True:
            global dict_re1
            dict_re1 = {'note': 're1', 'startTime': time.time(), 'endTime': ''}

    re1_isPressed += 1


def re1_rel(event=True):

    piano.itemconfigure(RE1, fill='white')
    print("RE1 relevé")

    global re1_joue
    re1_joue.stop()
    global re1_isPressed
    re1_isPressed = 0

    global recording, dict_re1
    if recording == True:
        dict_re1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_re1)

    # MI - Octave 1


mi1_isPressed = 0


def mi1_app(event=True):

    piano.itemconfigure(MI1, fill='red')

    global mi1_isPressed
    if mi1_isPressed < 1:
        global mi1_joue
        mi1_joue = mi1_note.play()
        print("MI1 appuyé")

        global recording
        if recording == True:
            global dict_mi1
            dict_mi1 = {'note': 'mi1', 'startTime': time.time(), 'endTime': ''}

    mi1_isPressed += 1


def mi1_rel(event=True):

    piano.itemconfigure(MI1, fill='white')
    print("MI1 relevé")

    global mi1_joue
    mi1_joue.stop()
    global mi1_isPressed
    mi1_isPressed = 0

    global recording, dict_mi1
    if recording == True:
        dict_mi1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_mi1)

    # FA - Octave 1


fa1_isPressed = 0


def fa1_app(event=True):

    piano.itemconfigure(FA1, fill='red')

    global fa1_isPressed
    if fa1_isPressed < 1:
        global fa1_joue
        fa1_joue = fa1_note.play()
        print("FA1 appuyé")

        global recording
        if recording == True:
            global dict_fa1
            dict_fa1 = {'note': 'fa1', 'startTime': time.time(), 'endTime': ''}

    fa1_isPressed += 1


def fa1_rel(event=True):

    piano.itemconfigure(FA1, fill='white')
    print("FA1 relevé")

    global fa1_joue
    fa1_joue.stop()
    global fa1_isPressed
    fa1_isPressed = 0

    global recording, dict_fa1
    if recording == True:
        dict_fa1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_fa1)

    # SOL - Octave 1


sol1_isPressed = 0


def sol1_app(event=True):

    piano.itemconfigure(SOL1, fill='red')

    global sol1_isPressed
    if sol1_isPressed < 1:
        global sol1_joue
        sol1_joue = sol1_note.play()
        print("SOL1 appuyé")

        global recording
        if recording == True:
            global dict_sol1
            dict_sol1 = {
                'note': 'sol1',
                'startTime': time.time(),
                'endTime': ''
            }

    sol1_isPressed += 1


def sol1_rel(event=True):

    piano.itemconfigure(SOL1, fill='white')
    print("SOL1 relevé")

    global sol1_joue
    sol1_joue.stop()
    global sol1_isPressed
    sol1_isPressed = 0

    global recording, dict_sol1
    if recording == True:
        dict_sol1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_sol1)

    # LA - Octave 1


la1_isPressed = 0


def la1_app(event=True):

    piano.itemconfigure(LA1, fill='red')

    global la1_isPressed
    if la1_isPressed < 1:
        global la1_joue
        la1_joue = la1_note.play()
        print("LA1 appuyé")

        global recording
        if recording == True:
            global dict_la1
            dict_la1 = {'note': 'la1', 'startTime': time.time(), 'endTime': ''}

    la1_isPressed += 1


def la1_rel(event=True):

    piano.itemconfigure(LA1, fill='white')
    print("LA1 relevé")

    time.sleep(0.1)
    global la1_joue
    la1_joue.stop()
    global la1_isPressed
    la1_isPressed = 0

    global recording, dict_la1
    if recording == True:
        dict_la1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_la1)

    # SI - Octave 1


si1_isPressed = 0


def si1_app(event=True):

    piano.itemconfigure(SI1, fill='red')

    global si1_isPressed
    if si1_isPressed < 1:
        global si1_joue
        si1_joue = si1_note.play()
        print("SI1 appuyé")

        global recording
        if recording == True:
            global dict_si1
            dict_si1 = {'note': 'si1', 'startTime': time.time(), 'endTime': ''}

    si1_isPressed += 1


def si1_rel(event=True):

    piano.itemconfigure(SI1, fill='white')
    print("SI1 relevé")

    global si1_joue
    si1_joue.stop()
    global si1_isPressed
    si1_isPressed = 0

    global recording, dict_si1
    if recording == True:
        dict_si1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_si1)

    # DO# - Octave 1


do1_n_isPressed = 0


def do1_n_app(event=True):

    piano.itemconfigure(DO1_n, fill='red')

    global do1_n_isPressed
    if do1_n_isPressed < 1:
        global do1_n_joue
        do1_n_joue = do1_n_note.play()
        print("DO1# appuyé")

        global recording
        if recording == True:
            global dict_do_n1
            dict_do_n1 = {
                'note': 'do_n1',
                'startTime': time.time(),
                'endTime': ''
            }

    do1_n_isPressed += 1


def do1_n_rel(event=True):

    piano.itemconfigure(DO1_n, fill='black')
    print("DO1# relevé")

    global do1_n_joue
    do1_n_joue.stop()
    global do1_n_isPressed
    do1_n_isPressed = 0

    global recording, dict_do_n1
    if recording == True:
        dict_do_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_do_n1)

    # RE# - Octave 1


re1_n_isPressed = 0


def re1_n_app(event=True):

    piano.itemconfigure(RE1_n, fill='red')

    global re1_n_isPressed
    if re1_n_isPressed < 1:
        global re1_n_joue
        re1_n_joue = re1_n_note.play()
        print("RE1# appuyé")

        global recording
        if recording == True:
            global dict_re_n1
            dict_re_n1 = {
                'note': 're_n1',
                'startTime': time.time(),
                'endTime': ''
            }

    re1_n_isPressed += 1


def re1_n_rel(event=True):

    piano.itemconfigure(RE1_n, fill='black')
    print("RE1# relevé")

    global re1_n_joue
    re1_n_joue.stop()
    global re1_n_isPressed
    re1_n_isPressed = 0

    global recording, dict_re_n1
    if recording == True:
        dict_re_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_re_n1)

    # FA# - Octave 1


fa1_n_isPressed = 0


def fa1_n_app(event=True):

    piano.itemconfigure(FA1_n, fill='red')

    global fa1_n_isPressed
    if fa1_n_isPressed < 1:
        global fa1_n_joue
        fa1_n_joue = fa1_n_note.play()
        print("FA1# appuyé")

        global recording
        if recording == True:
            global dict_fa_n1
            dict_fa_n1 = {
                'note': 'fa_n1',
                'startTime': time.time(),
                'endTime': ''
            }

    fa1_n_isPressed += 1


def fa1_n_rel(event=True):

    piano.itemconfigure(FA1_n, fill='black')
    print("FA1# relevé")

    global fa1_n_joue
    fa1_n_joue.stop()
    global fa1_n_isPressed
    fa1_n_isPressed = 0

    global recording, dict_fa_n1
    if recording == True:
        dict_fa_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_fa_n1)

    # SOL# - Octave 1


sol1_n_isPressed = 0


def sol1_n_app(event=True):

    piano.itemconfigure(SOL1_n, fill='red')

    global sol1_n_isPressed
    if sol1_n_isPressed < 1:
        global sol1_n_joue
        sol1_n_joue = sol1_n_note.play()
        print("SOL1# appuyé")

        global recording
        if recording == True:
            global dict_sol_n1
            dict_sol_n1 = {
                'note': 'sol_n1',
                'startTime': time.time(),
                'endTime': ''
            }

    sol1_n_isPressed += 1


def sol1_n_rel(event=True):

    piano.itemconfigure(SOL1_n, fill='black')
    print("SOL1# relevé")

    global sol1_n_joue
    sol1_n_joue.stop()
    global sol1_n_isPressed
    sol1_n_isPressed = 0

    global recording, dict_sol_n1
    if recording == True:
        dict_sol_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_sol_n1)

    # LA# - Octave 1


la1_n_isPressed = 0


def la1_n_app(event=True):

    piano.itemconfigure(LA1_n, fill='red')

    global la1_n_isPressed
    if la1_n_isPressed < 1:
        global la1_n_joue
        la1_n_joue = la1_n_note.play()
        print("LA1# appuyé")

        global recording
        if recording == True:
            global dict_la_n1
            dict_la_n1 = {
                'note': 'la_n1',
                'startTime': time.time(),
                'endTime': ''
            }

    la1_n_isPressed += 1


def la1_n_rel(event=True):

    piano.itemconfigure(LA1_n, fill='black')
    print("LA1# relevé")

    global la1_n_joue
    la1_n_joue.stop()
    global la1_n_isPressed
    la1_n_isPressed = 0

    global recording, dict_la_n1
    if recording == True:
        dict_la_n1['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_la_n1)

    # DO - Octave 2


do2_isPressed = 0


def do2_app(event=True):

    piano.itemconfigure(DO2, fill='red')

    global do2_isPressed
    if do2_isPressed < 1:
        global do2_joue
        do2_joue = do2_note.play()
        print("DO2 appuyé")

        global recording
        if recording == True:
            global dict_do2
            dict_do2 = {'note': 'do2', 'startTime': time.time(), 'endTime': ''}

    do2_isPressed += 1


def do2_rel(event=True):

    piano.itemconfigure(DO2, fill='white')
    print("DO2 relevé")

    global do2_joue
    do2_joue.stop()
    global do2_isPressed
    do2_isPressed = 0

    global recording, dict_do2
    if recording == True:
        dict_do2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_do2)

    # RE - Octave 2


re2_isPressed = 0


def re2_app(event=True):

    piano.itemconfigure(RE2, fill='red')

    global re2_isPressed
    if re2_isPressed < 1:
        global re2_joue
        re2_joue = re2_note.play()
        print("RE2 appuyé")

        global recording
        if recording == True:
            global dict_re2
            dict_re2 = {'note': 're2', 'startTime': time.time(), 'endTime': ''}

    re2_isPressed += 1


def re2_rel(event=True):

    piano.itemconfigure(RE2, fill='white')
    print("RE2 relevé")

    global re2_joue
    re2_joue.stop()
    global re2_isPressed
    re2_isPressed = 0

    global recording, dict_re2
    if recording == True:
        dict_re2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_re2)

    # MI - Octave 2


mi2_isPressed = 0


def mi2_app(event=True):

    piano.itemconfigure(MI2, fill='red')

    global mi2_isPressed
    if mi2_isPressed < 1:
        global mi2_joue
        mi2_joue = mi2_note.play()
        print("MI2 appuyé")

        global recording
        if recording == True:
            global dict_mi2
            dict_mi2 = {'note': 'mi2', 'startTime': time.time(), 'endTime': ''}

    mi2_isPressed += 1


def mi2_rel(event=True):

    piano.itemconfigure(MI2, fill='white')
    print("MI2 relevé")

    global mi2_joue
    mi2_joue.stop()
    global mi2_isPressed
    mi2_isPressed = 0

    global recording, dict_mi2
    if recording == True:
        dict_mi2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_mi2)

    # FA - Octave 2


fa2_isPressed = 0


def fa2_app(event=True):

    piano.itemconfigure(FA2, fill='red')

    global fa2_isPressed
    if fa2_isPressed < 1:
        global fa2_joue
        fa2_joue = fa2_note.play()
        print("FA2 appuyé")

        global recording
        if recording == True:
            global dict_fa2
            dict_fa2 = {'note': 'fa2', 'startTime': time.time(), 'endTime': ''}

    fa2_isPressed += 1


def fa2_rel(event=True):

    piano.itemconfigure(FA2, fill='white')
    print("FA2 relevé")

    global fa2_joue
    fa2_joue.stop()
    global fa2_isPressed
    fa2_isPressed = 0

    global recording, dict_fa2
    if recording == True:
        dict_fa2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_fa2)

    # SOL - Octave 2


sol2_isPressed = 0


def sol2_app(event=True):

    piano.itemconfigure(SOL2, fill='red')

    global sol2_isPressed
    if sol2_isPressed < 1:
        global sol2_joue
        sol2_joue = sol2_note.play()
        print("SOL2 appuyé")

        global recording
        if recording == True:
            global dict_sol2
            dict_sol2 = {
                'note': 'sol2',
                'startTime': time.time(),
                'endTime': ''
            }

    sol2_isPressed += 1


def sol2_rel(event=True):

    piano.itemconfigure(SOL2, fill='white')
    print("SOL2 relevé")

    global sol2_joue
    sol2_joue.stop()
    global sol2_isPressed
    sol2_isPressed = 0

    global recording, dict_sol2
    if recording == True:
        dict_sol2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_sol2)

    # LA - Octave 2


la2_isPressed = 0


def la2_app(event=True):

    piano.itemconfigure(LA2, fill='red')

    global la2_isPressed
    if la2_isPressed < 1:
        global la2_joue
        la2_joue = la2_note.play()
        print("LA2 appuyé")

        global recording
        if recording == True:
            global dict_la2
            dict_la2 = {'note': 'la2', 'startTime': time.time(), 'endTime': ''}

    la2_isPressed += 1


def la2_rel(event=True):

    piano.itemconfigure(LA2, fill='white')
    print("LA2 relevé")

    global la2_joue
    la2_joue.stop()
    global la2_isPressed
    la2_isPressed = 0

    global recording, dict_la2
    if recording == True:
        dict_la2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_la2)

    # SI - Octave 2


si2_isPressed = 0


def si2_app(event=True):

    piano.itemconfigure(SI2, fill='red')

    global si2_isPressed
    if si2_isPressed < 1:
        global si2_joue
        si2_joue = si2_note.play()
        print("SI2 appuyé")

        global recording
        if recording == True:
            global dict_si2
            dict_si2 = {'note': 'si2', 'startTime': time.time(), 'endTime': ''}

    si2_isPressed += 1


def si2_rel(event=True):

    piano.itemconfigure(SI2, fill='white')
    print("SI2 relevé")

    global si2_joue
    si2_joue.stop()
    global si2_isPressed
    si2_isPressed = 0

    global recording, dict_si2
    if recording == True:
        dict_si2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_si2)

    # DO# - Octave 2


do2_n_isPressed = 0


def do2_n_app(event=True):

    piano.itemconfigure(DO2_n, fill='red')

    global do2_n_isPressed
    if do2_n_isPressed < 1:
        global do2_n_joue
        do2_n_joue = do2_n_note.play()
        print("DO2# appuyé")

        global recording
        if recording == True:
            global dict_do_n2
            dict_do_n2 = {
                'note': 'do_n2',
                'startTime': time.time(),
                'endTime': ''
            }

    do2_n_isPressed += 1


def do2_n_rel(event=True):

    piano.itemconfigure(DO2_n, fill='black')
    print("DO2# relevé")

    global do2_n_joue
    do2_n_joue.stop()
    global do2_n_isPressed
    do2_n_isPressed = 0

    global recording, dict_do_n2
    if recording == True:
        dict_do_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_do_n2)

    # RE# - Octave 2


re2_n_isPressed = 0


def re2_n_app(event=True):

    piano.itemconfigure(RE2_n, fill='red')

    global re2_n_isPressed
    if re2_n_isPressed < 1:
        global re2_n_joue
        re2_n_joue = re2_n_note.play()
        print("RE2# appuyé")

        global recording
        if recording == True:
            global dict_re_n2
            dict_re_n2 = {
                'note': 're_n2',
                'startTime': time.time(),
                'endTime': ''
            }

    re2_n_isPressed += 1


def re2_n_rel(event=True):

    piano.itemconfigure(RE2_n, fill='black')
    print("RE2# relevé")

    global re2_n_joue
    re2_n_joue.stop()
    global re2_n_isPressed
    re2_n_isPressed = 0

    global recording, dict_re_n2
    if recording == True:
        dict_re_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_re_n2)

    # FA# - Octave 2


fa2_n_isPressed = 0


def fa2_n_app(event=True):

    piano.itemconfigure(FA2_n, fill='red')

    global fa2_n_isPressed
    if fa2_n_isPressed < 1:
        global fa2_n_joue
        fa2_n_joue = fa2_n_note.play()
        print("FA2# appuyé")

        global recording
        if recording == True:
            global dict_fa_n2
            dict_fa_n2 = {
                'note': 'fa_n2',
                'startTime': time.time(),
                'endTime': ''
            }

    fa2_n_isPressed += 1


def fa2_n_rel(event=True):

    piano.itemconfigure(FA2_n, fill='black')
    print("FA2# relevé")

    global fa2_n_joue
    fa2_n_joue.stop()
    global fa2_n_isPressed
    fa2_n_isPressed = 0

    global recording, dict_fa_n2
    if recording == True:
        dict_fa_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_fa_n2)

    # SOL# - Octave 2


sol2_n_isPressed = 0


def sol2_n_app(event=True):

    piano.itemconfigure(SOL2_n, fill='red')

    global sol2_n_isPressed
    if sol2_n_isPressed < 1:
        global sol2_n_joue
        sol2_n_joue = sol2_n_note.play()
        print("SOL2# appuyé")

        global recording
        if recording == True:
            global dict_sol_n2
            dict_sol_n2 = {
                'note': 'sol_n2',
                'startTime': time.time(),
                'endTime': ''
            }

    sol2_n_isPressed += 1


def sol2_n_rel(event=True):

    piano.itemconfigure(SOL2_n, fill='black')
    print("SOL2# relevé")

    global sol2_n_joue
    sol2_n_joue.stop()
    global sol2_n_isPressed
    sol2_n_isPressed = 0

    global recording, dict_sol_n2
    if recording == True:
        dict_sol_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_sol_n2)

    # LA# - Octave 2


la2_n_isPressed = 0


def la2_n_app(event=True):

    piano.itemconfigure(LA2_n, fill='red')

    global la2_n_isPressed
    if la2_n_isPressed < 1:
        global la2_n_joue
        la2_n_joue = la2_n_note.play()
        print("LA2# appuyé")

        global recording
        if recording == True:
            global dict_la_n2
            dict_la_n2 = {
                'note': 'la_n2',
                'startTime': time.time(),
                'endTime': ''
            }

    la2_n_isPressed += 1


def la2_n_rel(event=True):

    piano.itemconfigure(LA2_n, fill='black')
    print("LA2# relevé")

    global la2_n_joue
    la2_n_joue.stop()
    global la2_n_isPressed
    la2_n_isPressed = 0

    global recording, dict_la_n2
    if recording == True:
        dict_la_n2['endTime'] = time.time()
        with open('Enregistrements/tempName.csv', 'a', newline='') as file:
            global clefs
            writer = csv.DictWriter(file, fieldnames=clefs)
            writer.writerow(dict_la_n2)


# Création du piano
piano = Canvas(fenetre,
               height=fenetre.winfo_height() / 1.5,
               width=fenetre.winfo_width(),
               bg='blue')
piano.pack(expand=True)

# Création de chaque touches indépendemment pour plus de contrôle
y, x = fenetre.winfo_height() / 1.5, fenetre.winfo_width() / 14

# Création de la fonction permettant d'afficher l'aide

aideActive = False


def aideFunc():
    global aideActive, A, Z, E, R, T, Y, U, I, O, P, S, D, F, G, H, J, K, W, X, C, V, B, N, comma
    if aideActive == False:
        A = piano.create_text(x,
                              y / 2,
                              text="A",
                              fill="white",
                              font=("Helvetica", 18))
        Z = piano.create_text(x * 2,
                              y / 2,
                              text="Z",
                              fill="white",
                              font=("Helvetica", 18))
        E = piano.create_text(x * 4,
                              y / 2,
                              text="E",
                              fill="white",
                              font=("Helvetica", 18))
        R = piano.create_text(x * 5,
                              y / 2,
                              text="R",
                              fill="white",
                              font=("Helvetica", 18))
        T = piano.create_text(x * 6,
                              y / 2,
                              text="T",
                              fill="white",
                              font=("Helvetica", 18))
        Y = piano.create_text(x * 8,
                              y / 2,
                              text="Y",
                              fill="white",
                              font=("Helvetica", 18))
        U = piano.create_text(x * 9,
                              y / 2,
                              text="U",
                              fill="white",
                              font=("Helvetica", 18))
        I = piano.create_text(x * 11,
                              y / 2,
                              text="I",
                              fill="white",
                              font=("Helvetica", 18))
        O = piano.create_text(x * 12,
                              y / 2,
                              text="O",
                              fill="white",
                              font=("Helvetica", 18))
        P = piano.create_text(x * 13,
                              y / 2,
                              text="P",
                              fill="white",
                              font=("Helvetica", 18))

        S = piano.create_text(x * 1 / 2,
                              y * 3 / 4,
                              text="S",
                              fill="black",
                              font=("Helvetica", 18))
        D = piano.create_text(x * 3 / 2,
                              y * 3 / 4,
                              text="D",
                              fill="black",
                              font=("Helvetica", 18))
        F = piano.create_text(x * 5 / 2,
                              y * 3 / 4,
                              text="F",
                              fill="black",
                              font=("Helvetica", 18))
        G = piano.create_text(x * 7 / 2,
                              y * 3 / 4,
                              text="G",
                              fill="black",
                              font=("Helvetica", 18))
        H = piano.create_text(x * 9 / 2,
                              y * 3 / 4,
                              text="H",
                              fill="black",
                              font=("Helvetica", 18))
        J = piano.create_text(x * 11 / 2,
                              y * 3 / 4,
                              text="J",
                              fill="black",
                              font=("Helvetica", 18))
        K = piano.create_text(x * 13 / 2,
                              y * 3 / 4,
                              text="K",
                              fill="black",
                              font=("Helvetica", 18))

        W = piano.create_text(x * 15 / 2,
                              y * 3 / 4,
                              text="W",
                              fill="black",
                              font=("Helvetica", 18))
        X = piano.create_text(x * 17 / 2,
                              y * 3 / 4,
                              text="X",
                              fill="black",
                              font=("Helvetica", 18))
        C = piano.create_text(x * 19 / 2,
                              y * 3 / 4,
                              text="C",
                              fill="black",
                              font=("Helvetica", 18))
        V = piano.create_text(x * 21 / 2,
                              y * 3 / 4,
                              text="V",
                              fill="black",
                              font=("Helvetica", 18))
        B = piano.create_text(x * 23 / 2,
                              y * 3 / 4,
                              text="B",
                              fill="black",
                              font=("Helvetica", 18))
        N = piano.create_text(x * 25 / 2,
                              y * 3 / 4,
                              text="N",
                              fill="black",
                              font=("Helvetica", 18))
        comma = piano.create_text(x * 27 / 2,
                                  y * 3 / 4,
                                  text=",",
                                  fill="black",
                                  font=("Helvetica", 18))

        aideActive = True
        print("Aide activée")

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

        print("Aide désactivée")
        aideActive = False


DO1 = piano.create_rectangle(0,
                             0,
                             x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
RE1 = piano.create_rectangle(x,
                             0,
                             2 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
MI1 = piano.create_rectangle(2 * x,
                             0,
                             3 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
FA1 = piano.create_rectangle(3 * x,
                             0,
                             4 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
SOL1 = piano.create_rectangle(4 * x,
                              0,
                              5 * x,
                              y,
                              outline="black",
                              fill="white",
                              width=4)
LA1 = piano.create_rectangle(5 * x,
                             0,
                             6 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
SI1 = piano.create_rectangle(6 * x,
                             0,
                             7 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)

DO1_n = piano.create_rectangle(x * 3 / 4,
                               0,
                               x * 5 / 4,
                               y * 2 / 3,
                               outline="black",
                               fill="black",
                               width=4)
RE1_n = piano.create_rectangle(x * 7 / 4,
                               0,
                               x * 9 / 4,
                               y * 2 / 3,
                               outline="black",
                               fill="black",
                               width=4)
FA1_n = piano.create_rectangle(x * 15 / 4,
                               0,
                               x * 17 / 4,
                               y * 2 / 3,
                               outline="black",
                               fill="black",
                               width=4)
SOL1_n = piano.create_rectangle(x * 19 / 4,
                                0,
                                x * 21 / 4,
                                y * 2 / 3,
                                outline="black",
                                fill="black",
                                width=4)
LA1_n = piano.create_rectangle(x * 23 / 4,
                               0,
                               x * 25 / 4,
                               y * 2 / 3,
                               outline="black",
                               fill="black",
                               width=4)

DO2 = piano.create_rectangle(7 * x,
                             0,
                             8 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
RE2 = piano.create_rectangle(8 * x,
                             0,
                             9 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
MI2 = piano.create_rectangle(9 * x,
                             0,
                             10 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
FA2 = piano.create_rectangle(10 * x,
                             0,
                             11 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
SOL2 = piano.create_rectangle(11 * x,
                              0,
                              12 * x,
                              y,
                              outline="black",
                              fill="white",
                              width=4)
LA2 = piano.create_rectangle(12 * x,
                             0,
                             13 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)
SI2 = piano.create_rectangle(13 * x,
                             0,
                             14 * x,
                             y,
                             outline="black",
                             fill="white",
                             width=4)

DO2_n = piano.create_rectangle(x * 31 / 4,
                               0,
                               x * 33 / 4,
                               y * 2 / 3,
                               outline="black",
                               fill="black",
                               width=4)
RE2_n = piano.create_rectangle(x * 35 / 4,
                               0,
                               x * 37 / 4,
                               y * 2 / 3,
                               outline="black",
                               fill="black",
                               width=4)
FA2_n = piano.create_rectangle(x * 43 / 4,
                               0,
                               x * 45 / 4,
                               y * 2 / 3,
                               outline="black",
                               fill="black",
                               width=4)
SOL2_n = piano.create_rectangle(x * 47 / 4,
                                0,
                                x * 49 / 4,
                                y * 2 / 3,
                                outline="black",
                                fill="black",
                                width=4)
LA2_n = piano.create_rectangle(x * 51 / 4,
                               0,
                               x * 53 / 4,
                               y * 2 / 3,
                               outline="black",
                               fill="black",
                               width=4)

border = piano.create_rectangle(0,
                                0,
                                fenetre.winfo_width(),
                                fenetre.winfo_height() / 1.5,
                                outline="black",
                                width=10)
print("Piano créé")

# Création du menu


mainMenu = Menu(fenetre, tearoff=0, activebackground='red')
fenetre.config(menu=mainMenu)

menuEnregistrer = Menu(fenetre, tearoff=0, activebackground='red')
mainMenu.add_cascade(label="Fichier", menu=menuEnregistrer)

menuEnregistrer.add_command(label="Commencer l'enregistrement",
                            command=startRecording)
menuEnregistrer.add_command(label="Arrêter l'enregistrement",
                            command=stopRecording)
menuEnregistrer.entryconfigure(1, state=DISABLED)
menuEnregistrer.add_command(label="Parcourir les enregistrements",
                            command=parcourir)

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

print("Piano fermé")