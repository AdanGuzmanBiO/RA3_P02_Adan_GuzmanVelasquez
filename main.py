# *** LListes python ***

def comprobarInt(text):
    try:
        return int(input(f"{text}"))

    except ValueError:
        print("Valor incorrecte")

def comprobarStr(dada):
    try:
        text = str(input(f"introdueix la dada {dada}: "))
        
    except ValueError:
        print ("Valor incorrecte")

    return text

def LlistaAlumnes(alumnes):
    for i, alumne in enumerate (alumnes):
        print(f"\nL'alumne amb index {i} es")
        for j, campo in enumerate (alumne):
            print(f"Campo {j}: {campo}")

def GrauAlumne(alumnes_grau,alumnes):
    for i, alumne in enumerate (alumnes):
        for j, campo in enumerate (alumne):
            if alumnes_grau == campo.lower():
                print(f"L'alumne {alumne[0]} cursa el grau {alumnes_grau}")
                
def comprobarIndexLlista(alumnes, text):
    while True:
        try:
            while True:
                index = int(input(f"{text}"))
                if index < 0:
                    print("L'index ha de ser un enter positiu")
                else:
                    break
            alumnes[index]
            return index
        
        except ValueError:
            print("Valor incorrecte, ha de ser un enter")

        except IndexError:
            print("Fora de rang, torna-ho a provar")
    

alumne_nou = []

alumnes = [
    ["Anna", "Pujol", "SMX", "1r", "A101"],
    ["Marc","Serra","SMX","2n","A102"],
    ["Laia","Rovira","ASIX","1r","B201"],
    ["Jordi","Casals","ASIX","2n","B202"]
]

while True:

    print("\nLes opciones que pots triar son: ")
    print("""1. Mostra les dades de tots els alumnes
2. Agregar un nou alumne
3. Eliminar un alumne
4. Mostra alumnes d'un grau concret
5. Modificar dades d'un alumne
6. Sortir del sistema""")

    opcio_menu_01 = comprobarInt(text = "\nTria una opció del menú: ")
    match opcio_menu_01:
        case 1:
            LlistaAlumnes(alumnes)

        case 2:
            print("Dades del nou alumne: ")
            nom = comprobarStr(dada = "nom")
            cognom = comprobarStr(dada = "cognom")
            grau = comprobarStr(dada = "grau")
            curs = comprobarStr(dada = "curs")
            aula = comprobarStr(dada = "aula")

            print("\nLes dades de l'alumne nou son: ")
            print(f"""Nom: {nom}
Cognom: {cognom}
Grau: {grau}
Curs: {curs}
Aula: {aula}""")

            alumne_nou = [nom, cognom, grau, curs, aula]
            alumnes.append(alumne_nou)
        
        case 3:
            print("\nLlista d'alumnes actual: ")
            LlistaAlumnes(alumnes)
            del alumnes[comprobarIndexLlista(alumnes, text = "\nTria l'index de l'alumne que vols eliminar: ")]

        case 4:
            while True:
                alumnes_grau = input("\nEls alumnes de qué grau vols veure(SMX/ASIX)? ").lower()
                if alumnes_grau == "smx" or alumnes_grau == "asix":
                    break
                else:
                    print("Grau incorrecte, torna-ho a provar")
            
            GrauAlumne(alumnes_grau, alumnes)
                
        case 5:
            print("Les opcions que pots triar son: ")
            print("""1. Agregar una dada nova
2. Eliminar una dada""")
            opcio_menu_02 = comprobarInt(text = "\nTria entre agregar o eliminar una dada d'un alumne: ")

            match opcio_menu_02:
                case 1:
                    while True:
                        LlistaAlumnes(alumnes)
                        index_alumne_agregar = comprobarIndexLlista(alumnes, text = "\nTria l'index al que vols agregar una dada: ")
                        for index_alumne, alumne in enumerate (alumnes):
                            if index_alumne == index_alumne_agregar:
                                print(f"Les dades de l'alumne amb index {index_alumne_agregar} son:")
                            for index_dada, campo in enumerate (alumne):
                                if index_alumne == index_alumne_agregar:
                                    print(F"Index: {index_dada}: {campo}")
                        
                        dada_nova = comprobarStr(dada = "nova")

                        alumnes[index_alumne_agregar].append(dada_nova)
                        print("\nDada agregada correctament")

                        while True:
                            agregar_altre_dada = input("Vols agregar una altra dada (Si/No)? ").lower()
                            if agregar_altre_dada != "si" and agregar_altre_dada != "no":
                                print("Resposta incorrecta, torna-ho a provar")
                            else:
                                break
                            
                        if agregar_altre_dada == "si":
                            continue
                        else:
                            print("Tornant al menú principal..")
                            break

                case 2:
                    while True:
                        LlistaAlumnes(alumnes)
                        index_alumne_eliminar = comprobarIndexLlista(alumnes, text = "\nTria l'index que té la dada que vols eliminar: ")
                        for index_alumne, alumne in enumerate (alumnes):
                            if index_alumne == index_alumne_eliminar:
                                print(f"Les dades de l'alumne amb index {index_alumne_eliminar} son:")
                            for index_dada, campo in enumerate (alumne):
                                if index_alumne == index_alumne_eliminar:
                                    print(F"Index: {index_dada}: {campo}")
                                    
                        index_dada_eliminar = comprobarIndexLlista(alumnes, text = "\nIndica l'index de la dada que vols eliminar: ")

                        del alumnes[index_alumne_eliminar][index_dada_eliminar]
                        print("\nDada eliminada correctament")

                        while True:
                            eliminar_altre_dada = input("Vols eliminar un altre dada (Si/No)? ").lower()
                            if eliminar_altre_dada != "si" and eliminar_altre_dada != "no":
                                print("Resposta incorrecta, torna-ho a provar")
                            else:
                                break
                            
                        if eliminar_altre_dada == "si":
                            continue
                        else:
                            print("Tornant al menú principal..")
                            break
                case _:
                    print("Opció incorrecta, tria una opció dins del rang")

        case 6:
            print("Sortint de la base de dades dels alumnes..")
            break

        case _:
            print("Opció incorrecta, tria una opció dins del rang")