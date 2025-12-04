


# i numeri si fanno cosi

print((2.23 + 2) / 3)

# operazioni matematiche
#
print('2 + 2', 2+2)
print('3/2', 3/2)
print('3 * 2', 3*2)
print('3 % 2', 3%2) # resto della divisione
print('2**3', 2**3) # potenza

# le stringhe si fanno o con la singola quota

print("Hello World!")

# o con la doppia
print("foaiuheifauweh")
print("asdfad")

print("Hello World!")

# se devi usare gli accapi usi le triple quote

print(
    """
    Hello World!
    asdofijaewoifj
    aweoifjaew;oijfa;eowj
    """
)

# la variabili possono contenere qualsiasi cosa

giorgia = "Giorgia Di Virgilio"
edoardo = "Edoardo Di Virgilio"

# inclusa un altra variabile

nomecorrente = edoardo

print(nomecorrente)


# boolean, True or False

print(True)
print(False)

# comparazioni

x = 80
y = 13
y = x

print("x", x)
print("y", y)

print("x > y", x > y)
print("x >= y", x >= y)
print("x == y", x == y)

# if, condizioni, l'if prende True o False come argomento

if x > y:
    print("x è maggiore di y")
elif x == y:
    print("x è uguale a y")
else:
    print("x è minore di y")

# while, prende come argomento una condizione

x = 0
while True:
    print("ciao", x)
    x += 1

    if x == 10:
        break

# lo stesso programma puo essere scritto
#

x = 0 # dobbiamo inizializzare la variabile
while x < 10: # poi controlliamo che sia minore di 10
    print("ciao", x)
    x += 1 # la incre




# forloop prende una cosa che puo essere iterata
# ed assegna ogni elemento alla variabile specificata


for x in [1, 2, 3]:
    print("list", x)

# il programma sopra puo essere scritto anche in questa maniera

x=1
print("list", x)

x=2
print("list", x)

x=3
print("list", x)
