import simpleaudio as sa
import time
from stopwatch import Stopwatch

son = sa.WaveObject.from_wave_file("186942__lemoncreme__piano-melody.wav")

debut = time.time()
for e in range(8) :

    time.sleep(.2)
    son_joue.stop()
fin = time.time()
print(debut, fin, fin-debut)


