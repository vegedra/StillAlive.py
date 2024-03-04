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
        
        # Intro -- ta rodando lento no pc da faculdade, testa o outro main depois
        blt.delay(500)
        #sing('Forms FORM-29827281-12:', 2,1, 70)  
        #sing('Test Assessment Report', 2,2, 70)  
        #blt.delay(1500)
        play_music('res/still_alive.wav', volume=0.9)
        
        # Tela 1
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
        blt.delay(3000)
        
        # Tela 2
        
if __name__ == "__main__": 
    main()