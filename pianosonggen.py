import winsound
import random
import time

def lowc():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianolowc", winsound.SND_ASYNC)
def csharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianoc#", winsound.SND_ASYNC)
def d():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianod", winsound.SND_ASYNC)
def dsharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianod#", winsound.SND_ASYNC)
def e():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianoe", winsound.SND_ASYNC)
def f():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianof", winsound.SND_ASYNC)
def fsharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianof#", winsound.SND_ASYNC)
def g():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianog", winsound.SND_ASYNC)
def gsharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianog#", winsound.SND_ASYNC)
def a():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianoa", winsound.SND_ASYNC)
def asharp():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianoa#", winsound.SND_ASYNC)
def b():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianob", winsound.SND_ASYNC)
def highc():
    winsound.PlaySound("C:/Users/aferg/OneDrive/Desktop/Clipped WAV files/pianohighc", winsound.SND_ASYNC)

if __name__ == "__main__":
    chromatic = [lowc, csharp, d, dsharp, e, f, fsharp, g, gsharp, a, asharp, b, highc]
    cmajor = [lowc, d, e, f, g, a, b, highc]
    dmajor = [d, e, fsharp, g, a, b, csharp]
    emajor = [e, fsharp, gsharp, a, b, csharp, dsharp]
    fmajor = [f, g, a, asharp, lowc, d, e, f]
    gmajor = [g, a, b, lowc, d, e, fsharp]
    amajor = [a, b, csharp, d, e, fsharp, gsharp]
    bmajor = [b, csharp, dsharp, e, fsharp, gsharp, asharp]
    iterator = 10
    while iterator >= 0:
        random.choice(fmajor)()
        time.sleep(2)
        iterator = iterator - 1