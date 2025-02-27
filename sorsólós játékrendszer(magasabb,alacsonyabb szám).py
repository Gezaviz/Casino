import random

def roll_dice():
    return random.randint(1, 6)

def higher_or_lower_game():
    print("\nÜdv a 'Magasabb vagy alacsonyabb' játékban!")
    players = int(input("Hány játékos játszik? "))
    scores = [0] * players
    
    current_roll = roll_dice()
    print(f"Első dobás: {current_roll}")
    
    while True:
        for i in range(players):
            print(f"\nJátékos {i + 1}, te következel!")
            guess = input("Szerinted a következő dobás magasabb (m) vagy alacsonyabb (a) lesz? ").strip().lower()
            
            next_roll = roll_dice()
            print(f"A következő dobás: {next_roll}")
            
            if (guess == "m" and next_roll > current_roll) or (guess == "a" and next_roll < current_roll):
                print("Helyes tipp! +1 pont")
                scores[i] += 1
            else:
                print("Rossz tipp!")
            
            current_roll = next_roll
            
        print("\nAktuális pontszámok:")
        for j, score in enumerate(scores):
            print(f"Játékos {j + 1}: {score} pont")
            
        if input("Folytatjátok a játékot? (i/n) ").strip().lower() == "n":
            break
    
    print("\nJáték vége! Végső eredmények:")
    for j, score in enumerate(scores):
        print(f"Játékos {j + 1}: {score} pont")
    
if __name__ == "__main__":
    higher_or_lower_game()
