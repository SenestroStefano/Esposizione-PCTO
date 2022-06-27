import global_var as GLOB
import main

percorso = "../MappaGioco/Tileset/Stanze/"
global dizionario_flag

def setPosition(posP, posC):
    global pos_portaP, pos_portaC
    pos_portaP = posP
    pos_portaC = posC

def inizializza():
    setToDefault()

    setPosition((152, 122), (130, -118))

def setToDefault():
    global dizionario_flag
    

    dizionario_flag = {
        
        "Ufficio" : False,
        "Esterno" : False,
        "Corridoio" : False,
        "Corridoio1" : False,
    
     }

def Ufficio():
    
    setPosition((252, 108), (-184, -140))

    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "Ufficio"
    GLOB.Default_collisions = "ufficio_Collisioni.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Ufficio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/UfficioOggetti.png"

    dizionario_flag["Ufficio"] = False


def Corridoio():
    

    if GLOB.Stanza == "Esterno":
        setPosition((270, 74), (-244, 56))

    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Corridoio1"
    GLOB.Default_collisions = "Corridoio_Collisioni.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Corridoio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/CorridoioOggetti.png"

    dizionario_flag["Corridoio"] = False


def Corridoio1():
    

    if GLOB.Stanza == "Ufficio":
        setPosition((154, 110), (-166, -32))

    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "Corridoio1"
    GLOB.Default_collisions = "Corridoio1_Collisioni.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Corridoio1.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Corridoio1Oggetti.png"

    dizionario_flag["Corridoio1"] = False

inizializza()


def CaricaElementi():
    GLOB.LoadCollisions = True
    main.collisions.load_map(GLOB.Default_Map)
    main.collisions.load_objects(GLOB.Default_object)
    main.load_collisions(GLOB.Default_collisions)


def caricaStanza():
    

    if not main.animazione.iFinished:
        main.collisions.load_map(GLOB.Default_Map)
        GLOB.LoadCollisions = True

        if GLOB.Default_object != None:
            main.collisions.load_objects(GLOB.Default_object)

    if GLOB.Default_collisions != None:
        main.load_collisions(GLOB.Default_collisions)


    if GLOB.Piano == "1-PianoTerra":

        if dizionario_flag["Corridoio1"]:
            Corridoio1()

        if dizionario_flag["Corridoio"]:
            Corridoio()

    elif GLOB.Piano == "2-PrimoPiano":
    
        if dizionario_flag["Corridoio1"]:
            Corridoio1()

        if dizionario_flag["Corridoio"]:
            Corridoio()

        if dizionario_flag["Ufficio"]:
            Ufficio()

    elif GLOB.Piano == "3-SecondoPiano":

        if dizionario_flag["Corridoio1"]:
            Corridoio1()