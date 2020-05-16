from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player == "piedra":
        if ai == options[0]:
            return "Empate!"
        elif ai == options[1]:
            return "Perdiste!"
        elif ai == options[2]:
            return "Ganaste!"
    elif player == "papel":
        if ai == options[0]:
            return "Ganaste!"
        elif ai == options[1]:
            return "Empate!"
        elif ai == options[2]:
            return "Perdiste!"
    elif player == "tijeras":
        if ai == options[0]:
            return "Perdiste!"
        elif ai == options[1]:
            return "Ganaste!"
        elif ai == options[2]:
            return "Empate!"
