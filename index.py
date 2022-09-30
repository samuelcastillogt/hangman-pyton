import os
import random
solucion = []
word =[]
letter_index_dict = {}
def run():
    os.system("cls")
    lista = []
    vidas = 5
    with open("./data.txt", "r", encoding="utf-8") as f:
        for palabra in f:
            lista.append(palabra.replace("\n", ""))
        f.close()
    palabra = random.choice(lista)
    palabra_separada = [i for i in palabra]
    word = ["__"] * len(palabra)
    indice_letras = {}
    for indice, letter in enumerate(palabra_separada):
        if not indice_letras.get(letter): 
            indice_letras[letter] = []
        indice_letras[letter].append(indice)
    print(indice_letras)
    if vidas > 0:
        while vidas > 0:
            os.system("cls")
            print("""
             _                                             
            | |                                            
            | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                __/ |                      
                               |___/   

            Proyecto de Samuel Castillo
            https://samuelcastillogt.github.io         
        """)
            print("Encuentra la palabra o moriras")
            print("Tienes " + str(vidas) + " intentos restantes")
            for espacio in word:
                print(espacio + " ", end="")
            print("\n")    
            letter = input("Ingresa una letra: ").strip()
            print(letter)
            assert letter.isalpha() 

            if letter in palabra_separada:
                for idx in indice_letras[letter]:
                    word[idx] = letter
            else:
                vidas = vidas - 1
           

            if "__" not in word:
                os.system("cls") 
                print("¡Ganaste! La palabra era", palabra)
                break
        print("""
                   ...
                 ;::::;
               ;::::; :;
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
         ;:::::::::`. ,,,;.        /  / DOOOOOO
       .';:::::::::::::::::;,     /  /     DOOOO
      ,::::::;::::::;;;;::::;,   /  /        DOOO
     ;`::::::`'::::::;;;::::: ,#/  /          DOOO
     :`:::::::`;::::::;;::: ;::#  /            DOOO
     ::`:::::::`;:::::::: ;::::# /              DOO
     `:`:::::::`;:::::: ;::::::#/               DOO
      :::`:::::::`;; ;:::::::::##                OO
      ::::`:::::::`;::::::::;:::#                OO
      `:::::`::::::::::::;'`:;::#                O
       `:::::`::::::::;' /  / `:#
        ::::::`:::::;'  /  /   `#""")
if __name__ == "__main__":
    run()