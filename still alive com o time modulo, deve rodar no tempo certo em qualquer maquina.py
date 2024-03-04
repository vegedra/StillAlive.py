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
    window.size=107x34;
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
    
def sing(text, x, y, tempo):
    cursor_x = x
    cursor_y = y
    frequency = 0.5

    start_time = time.perf_counter()
    
    for c in text:
        elapsed_time = time.perf_counter() - start_time
        target_time = elapsed_time + frequency
        
        while time.perf_counter() < target_time:
            blt.printf(cursor_x, cursor_y, c + "_")
            blt.refresh()
            blt.delay(1)  # You can adjust this delay value based on your preference

        blt.print(cursor_x, cursor_y, c)
        blt.refresh()
        cursor_x += 1
        blt.print(cursor_x, cursor_y, " ")
        blt.refresh()

        start_time = time.perf_counter()

        if blt.has_input():
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
        blt.clear()
        art('res/frame.txt', 1, 0)
        
        # Intro
        blt.delay(500)
        # Ta rodando lento no pc da faculdade, vou aumentar os valores
        sing('FORMS FORM-29827281-12', 2,1, 40)  # 70
        blt.print(23, 2, " " * 4)  # Solucao temporaria pra porcaria do _ aparecendo no final dos texto, mas nao funciona
        blt.refresh()              # Essa bosta parece aparecer de forma aleatoria, tem q mexer no codigo do `sing` msm
        sing('Test Assesment Report', 2,2, 40)  # 70
        blt.delay(1500)
        play_music('res/still_alive.wav', volume=0.9)
        
        # Tela 1
        sing('This was a triumph.', 2,5, 70)
        blt.delay(2000)
        sing("I'm making a note here:", 2,6, 70)
        sing("HUGE SUCCESS.", 2,7, 80)
        blt.delay(2000)
        sing("It's hard to overstate", 2,8, 95)
        sing("My satisfaction.", 2,9, 100)
        
if __name__ == "__main__": 
    main()