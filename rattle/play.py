from pygame import mixer

def play_song(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.set_volume(0.5)
    mixer.music.play()

    while True:
        print("Press P to pause, R to resume and E to exit the program")
        query = input(" ")

        if query == 'p':
            mixer.music.pause()
        elif query == 'r':
            mixer.music.unpause()
        elif query == 'e':
            mixer.music.stop()
            break

