from bearlibterminal import terminal as blt
from pygame import mixer
import sys
import time

# Abre o blt e o configura: se pode ser arrastado, o titulo da janela e de onde vem o input
blt.open()
blt.set("""
    window.resizeable=false;
    window.title='Still Alive';
    input: filter={keyboard};
    window.size=110x39;
""")

# Função para mostrar as artes em ASCII
def art(file_path, x, y):
    try:
        # Pega a arte do arquivo .txt e printa na tela
        with open(file_path, 'r') as file:
            content = file.read()
            blt.printf(x, y, content)
    except UnicodeDecodeError:
        print("Erro, verifique se o .txt existe ou usa caracteres especiais.")
        
# Função para tocar a música
def play_music(file_path, volume=0.8):
    mixer.init()
    mixer.music.stop()
    mixer.music.load(file_path)
    mixer.music.set_volume(volume)
    mixer.music.play()
    
# Função para mostrar  o texto como se alguem estivesse digitando no tempo certo
def sing(text, x, y, tempo):
    # Posição do texto
    cursor_x = x
    cursor_y = y
    frequency = 0.5
    
    # Loop que faz as letras aparecerem todo x millisegundo junto com o _
    for c in text:
        if time.time() % frequency < frequency / 2:
            blt.print(cursor_x, cursor_y, c + "_")
        else:
            blt.print(cursor_x, cursor_y, c)
        blt.refresh()
        
        blt.delay(tempo)
        
        # Remove o _
        blt.print(cursor_x, cursor_y, c)
        blt.refresh()
        cursor_x += 1
        blt.print(cursor_x, cursor_y, " ")
        blt.refresh()
        
        if blt.has_input():
            # Caso o usuario queira sair
            key = blt.read()
            if key in (blt.TK_CLOSE, blt.TK_5, blt.TK_ESCAPE):
                sys.exit()

# Cria a tela principal, definindo suas principais caracteristicas
def main():
    blt.clear()
    blt.refresh()
    blt.color('#FFB000')
    blt.bkcolor('black')
    blt.refresh()
    
    # Loop
    while True:
        # TODO: Menuzinho na caixa da direita com algumas configurações e pra dar play
        blt.clear()
        art('res/frame.txt', 1, 0)
        
        # Intro -- ta rodando lento no pc da faculdade, nao sei oq fazer pra arrumar
        blt.delay(500)
        #sing('Forms FORM-29827281-12:', 2,1, 70)  
        #sing('Test Assessment Report', 2,2, 70)  
        #blt.delay(1500)
        play_music('res/still_alive.mp3', volume=0.9)
        
        # Tela 1
        blt.printf(69, 5, "Still Alive in Python")
        blt.printf(71, 7, "By Pedro Ivo, 2024")
        blt.refresh()
        sing('This was a triumph.', 2,5, 70)  # Quanto maior o numero no final, mais lento o texto
        blt.delay(2000)
        sing("I'm making a note here:", 2,6, 65)
        sing("HUGE SUCCESS.", 2,7, 80)
        blt.delay(1750)
        sing("It's hard to overstate", 2,8, 95)
        sing("my satisfaction.", 2,9, 100)
        blt.delay(2000)
        
        art('res/aperture.txt', 59, 18)
        sing('Aperture Science', 2,10, 70)
        blt.delay(2400)
        sing('We do what we must', 2,11, 70)
        sing('because we can.', 2,12, 69)
        blt.delay(2000)
        sing('For the good of all of us.', 2,13, 88)
        blt.clear_area(59, 18, 50, 20)
        art('res/nuclear.txt', 59, 18)
        sing('Except the ones who are dead.', 2,14, 50)
        
        blt.clear_area(59, 18, 50, 20)
        art('res/aperture.txt', 59, 18)
        sing("But there's no sense crying", 2,16, 50)
        sing("over every mistake.", 2,17, 50)
        sing("You just keep on trying", 2,18, 50)
        sing("till you run out of cake.", 2,19, 50)
        blt.clear_area(59, 18, 50, 20)
        art('res/science.txt', 59, 18)
        sing("And the Science gets done.", 2,20, 50)
        sing("And you make a neat gun.", 2,21, 50)
        blt.clear_area(59, 18, 50, 20)
        art('res/aperture.txt', 59, 18)
        sing("For the people who are", 2,22, 50)
        sing("still alive.", 2,23, 70)
        blt.delay(2000)
        
        # Tela 2
        blt.clear_area(2, 1, 50, 30)
        sing('Forms FORM-55551-5:', 2,1, 20)  
        sing('Personnel File Addendum:', 2,2, 20)  
        
        sing('Dear <<Subject Name Here>>,', 2,4, 35)  
        sing("I'm not even angry.", 2,6, 70)  
        blt.delay(2700)
        sing("I'm being so sincere right now.", 2,7, 80)  
        sing("Even though you broke my heart.", 2,8, 85)  
        sing("And killed me.", 2,9, 80)  
        sing("And tore me to pieces.", 2,10, 70)  
        sing("And threw every piece into a fire.", 2,11, 70)  
        sing("As they burned it hurt because.", 2,12, 70)  
        sing("I was so happy for you!", 2,13, 70)  
        sing("Now these points of data", 2,14, 70)  
        sing("make a beautiful line.", 2,15, 70)  
        sing("And we're out of beta.", 2,16, 70)  
        sing("We're releasing on time.", 2,17, 70)  
        sing("So i'm GLaD. I got burned.", 2,18, 70)  
        sing("Think of all the things we learned", 2,19, 70)  
        sing("for the people who are", 2,20, 70)  
        sing("still alive.", 2,21, 70)  
        
        # Tela 3
        sing('Forms FORM-55551-6:', 2,1, 70)  
        sing('Personnel File Addendum Addendum:', 2,2, 70) 
        
        sing("One last thing:", 2,4, 70)  
        
if __name__ == "__main__": 
    main()