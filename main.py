from bearlibterminal import terminal as blt
import time
import sys
from pygame import mixer

# Abre o BLT e faz as configurações básicas
blt.open()
blt.set("""
    window.resizeable=false;
    window.title='Still Alive';
    input: filter={keyboard};
    window.size=110x39;
    window.cellsize=9x15;
""")

# Função que mostra as artes ASCII
def art(file_path, x, y):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            blt.printf(x, y, content)
    except UnicodeDecodeError:
        print("Error: Check if the .txt file exists or contains special characters.")

# Função que toca a música
def play_music(file_path, volume=0.8):
    mixer.init()
    mixer.music.stop()
    mixer.music.load(file_path)
    mixer.music.set_volume(volume)
    mixer.music.play()

# Função que mostra o texto como se estivesse sendo digitado, também cuida do input para fechar o programa
def sing(text, x, y, tempo):
    # Posição do texto e outras variaveis
    cursor_x = x
    cursor_y = y
    frequency = 0.5
    start_time = time.perf_counter()

    # Loop que faz as letras aparecerem todo x millisegundo junto com o _
    for i, c in enumerate(text):
        elapsed_time = time.perf_counter() - start_time
        if elapsed_time % frequency < frequency / 2:
            blt.print(cursor_x, cursor_y, c + "_")
        else:
            blt.print(cursor_x, cursor_y, c)
        blt.refresh()

        blt.delay(tempo)

        # Remove o "_"
        blt.print(cursor_x, cursor_y, c)
        blt.refresh()
        cursor_x += 1
        blt.print(cursor_x, cursor_y, " ")
        blt.refresh()

        # Caso o usuario queira sair
        if blt.has_input():
            key = blt.read()
            if key in (blt.TK_CLOSE, blt.TK_ESCAPE):
                sys.exit()

def main():
    blt.clear()
    blt.refresh()
    blt.color('#FFB000')
    blt.bkcolor('black')
    art('res/frame.txt', 1, 0)
    blt.printf(69, 3, "Still Alive in Python")
    blt.printf(71, 5, "By Pedro Ivo, 2024")
    blt.refresh()

    # Main Loop
    while (blt.TK_CLOSE != True):
      blt.printf(74, 10, "1) Play")
      blt.printf(74, 11, "2) Settings")
      blt.printf(74, 12, "3) Exit")
      blt.refresh()
        
      key = blt.read()
      
      if key in (blt.TK_CLOSE, blt.TK_3, blt.TK_ESCAPE):
        sys.exit()
        
      elif (key == blt.TK_2):
        blt.clear_area(70, 10, 20, 5)
        blt.printf(77, 11, "INDEV")
        blt.refresh()
        blt.delay(2000)
        main()
      
      elif (key == blt.TK_1):
        play_music('res/still_alive.mp3', volume=0.9)
        blt.clear_area(70, 10, 20, 5)
        #blt.clear()
        
        #blt.delay(500)
        #sing('Forms FORM-29827281-12:', 2,1, 70)  
        #sing('Test Assessment Report', 2,2, 70)  
        #blt.delay(1500)

        # Tela 1
        sing('This was a triumph.', 2, 5, 70)
        time.sleep(2)
        sing("I'm making a note here:", 2, 6, 65)
        sing("HUGE SUCCESS.", 2, 7, 80)
        time.sleep(1.75)
        sing("It's hard to overstate", 2, 8, 95)
        sing("my satisfaction.", 2, 9, 100)
        time.sleep(2)

        art('res/aperture.txt', 59, 18)
        sing('Aperture Science', 2, 10, 70)
        time.sleep(2.4)
        sing('We do what we must', 2, 11, 70)
        sing('because we can.', 2, 12, 69)
        time.sleep(2)
        sing('For the good of all of us.', 2, 13, 88)
        blt.clear_area(59, 18, 50, 20)
        art('res/nuclear.txt', 59, 18)
        sing('Except the ones who are dead.', 2, 14, 50)

        blt.clear_area(59, 18, 50, 20)
        art('res/aperture.txt', 59, 18)
        sing("But there's no sense crying", 2, 16, 50)
        sing("over every mistake.", 2, 17, 50)
        sing("You just keep on trying", 2, 18, 50)
        sing("till you run out of cake.", 2, 19, 50)
        blt.clear_area(59, 18, 50, 20)
        art('res/science.txt', 59, 18)
        sing("And the Science gets done.", 2, 20, 50)
        sing("And you make a neat gun.", 2, 21, 50)
        blt.clear_area(59, 18, 50, 20)
        art('res/aperture.txt', 59, 18)
        sing("For the people who are", 2, 22, 50)
        sing("still alive.", 2, 23, 70)
        time.sleep(2)
        
        # Tela 2
        blt.clear_area(2, 1, 50, 30)
        sing('Forms FORM-55551-5:', 2,1, 20)  
        sing('Personnel File Addendum:', 2,2, 20)  
        sing('Dear <<Subject Name Here>>,', 2,4, 35)  
        
        sing("I'm not even angry.", 2,6, 70)  
        time.sleep(2.7)
        sing("I'm being so sincere right now.", 2,7, 80) 
        time.sleep(1.6)        
        sing("Even though you broke my heart.", 2,8, 85)  
        sing("And killed me.", 2,9, 80)  
        time.sleep(2)  
        sing("And tore me to pieces.", 2,10, 70)  
        time.sleep(2)  
        sing("And threw every piece into a fire.", 2,11, 80)  
        time.sleep(1.6)  
        sing("As they burned it hurt because.", 2,12, 70)  
        sing("I was so happy for you!", 2,13, 70)  
        time.sleep(0.5)  
        sing("Now these points of data", 2,14, 60)  
        sing("make a beautiful line.", 2,15, 60)  
        sing("And we're out of beta.", 2,16, 60)  
        sing("We're releasing on time.", 2,17, 60)  
        sing("So i'm GLaD. I got burned.", 2,18, 60)  
        sing("Think of all the things we learned", 2,19, 60)  
        sing("for the people who are", 2,20, 60)  
        sing("still alive.", 2,21, 60)  
        time.sleep(1)  
        
        # Tela 3
        blt.clear_area(2, 1, 50, 30)
        sing('Forms FORM-55551-6:', 2,1, 20)  
        sing('Personnel File Addendum Addendum:', 2,2, 20) 
        
        sing("One last thing:", 2,4, 30)  
        
        blt.clear()
        main()

if __name__ == "__main__":
    main()

