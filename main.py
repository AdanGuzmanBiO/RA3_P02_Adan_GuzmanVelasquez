# *** LListes python ***

# Funcio que comprova que l'entrada sigui un enter y personalització de text
def comprobarInt(text):
    try:
        return int(input(f"{text}"))

    except ValueError:
        print("Valor incorrecte")

# Funció per variar les dades que es demanen a l'usuari
def comprobarStr(dada):
    try:
        text = str(input(f"introdueix la dada {dada}: "))
        
    except ValueError:
        print ("Valor incorrecte")

    return text

# Funcio per veure la llista d'alumnes
def LlistaAlumnes(alumnes):
    for i, alumne in enumerate (alumnes):
        print(f"\nL'alumne amb index {i} es")
        for j, campo in enumerate (alumne):
            print(f"Campo {j}: {campo}")

# Funció per veure els alumnes d'un grau concret
def GrauAlumne(alumnes_grau,alumnes):
    for i, alumne in enumerate (alumnes):
        for j, campo in enumerate (alumne):
            if alumnes_grau == campo.lower():
                print(f"L'alumne {alumne[0]} cursa el grau {alumnes_grau}")

# Funcio per comprovar l'index d'una llista y personalització de text
def comprovarIndexLlista(comprovar_index, text):
    while True:
        try:
            while True:
                index = int(input(f"{text}"))
                if index < 0:
                    print("L'index ha de ser un enter positiu")
                else:
                    break
            comprovar_index[index]
            return index
        
        except ValueError:
            print("Valor incorrecte, ha de ser un enter")

        except IndexError:
            print("Fora de rang, torna-ho a provar")
    
#Dades inicials
alumne_nou = []

alumnes = [
    ["Anna", "Pujol", "SMX", "1r", "A101"],
    ["Marc","Serra","SMX","2n","A102"],
    ["Laia","Rovira","ASIX","1r","B201"],
    ["Jordi","Casals","ASIX","2n","B202"]
]

# Menu principal loopeable fins que l'usuari decideixi sortir
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

        # Imprimeix la llista dels alumnes en pantalla
        case 1:
            LlistaAlumnes(alumnes)

        # Agrega un nou alumne a la llista demanant les dades
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
        
        # Elimina un alumne de la llista segons l'index
        case 3:
            print("\nLlista d'alumnes actual: ")
            LlistaAlumnes(alumnes)
            del alumnes[comprovarIndexLlista(comprovar_index = alumnes, text = "\nTria l'index de l'alumne que vols eliminar: ")]
            print("Alumne eliminat correctament")

        # Mostra els alumnes d'un grau concret, demanant a l'usuari el grau que vol veure
        case 4:
            while True:
                alumnes_grau = input("\nEls alumnes de qué grau vols veure(SMX/ASIX)? ").lower()
                if alumnes_grau == "smx" or alumnes_grau == "asix":
                    break
                else:
                    print("Grau incorrecte, torna-ho a provar")
            
            GrauAlumne(alumnes_grau, alumnes)
        
        # Menú per a que l'usuari pugui decidir quin tipus de modificació vol fer
        case 5:
            while True:
                print("\nLes opcions que pots triar son: ")
                print("""1. Agregar una dada nova
2. Eliminar una dada
3. Tornar al menú principal""")
                
                opcio_menu_02 = comprobarInt(text = "\nTria entre agregar/eliminar una dada d'un alumne o tornar al menú principal: ")

                match opcio_menu_02:

                    # Agrega una dada nova a partir de l'index de l'alumne que l'usuari indica
                    case 1:
                        while True:
                            LlistaAlumnes(alumnes)
                            index_alumne_agregar = comprovarIndexLlista(comprovar_index = alumnes, text = "\nTria l'index al que vols agregar una dada: ")
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
                                print("Sortint de l'agregador de dades..")
                                break

                    # Elimina una dada a partir de l'index de l'alumne i de la dada que l'usuari indica
                    case 2:
                        while True:
                            LlistaAlumnes(alumnes)
                            index_alumne_eliminar = comprovarIndexLlista(comprovar_index = alumnes, text = "\nTria l'index que té la dada que vols eliminar: ")
                            for index_alumne, alumne in enumerate (alumnes):
                                if index_alumne == index_alumne_eliminar:
                                    print(f"Les dades de l'alumne amb index {index_alumne_eliminar} son:")
                                for index_dada, campo in enumerate (alumne):
                                    if index_alumne == index_alumne_eliminar:
                                        print(F"Index: {index_dada}: {campo}")
                                        
                            index_dada_eliminar = comprovarIndexLlista(comprovar_index = alumnes[index_alumne_eliminar], text = "\nIndica l'index de la dada que vols eliminar: ")

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
                                print("Sortint de l'eliminador de dades..")
                                break
                    case 3:
                        print("Tornant al menú principal..")
                        break

                    case _:
                        print("Opció incorrecta, tria una opció dins del rang")

        # Surt del programa
        case 6:
            print("Sortint de la base de dades dels alumnes..")
            break
        
        # Controla que l'usuari introdueixi una opció correcta
        case _:
            print("Opció incorrecta, tria una opció dins del rang")