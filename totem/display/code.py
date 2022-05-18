import board
import neopixel
import toad
import pikachu
import dinosaur
import alien1
#import excision
import pepe
import mario1
import pikachu2
#import ricardo
import illenium
import spongebob
import squirtle
import winnie

pixels = neopixel.NeoPixel(board.D18, 1536, brightness=0.1, auto_write=False)

def play(animation, times):
    for i in range(times):
        for frame in animation.gif:
            for i in range(len(frame)):
                pixels[i] = frame[i]
            pixels.show()

while True:
    play(spongebob, 70)
    play(squirtle, 25)
    play(winnie, 6)
    play(mario1, 30)
    #play(illenium, 2)
    play(pikachu2, 65)
    play(toad, 22)
    #play(pepe, 2)
    #play(ricardo, 1)
    play(alien1, 10)
