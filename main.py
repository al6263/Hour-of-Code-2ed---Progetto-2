# Setup: popola il dizionario "rubrica" con dei valori finti generati online

from ottieni_rubrica import ottieni_rubrica
rubrica = ottieni_rubrica()

#############################################################################
# Definisci qui i tuoi comandi

def termina():
    """Termina programma"""

    global continua
    print("Grazie per avere usato la mia rubrica!")
    continua = False


def aggiungi():
    """aggiungi un contatto"""
    nome = input("nome del contatto -> ")
    cognome = input("cognome del contatto -> ") 
    email = input("email del contatto -> ") 
    num_casa = input("numero di casa del contatto -> ") 
    num_cell = input("numero di cellulare del contatto -> ") 

    nuovo_contatto = {
            "nome" : nome,
            "cognome" : cognome, 
            "email" : email, 
            "telefono" : {
                "casa" : num_casa,
                "cellulare" : num_cell
                }
            }

    rubrica[str(nuovo_id)] = nuovo_contatto
    rubrica += 1
    print(f"ho aggiunto {nome} {cognome} alla tua rubrica!") 




def modifica():
    """modifica un contatto"""
    global rubrica 

    id = input("inserisci l'id del contatto da modificare: ") 
    if id in rubrica: 

        contatto = rubrica[id]
        nome = input(f"nome contatto ({contatto['nome']}): ")
        if nome == "": 
            nome = contatto["nome"]
        cognome = input(f"cognome contatto ({contatto['cognome']}): ")
        if cognome == "":
            cognome = contatto["cognome"]
        email = input(f"email contatto ({contatto['email']}): ")
        if email == "": 
            email = contatto["email"]
        num_casa = input(f"numero di casa del contatto({contatto['telefono']['casa']}): ")
        if num_casa == "":
            num_casa = contatto["telefono"]["casa"]
        num_cell = input(f"numero di cellulare del contatto ({contatto['telefono']['cellulare']}): ")
        if num_cell == "":
            num_cell = contatto["telefono"]["casa"]

        nuovo_contatto = {
                "nome" : nome, 
                "cognome" : cognome, 
                "email" : email, 
                "telefono": {
                    "numero di casa" : num_casa,
                    "numero di cellulare" : num_cell
                    }
                }

        rubrica[id] = nuovo_contatto
        print(f"ho modificato {nome} {cognome} nella tura rubrica!")
    else:
        print("id non valido")



def ricerca():
    """cerca un contatto"""
    global rubrica 

    print("chi stai cercando?").lower 
    
    lista = []

    for id, contatto in rubrica.items():
        if stringa in contatto['nome'] or (stringa in contatto['cognome']) or (stringa in contatto['nome'] + " " + contatto['cognome'])): 
            lista.append({id, contatto})
            if len(lista) > 0:
                for id, contatto in lista:
                    print(id, ":", contatto['nome'], contatto['congome'])


            else:
                print("non ho trovato nessun contatto...")
        


###################################################################################################

comandi = [
    # Aggiungi qui i tuoi comandi
    termina,
    aggiungi,
    modifica,
    ricerca
]

continua = True

while continua:
    print("-"*20)
    print("GESTIONE RUBRICA - Comandi disponibili:\n")
    for indice, comando in enumerate(comandi):
        print(f"[{indice}]", "-", comando.__doc__)
    print("\n"+"-"*20)
    i = input("Quale comando vuoi usare? ")
    try:
        i = int(i)
        if i<0 or i>=len(comandi):
            print("Indice fuori range!\n\n")
            continue
        else:
            print("\n\n")
            comandi[i]()
    except Error as a:
        print("Error")
        continue
