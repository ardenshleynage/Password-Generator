import random
import string

print('\nBienvenue sur cette application de générateur de mots de passe :\n')

while True:
    user_choice = input('Choisissez le niveau de complexité : \n1- Faible\n2- Moyenne\n3- Élevée\n4- Quitter\n') 

    try:
        user_choice = int(user_choice)
        
        if user_choice < 1 or user_choice > 4:
            print('Veuillez entrer un nombre entier entre 1 et 4.\n')
        elif user_choice ==4 :
            while True:
                quit_choice = input("Voulez-vous quitter l'application ? \n1- Oui\n2- Non\n")

                try:
                    quit_choice = int(quit_choice)
                    
                    if quit_choice == 1:
                        print("Merci d'avoir utilisé l'application. Au revoir !")
                        exit() 
                    elif quit_choice == 2:
                        break
                    else:
                        print("Veuillez entrer 1 pour Oui ou 2 pour Non.\n")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide (1 ou 2).\n")
            
        else:
            if user_choice == 1:
                max_lenght_low = random.randint(6, 8)
                caracteres_low = string.ascii_letters
                password_low = ''.join(random.choice(caracteres_low) for i in range(max_lenght_low))
                print(f"Votre mot de passe généré (faible) est : {password_low}")
            elif user_choice == 2:
                max_lenght_mid = random.randint(8, 12)
                caracteres_mid = string.ascii_letters + string.digits
                password_mid = ''.join(random.choice(caracteres_mid) for i in range(max_lenght_mid))
                print(f"Votre mot de passe généré (moyen) est : {password_mid}")
            elif user_choice == 3:
                max_lenght_hard = random.randint(12, 20)
                caracteres_hard = string.ascii_letters + string.digits + string.punctuation
                password_hard = ''.join(random.choice(caracteres_hard) for i in range(max_lenght_hard))
                print(f"Votre mot de passe généré (élevé) est : {password_hard}")

            while True:
                quit_choice = input("Voulez-vous générer d'autre mots de passe ? \n1- Oui\n2- Non\n")

                try:
                    quit_choice = int(quit_choice)
                    
                    if quit_choice == 1:
                        print("Vous pouvez générer un autre mot de passe.\n")
                        break                       
                    elif quit_choice == 2:
                        print("Merci d'avoir utilisé l'application. Au revoir !")
                        exit()
                    else:
                        print("Veuillez entrer 1 pour Oui ou 2 pour Non.\n")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide (1 ou 2).\n")

    except ValueError:
        print("Erreur : veuillez entrer un nombre valide.\n")
