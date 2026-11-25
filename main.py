import random

meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado",
    "COOKED": "Estar acabado, en problemas o sin salida.",
    "BRO": "Es la abreviatura de brother (hermano) y se usa de forma informal como 'amigo', 'che', 'loco' o 'boludo' (en confianza)",
    "AURA": "Nivel de presencia, facha o respeto que impone alguien (se suele decir ganó/perdió puntos de aura)"
}

# Saludo e instrucciones
print("¡Hola! Bienvenido al Diccionario de Memes y Jerga de Internet.")
print("Instrucciones: Escribe una palabra que no entiendas y te diré qué significa.")
print("Podrás hacer hasta 5 consultas seguidas.")
print()

# Bucle que repite el proceso 5 veces
for i in range(5):
    word = input("Intento " + str(i + 1) + "/5 - Escribe una palabra: ").upper().strip()

    if word in meme_dict:
        print("Significado: " + meme_dict[word])
    else:
        print("Hermano, esa palabra no está, prueba con esta:")
        print(random.choice(list(meme_dict.keys())))
    
    print("-" * 40)

print("¡Listo! Ya usaste tus 5 consultas. ¡Nos vemos!")
