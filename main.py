from xml.dom import minidom

FILE_BARBATI = "C:\\Users\\msabau1\\Documents\\GenerarePersoane\\prenumeBaieti.txt"
FILE_FEMEI = "C:\\Users\\msabau1\\Documents\\GenerarePersoane\\prenumeFete.txt"
FILE_NUME_FAMILIE = "C:\\Users\\msabau1\\Documents\\GenerarePersoane\\numeFamilie.txt"
criteriu_lungime = lambda nume: len(nume)
def nrVocale(s):
    s = s.lower()
    kV = 0
    vocale = ["a", "e", "i", "o", "u", "ă", "â", "î"]
    for litera in s:
        if litera in vocale:
            kV = kV + 1
    return kV

def nrConsoane(s):
    s = s.lower()
    kC = 0
    consoane = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "ș", "ț"]
    for litera in s:
        if litera in consoane:
            kC = kC + 1
    return kC

def nrDiacritice(s):
    s = s.lower()
    kD = 0
    diacritice = ["ă", "â", "î", "ș", "ț"]
    for litera in s:
        if litera in diacritice:
            kD = kD + 1
    return kD

def prenumeXMLGenerator():
    f1 = open(FILE_BARBATI, "r", encoding="utf-8-sig")
    f2 = open(FILE_FEMEI, "r", encoding="utf-8-sig")
    if f1 == None or f2 == None:
        raise Exception("Fisierul nu a putut fi deschis!")
    else:
        listaBarbati = []
        for line in f1:
            listaBarbati.append(line.strip())
        f1.close()
        listaBarbati = sorted(listaBarbati, key=criteriu_lungime)
        print(listaBarbati)
        listaBarbati = sorted(listaBarbati, key=lambda s: nrDiacritice(s), reverse=True)
        print(listaBarbati)
        listaBarbati = sorted(listaBarbati, key=lambda s: nrVocale(s), reverse=True)
        print(listaBarbati)
        listaBarbati = sorted(listaBarbati, key=lambda s: nrConsoane(s), reverse=True)
        print(listaBarbati)
        listaFemei = []
        for line in f2:
            listaFemei.append(line.strip())
        # print(listaFemei)
        f2.close()
        listaFemei = sorted(listaFemei, key=criteriu_lungime)
        print(listaFemei)
        listaFemei = sorted(listaFemei, key=lambda s: nrDiacritice(s), reverse=True)
        print(listaFemei)
        listaFemei = sorted(listaFemei, key=lambda s: nrVocale(s), reverse=True)
        print(listaBarbati)
        listaFemei = sorted(listaFemei, key=lambda s: nrConsoane(s), reverse=True)
        print(listaFemei)
        root = minidom.Document()
        listaPrenume = root.createElement("listaPrenume")
        root.appendChild(listaPrenume)
        for p in listaBarbati:
            e = root.createElement("prenume")
            e.setAttribute("lungime", str(len(p)))
            e.setAttribute("sex", "M")
            e.setAttribute("consoane", str(nrConsoane(p)))
            e.setAttribute("vocale", str(nrVocale(p)))
            e.setAttribute("diacritice", str(nrDiacritice(p)))
            p = root.createTextNode(p)
            e.appendChild(p)
            listaPrenume.appendChild(e)
        for p in listaFemei:
            e = root.createElement("prenume")
            e.setAttribute("lungime", str(len(p)))
            e.setAttribute("sex", "F")
            e.setAttribute("consoane", str(nrConsoane(p)))
            e.setAttribute("vocale", str(nrVocale(p)))
            e.setAttribute("diacritice", str(nrDiacritice(p)))
            p = root.createTextNode(p)
            e.appendChild(p)
            listaPrenume.appendChild(e)
        xml_str = root.toprettyxml(indent="\t")
        file = "prenume.xml"
        with open(file, "w", encoding="utf-8-sig") as f:
            f.write(xml_str)
        f.close()

def numeFamilieXMLGenerator():
    f3 = open(FILE_NUME_FAMILIE, "r", encoding="utf-8-sig")
    if f3 == None:
        raise Exception("Fisierul nu a putut fi deschis!")
    else:
        listaNumeFamilie = []
        for line in f3:
            listaNumeFamilie.append(line.strip())
        f3.close()
        root = minidom.Document()
        listaNume = root.createElement("listaNumeFamilie")
        root.appendChild(listaNume)
        for p in listaNumeFamilie:
            e = root.createElement("numeFamilie")
            e.setAttribute("lungime", str(len(p)))
            e.setAttribute("consoane", str(nrConsoane(p)))
            e.setAttribute("vocale", str(nrVocale(p)))
            e.setAttribute("diacritice", str(nrDiacritice(p)))
            nodText = root.createTextNode(p)
            e.appendChild(nodText)
            listaNume.appendChild(e)
        xml_str = root.toprettyxml(indent="\t")
        file = "numeFamilie.xml"
        with open(file, "w", encoding="utf-8-sig") as f:
            f.write(xml_str)
        f.close()

prenumeXMLGenerator()
numeFamilieXMLGenerator()
