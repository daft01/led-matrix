import board
import neopixel
import toad
import pikachu
import dinosaur
import alien1
import excision
import mario1
import pikachu2
import ricardo
import squidGames
import illenium

pixels = neopixel.NeoPixel(board.D18, 1536, brightness=0.05, auto_write=False)

def play(animation, times):
    for i in range(times):
        for frame in animation.gif:
            for i in range(len(frame)):
                pixels[i] = frame[i]
            pixels.show()

while True:
    play(mario1, 3)
    play(illenium, 1)
    play(pikachu2, 5)
    play(toad, 3)
    play(ricardo, 1)
    play(alien1, 1)
