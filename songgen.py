import winsound
import random
import math


lengthsatisfy = False
while lengthsatisfy == False:
    try:
        songlength = int(input("How long in seconds do you want your song to be?\n"))
        if songlength > 0:
            lengthsatisfy = True
        else:
            raise Exception
    except:
        print("Invalid song length")

songinmilli = songlength * 1000

BPMsatisfy = False
while BPMsatisfy == False:
    try:
        BPM = int(input("Enter a BPM for your song between 60 and 120 (Beats Per Minute)\n"))
        if BPM >= 60 and BPM <= 120:
            BPMsatisfy = True
        else:
            raise Exception
    except:
        print("Invalid BPM")

keysatisfy = False
while keysatisfy == False:
    key = input("Enter a Key, i.e. 'asharpminor'\n")
    if key.lower() in ['cmajor', 'dmajor', 'emajor', 'fmajor', 'gmajor', 'amajor', 'bmajor', 'csharpmajor', 'dsharpmajor', 'fsharpmajor', 'gsharpmajor', 'asharpmajor', 'cminor', 'dminor', 'eminor', 'fminor', 'gminor', 'aminor', 'bminor', 'csharpminor', 'dsharpminor', 'fsharpminor', 'gsharpminor', 'asharpminor']:
        keysatisfy = True
    else: 
        print("Invalid Key")

elapsed = 0



c5 = 523
c5sharp = 554
d5 = 587
d5sharp = 622
e5 = 659
f5 = 698
f5sharp = 740
g5 = 784
g5sharp = 831
a5 = 880
a5sharp = 932
b5 = 988
c6 = 1046


#MAJOR KEYS
cmajor = [c5, d5, e5, f5, g5, a5, b5, c6]
dmajor = [d5, e5, f5sharp, g5, a5, b5, c5sharp]
emajor = [e5, f5sharp, g5sharp, a5, b5, c5sharp, d5sharp]
fmajor = [f5, g5, a5, a5sharp, c5, d5, e5]
gmajor = [g5, a5, b5, c5, d5, e5, f5sharp]
amajor = [a5, b5, c5sharp, d5, e5, f5sharp, g5sharp]
bmajor = [b5, c5sharp, d5sharp, e5, f5sharp, g5sharp, a5sharp]
csharpmajor = [c5sharp, d5sharp, f5, f5sharp, g5sharp, a5sharp, c5]
dsharpmajor = [d5sharp, f5, g5, g5sharp, a5sharp, c5, d5]
fsharpmajor = [f5sharp, g5sharp, a5sharp, b5, c5sharp, d5sharp, f5]
gsharpmajor = [g5sharp, a5sharp, c5, c5sharp, d5sharp, f5, g5]
asharpmajor = [a5sharp, c5, d5, d5sharp, f5, g5, a5]


#MINOR KEYS
cminor = [c5, d5, d5sharp, f5, g5, g5sharp, a5sharp, c6]
dminor = [d5, e5, f5, g5, a5, a5sharp, c5]
eminor = [e5, f5sharp, g5, a5, b5, c5, d5]
fminor = [f5, g5, g5sharp, a5sharp, c5, c5sharp, d5sharp]
gminor = [g5, a5, a5sharp, c5, d5, d5sharp, f5]
aminor = [a5, b5, c5, d5, e5, f5, g5]
bminor = [b5, c5sharp, d5, e5, f5sharp, g5, a5]
csharpminor = [c5sharp, d5sharp, e5, f5sharp, g5sharp, a5, b5]
dsharpminor = [d5sharp, f5, f5sharp, g5sharp, a5sharp, b5, c5sharp]
fsharpminor = [f5sharp, g5sharp, a5, b5, c5sharp, d5, e5]
gsharpminor = [g5sharp, a5sharp, b5, c5sharp, d5sharp, e5, f5sharp]
asharpminor = [a5sharp, c5, c5sharp, d5sharp, f5, f5sharp, g5sharp]


#NOTELENGTHS

notelengths = ['eighth', 'quarter', 'half', 'whole']




iterator = 10

while elapsed < songinmilli:
    note = random.choice(eval(key))
    notelength = random.choice(notelengths)
    
    if notelength == 'eighth':
        length = math.ceil(250 * (60/BPM))
    if notelength == 'quarter':
        length = math.ceil(500 * (60/BPM))
    if notelength == 'half':
        length = math.ceil(1000 * (60/BPM))
    if notelength == 'whole':
        length = math.ceil(2000 * (60/BPM))
        
    winsound.Beep(note, length)
    elapsed = elapsed + length
    