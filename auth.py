import bcrypt

# Charger le mot de passe hashé depuis un fichier (s'il existe)
try:
    with open("master_password.txt", "r") as file:
        stored_hashed_password = file.read().encode() #.read est en str donc on converti en bytes
except FileNotFoundError:
    stored_hashed_password = None

if stored_hashed_password is None:
    # Demander à l'utilisateur de créer un master password
    master_password = input("Set a master password: ").encode()
    hashed_master_password = bcrypt.hashpw(master_password, bcrypt.gensalt())

    # Sauvegarder le mot de passe hashé dans un fichier
    with open("master_password.txt", "w") as file:
        file.write(hashed_master_password.decode())  # Décoder en string avant d'écrire dans le file
    print("Master password is set and saved!")
else:
    # Si un master password existe, demander à l'utilisateur de s'authentifier
    entered_password = input("Enter your master password: ").encode()
    if bcrypt.checkpw(entered_password, stored_hashed_password): # on verifie ici si c'est le même
        print("the access is granted")
    else:
        print("the access is denied")
