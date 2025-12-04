# ============================================
# PARTE 1: CICLI FOR - BASE
# ============================================

print("=== ESERCIZIO 1: Stampa numeri da 1 a 5 ===")
# TODO: Usa un ciclo for con range() per stampare i numeri da 1 a 5
# IL TUO CODICE QUI:


for x in [
    1,
    2,
    3,
    4,
    5,
]:
    print(x)


print("\n=== ESERCIZIO 2: Stampa ogni lettera ===")
# TODO: Usa un ciclo for per stampare ogni lettera in "PYTHON"
word = "PYTHON"
# IL TUO CODICE QUI:


print("\n=== ESERCIZIO 3: Somma di numeri ===")
# TODO: Calcola la somma dei numeri da 1 a 10 usando un ciclo for
total = 0
# IL TUO CODICE QUI:


print(f"Somma: {total}")


# ============================================
# PARTE 2: TIPI BASE - LISTE E STRINGHE
# ============================================

print("\n=== ESERCIZIO 4: Lista di frutti ===")
fruits = ["apple", "banana", "cherry", "date"]
# TODO: Stampa ogni frutto con il suo numero di posizione (partendo da 1)
# Esempio output: "1. apple"
# IL TUO CODICE QUI:


print("\n=== ESERCIZIO 5: Conta le vocali ===")
# TODO: Conta quante vocali ci sono in questa frase
sentence = "I love learning Python"
vowels = "aeiouAEIOU"
count = 0
# IL TUO CODICE QUI:


print(f"Numero di vocali: {count}")


# ============================================
# PARTE 3: CICLI WHILE
# ============================================

print("\n=== ESERCIZIO 6: Conto alla rovescia ===")
# TODO: Crea un conto alla rovescia da 5 a 1 usando un ciclo while, poi stampa "Decollo!"
n = 5
# IL TUO CODICE QUI:


print("\n=== ESERCIZIO 7: Indovina il numero ===")
# TODO: Continua a chiedere input finché l'utente indovina il numero segreto (7)
# Suggerimento: Usa while True e break quando è corretto
secret = 7
# IL TUO CODICE QUI (decommenta quando sei pronto per testare):
# while True:
#     guess = int(input("Indovina un numero tra 1 e 10: "))
#     # La tua logica qui


print("\n=== ESERCIZIO 8: Raddoppia fino a 100 ===")
# TODO: Inizia con 1, continua a raddoppiare finché il numero supera 100
number = 1
# IL TUO CODICE QUI:


# ============================================
# PARTE 4: COMBINARE I CONCETTI
# ============================================

print("\n=== ESERCIZIO 9: Solo numeri pari ===")
numbers = [3, 7, 12, 18, 5, 22, 9, 14]
# TODO: Usa un ciclo for per stampare solo i numeri pari
# IL TUO CODICE QUI:


print("\n=== ESERCIZIO 10: Costruisci una stringa ===")
# TODO: Usa un ciclo for per costruire una stringa con asterischi
# Stampa: *, **, ***, ****, *****
# IL TUO CODICE QUI:


# ============================================
# ESERCIZI BONUS
# ============================================

print("\n=== BONUS 1: Tabellina ===")
# TODO: Stampa la tabellina del 7 (7 x 1 fino a 7 x 10)
# IL TUO CODICE QUI:


print("\n=== BONUS 2: Inverti una parola ===")
word = "PYTHON"
reversed_word = ""
# TODO: Inverti la parola usando un ciclo for (non usare word[::-1])
# IL TUO CODICE QUI:


print(f"Invertita: {reversed_word}")
