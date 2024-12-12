import random

# Dictionnaire des régions et chefs-lieux
REGIONS = {
    "Agneby-Tiassa": "Agboville",
    "Bélier": "Yamoussoukro",
    "Cavally": "Guiglo",
    "Gbêkê": "Bouaké",
    "Indénié-Djuablin": "Abengourou",
    "Nawa": "Soubré",
    "Poro": "Korhogo",
    "San-Pedro": "San-Pedro",
    "Tonkpi": "Man",
    "Zanzan": "Bondoukou"
}

def jouer_partie():
    scores = []
    
    while True:
        # Afficher les meilleurs scores
        print("\n Meilleurs Scores ")
        for i, score in enumerate(sorted(scores, reverse=True)[:5], 1):
            print(f"{i}. {score}/10")
        
        # Initialiser la partie
        score_partie = 0
        questions_posees = set()
        
        # 10 questions
        for tour in range(1, 11):
            # Choisir une région unique
            while True:
                region = random.choice(list(REGIONS.keys()))
                if region not in questions_posees:
                    questions_posees.add(region)
                    break
            
            # Poser la question
            print(f"\nQuestion {tour}/10 : Quel est le chef-lieu de {region} ?")
            reponse = input("Votre réponse : ").strip()
            
            # Vérifier la réponse
            if reponse.lower() == REGIONS[region].lower():
                print("Bonne réponse !")
                score_partie += 1
            else:
                print(f" Mauvaise réponse. Le chef-lieu est {REGIONS[region]}.")
        
        # Résultat de la partie
        print(f"\n Fin du jeu ! Votre score : {score_partie}/10")
        scores.append(score_partie)
        
        # Rejouer ?
        if input("\nVoulez-vous rejouer ? (O/N) : ").upper() != 'O':
            break

# Lancer le jeu
print("🇨🇮 JEU DES RÉGIONS DE CÔTE D'IVOIRE 🇨🇮")
jouer_partie()