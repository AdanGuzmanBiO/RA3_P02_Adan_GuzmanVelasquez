# *** LListes python ***

def comprobarInt():
    try:
        return int(input("\nEscull l'opció que vols: "))

    except ValueError:
        print("Valor incorrecte")

def comprobarStr(dada):
    try:
        text = str(input(f"introdueix la dada {dada}: "))
        
    except ValueError:
        print ("Valor incorrecte")

    return text



def comprobarIndexLlista(llista):
    try:
        return int(input("Escull el teu index: "))

    except IndexError:
        print("Fora de rang")

alumne_nou = []

alumnes = [
    ["Anna", "Pujol", "SMX", "1r", "A101"],
    ["Marc","Serra","SMX","2n","A102"],
    ["Laia","Rovira","ASIX","1r","B201"],
    ["Jordi","Casals","ASIX","2n","B202"]
]

while True:

    print("\nLes opciones que pots triar son: ")
    print("1. Mostra les dades de tots els alumnes")
    print("2. Agregar un nou alumne")

    opcio = comprobarInt()
    match opcio:
        case 1:
            for i, alumne in enumerate(alumnes):
                print(f"\nAlumne {i}:")
                for j, campo in enumerate (alumne):
                    print (f"Campo {j}:", campo)


        case 2:
            print("Dades del nou alumne: ")
            dada = "nom "
            nom = comprobarStr(dada)

            dada = "cognom "
            cognom = comprobarStr(dada)
            
            dada = "grau "
            grau = comprobarStr(dada)
            
            dada = "curs "
            curs = comprobarStr(dada)

            dada = "aula "
            aula = comprobarStr(dada)

            print("\nLes dades de l'alumne nou son: ")
            print(f"""Nom: {nom}
Cognom: {cognom}
Grau: {grau}
Curs: {curs}
Aula: {aula}
            """)

            alumne_nou.append({
                "nom" : nom,
                "cognom" : cognom,
                "grau" : grau,
                "curs" : curs,
                "aula" : aula
            })

            print(alumne_nou)

            alumnes.append(alumne_nou)

        
        case 3:
            print("Opció 3")

        case 4:
            print("Opció 4")

        case 5:
            print("Opció 5")

        case 6:
            print("Opció 6")
            break

        case _:
            print("Opció incorrecta, tria una opció dins del rang")