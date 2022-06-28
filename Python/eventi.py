import random
import main
import global_var as GLOB

def testa():

# ---- GESTIONE EVENTI ----

    def AggiungiChiavetta():
        
        main.Gui.inventory_sound.play()
        
        if main.player.evento == GLOB.RandomKey:
            var = GLOB.RandomRoom
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario[GLOB.RandomKey] = (GLOB.chiavette[var][2], False, "Sono pesante, andavo di moda negli anni '80 / '90, e con me almeno una volta ci hai parlato, che cosa sono?")
            main.player.evento = None
            return
        
        
        if main.player.evento == "chiavetta-1":
            var = "Fisica"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-1"] = (GLOB.chiavette[var][2], False, "Proprietario: Tommaso Dalbesio - Files: ziopera.pkt")
            main.player.evento = None


        if main.player.evento == "chiavetta-2":
            var = "1A"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-2"] = (GLOB.chiavette[var][2], False, "Proprietario: Stefano Senestro - Files: TheLostKeys.py")
            main.player.evento = None


        if main.player.evento == "chiavetta-3":
            var = "WC-Femmine"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-3"] = (GLOB.chiavette[var][2], False, "Proprietario: Aleksandra Venezia - Files: ciauu.py")
            main.player.evento = None


        if main.player.evento == "chiavetta-4":
            var = "AulaMagna"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-4"] = (GLOB.chiavette[var][2], False, "Proprietario: Matteo Seimandi - Files: App.js")
            main.player.evento = None


        if main.player.evento == "chiavetta-5":
            var = "AulaProfessori"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-5"] = (GLOB.chiavette[var][2], False, "Proprietario: Giuseppe Di Biase - Files: stringhedibrutto.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-6":
            var = "LabInfo"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-6"] = (GLOB.chiavette[var][2], False, "Proprietario: Giulio Dajani - Files: shqipe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-7":
            var = "4A"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-7"] = (GLOB.chiavette[var][2], False, "Proprietario: Lorenzo Ferrato - Files: Ilmiocodice.sql")
            main.player.evento = None


        if main.player.evento == "chiavetta-8":
            var = "AulaVideo"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-8"] = (GLOB.chiavette[var][2], False, "Proprietario: Arvind Pal - Files: onlyCss.css index.html")
            main.player.evento = None


        if main.player.evento == "chiavetta-9":
            var = "LabInformatica"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-9"] = (GLOB.chiavette[var][2], False, "Proprietario: Alberto Boaglio - Files: ABMediaAgency")
            main.player.evento = None


        if main.player.evento == "chiavetta-10":
            var = "Ripostiglio"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-10"] = (GLOB.chiavette[var][2], False, "E' la chiavetta per le macchinette...")
            main.player.evento = None
            
            
            
        if main.player.evento == "chiavetta-11":
            var = "1D"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-11"] = (GLOB.chiavette[var][2], False, "Proprietario: Mattia Barbero - Files: Italian_Ripper.py IlBarbista.sql")
            main.player.evento = None
            
            
        if main.player.evento == "chiavetta-12":
            var = "Corridoio3"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-12"] = (GLOB.chiavette[var][2], False, "Proprietario: Marco Rolando - Files: somebodyelse.mp3")
            main.player.evento = None



    def Cerca(event):
        oggetti = (GLOB.inventario.keys())

        c = False
        for oggetto in oggetti:
            if oggetto == event:
                c = True

        return c


    def Blocca():
        main.Gui.door_sound_locked.play()
        main.player.evento = "porta-99"
        risposte = ["la porta sembra chiusa", "non si apre", "è bloccata"]
        main.player.finish()
        main.player.setAllkeys(False)
        GLOB.PlayerIsRunning = False
        c = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
        c.stampa()
        GLOB.PlayerReset = True


    def Controlla(o):
        try:
            GLOB.inventario[o]
            return False

        except KeyError:
            return True
        
    
    def ControllaContenuto(o):
        try:
                        
            # print(GLOB.inventario[o][1])
            if GLOB.inventario[o][1]:
                return False
            else:
                return True
        except KeyError:
            return True


    def VerificaEnigmi():
        var = GLOB.Stanza
        # print(var)

        c = False
        for value in GLOB.enigmi_risolti:
            if var == value:
                c = True

        return c


    def CheckEnimga(v):
        var = v
        # print(var)

        c = False
        for value in GLOB.enigmi_risolti:
            if var == value:
                c = True

        return c



    if main.player.evento == "enigma":
        condizione = False

        for value in GLOB.enigmi_da_risolvere:
    
            if value != GLOB.Stanza:

                GLOB.Enigma = False
                main.player.evento = None
            
            else:
                condizione = True

        
        if GLOB.Stanza == "WC-Femmine" and Controlla("Ghiaccio"):
            condizione = False
            
            
        if ("Corridoio" in GLOB.Stanza and GLOB.Piano == "3-SecondoPiano" and ControllaContenuto("chiavetta-10")):
            condizione = False
            
            risposte = ["Sembra un distributore di merendine", "Cosa farei per un duplo", "Strano che non sia ancora stato distrutto, sarebbero state merendine gratis...", "Non so il perche', ma ho una certa fame..."]
            
            d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
            d.stampa()
            
            
        if GLOB.Stanza == "Archivio" and ControllaContenuto(GLOB.RandomKey):
            condizione = False
            
            testo = "Sembrano due vecchi telefoni..."
            
            d = main.Dialoghi(GLOB.scelta_char, testo, 4)
            d.stampa()
            

        if condizione:
            GLOB.Enigma = True
        else:
            GLOB.Enigma = False
            
        GLOB.PlayerReset = True


    if main.player.evento == "enigma-risolto":
        testo = "Default"
        
        if GLOB.Stanza == "Chimica":
            testo = "Ho trovato un appunto del quale dice che ci sia una chiavetta nascosta all'interno della cella frigorifero...|Mmmm... mi potrebbe essere utile."
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "Chimica"
                GLOB.MonsterActualFloor = "1-PianoTerra"
                GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "WC-Femmine":
            oggetto = "Ghiaccio"

            if Cerca(oggetto):
                GLOB.inventario.pop(oggetto)
                main.player.evento = "chiavetta-3"
                AggiungiChiavetta()

                testo = "Wow!|Chi se lo sarebbe aspettato di trovare una chiavetta all'interno del ghiaccio|Magari potrei cercare un PC per vedere il suo contenuto."
                
                if GLOB.Stanza != GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "WC-Femmine"
                    GLOB.MonsterActualFloor = "2-PrimoPiano"
                    GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "AulaMagna":
            testo = "Mmmm.|Forse la prossima chiavetta ha qualcosa a che fare con una sedia."

            if GLOB.Stanza != GLOB.MonsterActualRoom and len(GLOB.enigmi_risolti) > 1:
                GLOB.MonsterActualRoom = "AulaMagna"
                GLOB.MonsterActualFloor = "2-PrimoPiano"
                GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "1A":
            testo = "Pensavo piu' difficile...|Ad ogni modo che cos'e' quella strana cosa tra i gessetti della lavagna?!?"

        if GLOB.Stanza == "AulaProfessori":
            testo = "Interessante.|Ho trovato una chiave dietro al foglio, con su scritto \"WC\""
            
            oggetto = "Chiave"
            descrizione = "Chiave del bagno Maschile"
            tipo = 3
            
            GLOB.inventario[oggetto] = (GLOB.oggetti[tipo][2], True, descrizione)

        if GLOB.Stanza == "AulaVideo":
            testo = "Pascoli...|Chissa' se nella libreria della scuola ci potrebbe essere quello che sto cercando."
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "Chimica"
                GLOB.MonsterActualFloor = "1-PianoTerra"
                GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "LabInfo":
            testo = "Scratch... che ricordi, chissa' se tra questi pc ce ne sarà uno funzionante..."
                
        if "Corridoio" in GLOB.Stanza and GLOB.Piano == "3-SecondoPiano":
            
            if Cerca("chiavetta-10"):
                main.player.evento = "chiavetta-12"
                AggiungiChiavetta()
            
            
            testo = "Si, evvai!!| Oltretutto inserendo il codice 4096 nella macchinetta, mi ha dato un'altra chiavetta!|Andiamo ad analizzarne il contenuto!"
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "Default"
                GLOB.MonsterActualFloor = "2-PrimoPiano"
                GLOB.MonsterHasChangedRoom = True
                
        if GLOB.Stanza == "Archivio":
            testo = "Ce l'ho fatta!!|Oltretutto c'è pure uno strano codice dietro al foglio...|C'è scritto: '"+str(GLOB.codice)+"'"
            
            GLOB.ShowCodice = True
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "Corridoio"
                GLOB.MonsterActualFloor = "1-PianoTerra"
        
        if testo != "Default":
            testo = testo.split("|")
            for t in testo:
                d = main.Dialoghi(GLOB.scelta_char, t, 4)
                d.stampa()
                
        GLOB.PlayerReset = True


    def piano():

        if main.player.evento == "piano-0":
            GLOB.Piano = "0-PianoSegreto"
            main.player.evento = None
            main.stanze.setToDefault()
            main.stanze.dizionario_flag["StanzaSegreta"] = True

            main.animazione.iFinished = False
            main.stanze.setPosition((192, 72), (146, 62))

        elif main.player.evento == "piano-1":
            last_floor = GLOB.Piano
            GLOB.Piano = "1-PianoTerra"
            main.player.evento = None
            main.stanze.setToDefault()

            main.animazione.iFinished = False


            main.stanze.setPosition((274, 72), (-132, -46))
            main.stanze.dizionario_flag["Corridoio"] = True

        elif main.player.evento == "piano-2":
            last_floor = GLOB.Piano
            GLOB.Piano = "2-PrimoPiano"
            main.player.evento = None
            main.stanze.setToDefault()
            main.stanze.dizionario_flag["Corridoio1"] = True

            main.animazione.iFinished = False

            if last_floor == "1-PianoTerra":
                main.stanze.setPosition((216, 96), (-286, -32))
            else:
                main.stanze.setPosition((260, 110), (-312, -148))

        elif main.player.evento == "piano-3":
            GLOB.Piano = "3-SecondoPiano"
            main.player.evento = None
            main.stanze.setToDefault()
            main.stanze.dizionario_flag["Corridoio2"] = True

            main.animazione.iFinished = False
            main.stanze.setPosition((270, 110), (-326, -148))

        elif main.player.evento == "piano-4":
            Blocca()
            return False

    def porte():
        
        
    
        if main.player.evento == "porta-0":
            main.player.evento = None
            main.stanze.setToDefault()


            if GLOB.Piano == "2-PrimoPiano":
                        
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["Ufficio"] = True

                if GLOB.Stanza == "Ufficio":
                    main.stanze.dizionario_flag["Corridoio1"] = True

            else:
                Blocca()
                return False
            
            main.Gui.door_sound.play()
            main.animazione.iFinished = False
        
        
        if main.player.evento != None:
            if "porta" in main.player.evento and main.player.evento != "porta-0":
                Blocca()
                return False
        

    if piano() == False or porte() == False:
        return

    # print(GLOB.PlayerCanCollect)
    if GLOB.PlayerCanCollect:
        AggiungiChiavetta()


    def NonTrovato():
        risposte = ["Non ho trovato nulla", "Sembrerebbe che non ci sia nulla", "Niente.", "Qua non c'è nulla."]
        
        d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
        d.stampa()
        GLOB.PlayerReset = True
        main.player.evento = None

    def Trovato(o):
        risposte = ["Trovato "+str(o), "Ho trovato "+str(o)]
        d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
        d.stampa()
        GLOB.PlayerReset = True
        main.player.evento = None


    if main.player.evento == "cerca-T":
        main.Gui.inventory_sound.play()
        GLOB.PlayerReset = True
        oggetto = "Default"
        descrizione = "Default"

        if GLOB.Stanza == "Chimica" and VerificaEnigmi():
            tipo = 0
            oggetto = "Ghiaccio"
            descrizione = "All'interno si intravede uno strano elemento"


        if GLOB.Stanza == "AulaProfessori":
            tipo = 1
            oggetto = "Libro Karl Marx"
            descrizione = "All'interno c'e' uno strano post-it con su scritto: \"E' stato bello finche\' e' durato stare in questa scuola 02/02/2018\""

        if GLOB.Stanza == "AulaMagna" and VerificaEnigmi():
            oggetto = "chiavetta-4"

            if Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return

        if GLOB.Stanza == "1A" and VerificaEnigmi():
            oggetto = "chiavetta-2"

            if Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return



        if GLOB.Stanza == "Archivio" and CheckEnimga("AulaVideo"):
            oggetto = "chiavetta-8"

            if Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return

        if GLOB.Stanza == "LabInfo" and CheckEnimga("LabInfo"):
            oggetto = "chiavetta-6"

            if Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return

        if Controlla(oggetto):
            try:
                GLOB.inventario[oggetto] = (GLOB.oggetti[tipo][2], True, descrizione)
            except UnboundLocalError:
                NonTrovato()
                return
        else:
            NonTrovato()
            return

        Trovato(oggetto)


    if main.player.evento == "cerca-F":
        main.Gui.inventory_sound.play()
        NonTrovato()
        GLOB.PlayerReset = True


    if main.player.evento == "vittoria":
        main.game_win()
        
        
    if main.player.evento == "pc":
        main.PC().show()


    if main.player.evento == "nascondiglio" and GLOB.PlayerCanHide:
        main.player.evento = None
        
        if GLOB.PlayerIsHidden:
            GLOB.PlayerIsHidden = False
        else:
            GLOB.PlayerIsHidden = True
            main.Gui.door_sound.play()
            
    
    if main.player.evento == "ispeziona":
        main.player.evento = None
        
        testo = "Default"
        
        if GLOB.Piano == "1-PianoTerra":
            
            if "Corridoio" in GLOB.Stanza:
                testo = "Sembra una vecchia bacheca con gli eventi riportati di quegli anni|Nulla che mi possa servire..."
                
            if GLOB.Stanza == "Fisica":
                testo = "Ah.. che bello!|Non riusciro' mai a scordarmi l'omega del Prof. Fulchero"
                
                
        if GLOB.Piano == "2-PrimoPiano":
                
            if "Corridoio" in GLOB.Stanza:
                testo = "Sembra un distributore di merendine|Peccato che non sia funzionante..."
                
            if GLOB.Stanza == "AulaMagna":
                testo = "Il tempo ha proprio ridotto male questo posto..."
                
            if GLOB.Stanza == "WC-Maschi":
                testo = "Sembra un rubinetto, ma purtroppo non ne esce acqua."
                
        if testo != "Default":  
            testo = testo.split("|")
            
            for frase in testo:
                
                d = main.Dialoghi(GLOB.scelta_char, frase, 4)
                d.stampa()