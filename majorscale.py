import winsound
import random

def lowc():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianolowc", winsound.SND_FILENAME)
def csharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianoc#", winsound.SND_FILENAME)
def d():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianod", winsound.SND_FILENAME)
def dsharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianod#", winsound.SND_FILENAME)
def e():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianoe", winsound.SND_FILENAME)
def f():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianof", winsound.SND_FILENAME)
def fsharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianof#", winsound.SND_FILENAME)
def g():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianog", winsound.SND_FILENAME)
def gsharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianog#", winsound.SND_FILENAME)
def a():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianoa", winsound.SND_FILENAME)
def asharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianoa#", winsound.SND_FILENAME)
def b():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianob", winsound.SND_FILENAME)
def highc():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianohighc", winsound.SND_FILENAME)

if __name__ == "__main__":
    chromatic = [lowc, csharp, d, dsharp, e, f, fsharp, g, gsharp, a, asharp, b, highc]
    iterator = 10
    while iterator >= 0:
        random.choice(chromatic)()
        iterator = iterator - 1