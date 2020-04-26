import winsound
import random
import math

class SineWaveSong:
    
    def __init__(self):
        
        #SONG PARAMETERS
        self.songinmilli = 0
        self.key = 'self.'
        self.BPM = 0
        
        #SONG PARAMETERS FOR FILE (IF APPLICABLE)
        
        self.file_songinmilli = 0
        self.file_key = 'self.'
        self.file_BPM = 0
        
        #FILE NAME IF APPLICABLE
        self.filename = ''
        
        #NOTES
        self.c5 = 523
        self.c5sharp = 554
        self.d5 = 587
        self.d5sharp = 622
        self.e5 = 659
        self.f5 = 698
        self.f5sharp = 740
        self.g5 = 784
        self.g5sharp = 831
        self.a5 = 880
        self.a5sharp = 932
        self.b5 = 988
        self.c6 = 1046


        #MAJOR KEYS
        self.cmajor = [self.c5, self.d5, self.e5, self.f5, self.g5, self.a5, self.b5, self.c6]
        self.dmajor = [self.d5, self.e5, self.f5sharp, self.g5, self.a5, self.b5, self.c5sharp]
        self.emajor = [self.e5, self.f5sharp, self.g5sharp, self.a5, self.b5, self.c5sharp, self.d5sharp]
        self.fmajor = [self.f5, self.g5, self.a5, self.a5sharp, self.c5, self.d5, self.e5]
        self.gmajor = [self.g5, self.a5, self.b5, self.c5, self.d5, self.e5, self.f5sharp]
        self.amajor = [self.a5, self.b5, self.c5sharp, self.d5, self.e5, self.f5sharp, self.g5sharp]
        self.bmajor = [self.b5, self.c5sharp, self.d5sharp, self.e5, self.f5sharp, self.g5sharp, self.a5sharp]
        self.csharpmajor = [self.c5sharp, self.d5sharp, self.f5, self.f5sharp, self.g5sharp, self.a5sharp, self.c5]
        self.dsharpmajor = [self.d5sharp, self.f5, self.g5, self.g5sharp, self.a5sharp, self.c5, self.d5]
        self.fsharpmajor = [self.f5sharp, self.g5sharp, self.a5sharp, self.b5, self.c5sharp, self.d5sharp, self.f5]
        self.gsharpmajor = [self.g5sharp, self.a5sharp, self.c5, self.c5sharp, self.d5sharp, self.f5, self.g5]
        self.asharpmajor = [self.a5sharp, self.c5, self.d5, self.d5sharp, self.f5, self.g5, self.a5]


        #MINOR KEYS
        self.cminor = [self.c5, self.d5, self.d5sharp, self.f5, self.g5, self.g5sharp, self.a5sharp, self.c6]
        self.dminor = [self.d5, self.e5, self.f5, self.g5, self.a5, self.a5sharp, self.c5]
        self.eminor = [self.e5, self.f5sharp, self.g5, self.a5, self.b5, self.c5, self.d5]
        self.fminor = [self.f5, self.g5, self.g5sharp, self.a5sharp, self.c5, self.c5sharp, self.d5sharp]
        self.gminor = [self.g5, self.a5, self.a5sharp, self.c5, self.d5, self.d5sharp, self.f5]
        self.aminor = [self.a5, self.b5, self.c5, self.d5, self.e5, self.f5, self.g5]
        self.bminor = [self.b5, self.c5sharp, self.d5, self.e5, self.f5sharp, self.g5, self.a5]
        self.csharpminor = [self.c5sharp, self.d5sharp, self.e5, self.f5sharp, self.g5sharp, self.a5, self.b5]
        self.dsharpminor = [self.d5sharp, self.f5, self.f5sharp, self.g5sharp, self.a5sharp, self.b5, self.c5sharp]
        self.fsharpminor = [self.f5sharp, self.g5sharp, self.a5, self.b5, self.c5sharp, self.d5, self.e5]
        self.gsharpminor = [self.g5sharp, self.a5sharp, self.b5, self.c5sharp, self.d5sharp, self.e5, self.f5sharp]
        self.asharpminor = [self.a5sharp, self.c5, self.c5sharp, self.d5sharp, self.f5, self.f5sharp, self.g5sharp]


        #NOTELENGTHS
        self.notelengths = ['eighth', 'quarter', 'half', 'whole']





    def define_song_inputs(self):

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

        self.songinmilli = songlength * 1000

        BPMsatisfy = False
        while BPMsatisfy == False:
            try:
                self.BPM = int(input("Enter a BPM for your song between 60 and 120 (Beats Per Minute)\n"))
                if self.BPM >= 60 and self.BPM <= 120:
                    BPMsatisfy = True
                else:
                    raise Exception
            except:
                print("Invalid BPM")

        keysatisfy = False
        while keysatisfy == False:
            inputkey = input("Enter a Key, i.e. 'asharpminor'\n")
            if inputkey.lower() in ['cmajor', 'dmajor', 'emajor', 'fmajor', 'gmajor', 'amajor', 'bmajor', 'csharpmajor', 'dsharpmajor', 'fsharpmajor', 'gsharpmajor', 'asharpmajor', 'cminor', 'dminor', 'eminor', 'fminor', 'gminor', 'aminor', 'bminor', 'csharpminor', 'dsharpminor', 'fsharpminor', 'gsharpminor', 'asharpminor']:
                keysatisfy = True
                self.key += inputkey
            else: 
                print("Invalid Key")


    def play_song_inputs(self):
        elapsed = 0

        while elapsed < self.songinmilli:
            note = random.choice(eval(self.key))
            notelength = random.choice(self.notelengths)
            
            if notelength == 'eighth':
                length = math.ceil(250 * (60/self.BPM))
            if notelength == 'quarter':
                length = math.ceil(500 * (60/self.BPM))
            if notelength == 'half':
                length = math.ceil(1000 * (60/self.BPM))
            if notelength == 'whole':
                length = math.ceil(2000 * (60/self.BPM))
                
            winsound.Beep(note, length)
            elapsed = elapsed + length
            
    
    def define_song_file(self):
        strippedlines = []
        fh = open(self.filename)
        lines = fh.readlines()
        for line in lines:
            strippedline = line.strip()
            strippedlines.append(strippedline)
        fh.close()
        
        self.file_songinmilli = int(strippedlines[0].split('-')[1]) * 1000
        self.file_key += strippedlines[1].split('-')[1]
        self.file_BPM = strippedlines[2].split('-')[1]
        
        
    def play_song_file(self):
        
        elapsed = 0

        while elapsed < self.file_songinmilli:
            note = random.choice(eval(self.file_key))
            notelength = random.choice(self.notelengths)
            
            if notelength == 'eighth':
                length = math.ceil(250 * (60/int(self.file_BPM)))
            if notelength == 'quarter':
                length = math.ceil(500 * (60/int(self.file_BPM)))
            if notelength == 'half':
                length = math.ceil(1000 * (60/int(self.file_BPM)))
            if notelength == 'whole':
                length = math.ceil(2000 * (60/int(self.file_BPM)))
                
            winsound.Beep(note, length)
            elapsed = elapsed + length
            
            
            
if __name__ == "__main__":
    
    paramsatisfy = False
    while paramsatisfy == False:
        parammethod = input("How would you like to create your song? Input a file or answer a series of inputs? Enter 'file' or 'inputs'\n")
        if parammethod.lower() in ['file', 'inputs']:
            paramsatisfy = True
        else:
            print("Invalid Parameter Method. Enter 'file' or 'inputs'")
            
    if parammethod.lower() == 'inputs':
        mySineWaveSong = SineWaveSong()
    
        mySineWaveSong.define_song_inputs()
    
        mySineWaveSong.play_song_inputs()
        
    
    
    
    elif parammethod.lower() == 'file':
        
        mySineWaveSong = SineWaveSong()
        
        mySineWaveSong.filename = input("Enter a txt file to be read.\n")

            
        
        mySineWaveSong.define_song_file()
        
        mySineWaveSong.play_song_file()
    