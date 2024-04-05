from bearlibterminal import terminal as blt
import time
import sys
from pygame import mixer

# Open BLT and configure settings
blt.open()
blt.set("""
    window.resizeable=false;
    window.title='Still Alive';
    input: filter={keyboard};
    window.size=110x39;
""")

# Function to display ASCII art
def art(file_path, x, y):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            blt.printf(x, y, content)
    except UnicodeDecodeError:
        print("Error: Check if the .txt file exists or contains special characters.")

# Function to play music
def play_music(file_path, volume=0.8):
    mixer.init()
    mixer.music.stop()
    mixer.music.load(file_path)
    mixer.music.set_volume(volume)
    mixer.music.play()

def read_lyrics(file_path):
    with open(file_path, 'r') as file:
        lyrics = []
        for line in file:
            line = line.strip()
            if line:
                lyric, tempo = line.rsplit(',', 1)
                lyrics.append((lyric, int(tempo)))
        return lyrics

def sing(lyrics, x, y):
    cursor_x = x
    cursor_y = y
    frequency = 0.5
    start_time = time.perf_counter()

    for lyric, tempo in lyrics:
        cursor_x = x  # Reset cursor position at the beginning of each lyric
        elapsed_time = time.perf_counter() - start_time
        
        for c in lyric:
            if elapsed_time % frequency < frequency / 2:
                blt.print(cursor_x, cursor_y, c + "_")
            else:
                blt.print(cursor_x, cursor_y, c)
            blt.refresh()

            blt.delay(tempo)

            blt.print(cursor_x, cursor_y, c)
            blt.refresh()
            cursor_x += 1
            blt.print(cursor_x, cursor_y, " ")
            blt.refresh()

            if blt.has_input():
                key = blt.read()
                if key in (blt.TK_CLOSE, blt.TK_5, blt.TK_ESCAPE):
                    sys.exit()
                    
            elapsed_time = time.perf_counter() - start_time  # Update elapsed time after each character

        cursor_y += 1  # Move to the next line for the next lyric

# Main function
def main():
    blt.clear()
    blt.refresh()
    blt.color('#FFB000')
    blt.bkcolor('black')
    blt.refresh()
    play_music('res/still_alive.mp3', volume=0.9)

    while True:
        blt.clear()
        art('res/frame.txt', 1, 0)
        lyrics = read_lyrics('lyrics.txt')

        sing(lyrics, 2, 5)
        blt.delay(2000)
        sing(lyrics, 2, 6)
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
        time.sleep(3)

if __name__ == "__main__":
    main()

