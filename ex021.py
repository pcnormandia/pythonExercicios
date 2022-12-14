from pygame import mixer
print('Programa Adea 0.1')
mixer.init()
mixer.music.load("ex021.mp3")
mixer.music.set_volume(0.9)
mixer.music.play()
while True:
    print('Pressione P para pausa, R para continuar, E para sair do programa: ')
    query = input(' ')

    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break

