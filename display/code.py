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
import illenium

display1 = neopixel.NeoPixel(board.D17, 1536, brightness=0.05, auto_write=False)
display2 = neopixel.NeoPixel(board.D18, 1536, brightness=0.05, auto_write=False)

def play(animation, times):
    for i in range(times):
        for frame in animation.gif:
            for i in range(len(frame)):
                display1[i] = frame[i]
                display2[i] = frame[i]
            display1.show()
            display2.show()

while True:
    play(mario1, 3)
    play(illenium, 1)
    play(pikachu2, 5)
    play(toad, 3)
    play(ricardo, 1)
    play(alien1, 1)
