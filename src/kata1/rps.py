from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player == "Piedra":
        if ai == "Piedra":
            return "Empate"
        elif ai == "Papel":
            return "AI"
        elif ai == "Tijeras":
            return "Player"
    elif player == "Papel":
        if ai == "Piedra":
            return "Player"
        elif ai == "Papel":
            return "Empate"
        elif ai == "Tijeras":
            return "AI"
    elif player == "Tijeras":
        if ai == "Piedra":
            return "AI"
        elif ai == "Papel":
            return "Player"
        elif ai == "Tijeras":
            return "Empate"
    

# Entry Point
def Game():
    player_choice = int(input("1-Piedra; 2-Papel; 3 - Tijeras"))
    if player_choice == 1:
         player = "Piedra"
    elif player_choice == 2:
        player = "Papel"
    elif player_choice == 3:
        player = "Tijeras"

    ai_choice = randint(1, 3)
    if ai_choice == 1:
        ai = "Piedra"
    elif ai_choice == 2:
        ai = "Papel"
    elif ai_choice == 3:
        ai = "Tijeras"

    
    winner = quienGana(player, ai)

    print(winner)



