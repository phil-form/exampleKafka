# exo07-Année bissextile (Pseudo-Code + Python)

annee = int(input("Entrer une année : "))

if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
    print("est bissextile")
else:
    print("non bissextile")


# exo8-Lanceur de balles de tennis (Pseudo-Code + Python)

pret = bool(int(input("Le joueur est-il prêt ? ")))
panier_vide = bool(int(input("Le panier est-il vide ? ")))

if pret and not panier_vide:
    print("Lancer la balle")
elif panier_vide:
    print("Insérer une balle ")
else:
    print("Attendre que le joueur soit pret.")


# exo09-Distributeur de boissons (Pseudo-Code + Python)

select = int(input("Entrer 1) coca 2) fanta 3) eau"))

match select:
    case 1:
        print("Voici votre coca.")
    case 2:
        print("Voici votre fanta.")
    case 3:
        print("Voici votre eau.")
    case _:
        print("Le choix est invalid.")

