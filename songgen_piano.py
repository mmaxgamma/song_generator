import winsound
import random
import time

def lowc():
    winsound.PlaySound("pianolowc", winsound.SND_ASYNC)
def csharp():
    winsound.PlaySound("pianoc#", winsound.SND_ASYNC)
def d():
    winsound.PlaySound("pianod", winsound.SND_ASYNC)
def dsharp():
    winsound.PlaySound("pianod#", winsound.SND_ASYNC)
def e():
    winsound.PlaySound("pianoe", winsound.SND_ASYNC)
def f():
    winsound.PlaySound("pianof", winsound.SND_ASYNC)
def fsharp():
    winsound.PlaySound("pianof#", winsound.SND_ASYNC)
def g():
    winsound.PlaySound("pianog", winsound.SND_ASYNC)
def gsharp():
    winsound.PlaySound("pianog#", winsound.SND_ASYNC)
def a():
    winsound.PlaySound("pianoa", winsound.SND_ASYNC)
def asharp():
    winsound.PlaySound("pianoa#", winsound.SND_ASYNC)
def b():
    winsound.PlaySound("pianob", winsound.SND_ASYNC)
def highc():
    winsound.PlaySound("pianohighc", winsound.SND_ASYNC)

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