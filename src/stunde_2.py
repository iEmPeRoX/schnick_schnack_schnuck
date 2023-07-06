
def wilkommen(name):
    print("Herzlich Willkommen "+name+"!")



def abfrage():
    name=input("Wie heißt du?")
    alter=input("Wie alt bist du?")
    if int(alter)<18:
        print("Haben dir das deine Eltern erlaubt?")
        antwort=input()
        if antwort=="ja":
            wilkommen(name)
        else: print("Zugriff verweigert!")

    else: wilkommen(name)

abfrage()

