import random
import time
import wave
from playsound import playsound #pip install playsound


class Song:
    
    def __init__(self):
        self.songinmilli = 0
        self.key = 'self.'
        
        instrument_satisfy = False
        
        while instrument_satisfy == False:
            instrument_input = input("What instrument would you like to use? Enter 'piano' or 'sax'\n")
            if instrument_input.lower() in ['piano', 'sax']:
                instrument_satisfy = True
            else:
                print("Invalid instrument, enter 'piano' or 'sax'")
        
        self.instrument = instrument_input
        
        #MAJOR KEYS
        self.chromatic = [Song.c5, Song.c5sharp, Song.d5, Song.d5sharp, Song.e5, Song.f5, Song.f5sharp, Song.g5, Song.g5sharp, Song.a5, Song.a5sharp, Song.b5, Song.c6]
        self.cmajor = [Song.c5, Song.d5, Song.e5, Song.f5, Song.g5, Song.a5, Song.b5, Song.c6]
        self.dmajor = [Song.d5, Song.e5, Song.f5sharp, Song.g5, Song.a5, Song.b5, Song.c5sharp]
        self.emajor = [Song.e5, Song.f5sharp, Song.g5sharp, Song.a5, Song.b5, Song.c5sharp, Song.d5sharp]
        self.fmajor = [Song.f5, Song.g5, Song.a5, Song.a5sharp, Song.c5, Song.d5, Song.e5, Song.f5]
        self.gmajor = [Song.g5, Song.a5, Song.b5, Song.c5, Song.d5, Song.e5, Song.f5sharp]
        self.amajor = [Song.a5, Song.b5, Song.c5sharp, Song.d5, Song.e5, Song.f5sharp, Song.g5sharp]
        self.bmajor = [Song.b5, Song.c5sharp, Song.d5sharp, Song.e5, Song.f5sharp, Song.g5sharp, Song.a5sharp]
        self.csharpmajor = [Song.c5sharp, Song.d5sharp, Song.f5, Song.f5sharp, Song.g5sharp, Song.a5sharp, Song.c5]
        self.dsharpmajor = [Song.d5sharp, Song.f5, Song.g5, Song.g5sharp, Song.a5sharp, Song.c5, Song.d5]
        self.fsharpmajor = [Song.f5sharp, Song.g5sharp, Song.a5sharp, Song.b5, Song.c5sharp, Song.d5sharp, Song.f5]
        self.gsharpmajor = [Song.g5sharp, Song.a5sharp, Song.c5, Song.c5sharp, Song.d5sharp, Song.f5, Song.g5]
        self.asharpmajor = [Song.a5sharp, Song.c5, Song.d5, Song.d5sharp, Song.f5, Song.g5, Song.a5]    
        
        #MINOR KEYS
        self.cminor = [Song.c5, Song.d5, Song.d5sharp, Song.f5, Song.g5, Song.g5sharp, Song.a5sharp, Song.c6]
        self.dminor = [Song.d5, Song.e5, Song.f5, Song.g5, Song.a5, Song.a5sharp, Song.c5]
        self.eminor = [Song.e5, Song.f5sharp, Song.g5, Song.a5, Song.b5, Song.c5, Song.d5]
        self.fminor = [Song.f5, Song.g5, Song.g5sharp, Song.a5sharp, Song.c5, Song.c5sharp, Song.d5sharp]
        self.gminor = [Song.g5, Song.a5, Song.a5sharp, Song.c5, Song.d5, Song.d5sharp, Song.f5]
        self.aminor = [Song.a5, Song.b5, Song.c5, Song.d5, Song.e5, Song.f5, Song.g5]
        self.bminor = [Song.b5, Song.c5sharp, Song.d5, Song.e5, Song.f5sharp, Song.g5, Song.a5]
        self.csharpminor = [Song.c5sharp, Song.d5sharp, Song.e5, Song.f5sharp, Song.g5sharp, Song.a5, Song.b5]
        self.dsharpminor = [Song.d5sharp, Song.f5, Song.f5sharp, Song.g5sharp, Song.a5sharp, Song.b5, Song.c5sharp]
        self.fsharpminor = [Song.f5sharp, Song.g5sharp, Song.a5, Song.b5, Song.c5sharp, Song.d5, Song.e5]
        self.gsharpminor = [Song.g5sharp, Song.a5sharp, Song.b5, Song.c5sharp, Song.d5sharp, Song.e5, Song.f5sharp]
        self.asharpminor = [Song.a5sharp, Song.c5, Song.c5sharp, Song.d5sharp, Song.f5, Song.f5sharp, Song.g5sharp]
        
        
        #LIST TO BE TURNED INTO FILE
        self.wavfiles = []
        
        #SONG NAME
        
        self.songname = 'yoursong'
        
        
        #FILE NAME IF APPLICABLE
        self.filename = ''
        
        
        #FILE INPUT PARAMETERS IF APPLICABLE
        self.file_songinmilli = 0
        self.file_key = 'self.'
        self.file_songname = 'yoursong'

        
    def c5(self):
        if self.instrument.lower() == 'piano':
            playsound("pianolowc.wav", False)
            return "pianolowc.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxlowc.wav", False)
            return "saxlowc.wav"
    def c5sharp(self):
        if self.instrument.lower() == 'piano':
            playsound("pianoc#.wav", False)
            return "pianoc#.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxc#.wav", False)
            return "saxc#.wav"
    def d5(self):
        if self.instrument.lower() == 'piano':
            playsound("pianod.wav", False)
            return "pianod.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxd.wav", False)
            return "saxd.wav"
    def d5sharp(self):
        if self.instrument.lower() == 'piano':
            playsound("pianod#.wav", False)
            return "pianod#.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxd#.wav", False)
            return "saxd#.wav"
    def e5(self):
        if self.instrument.lower() == 'piano':
            playsound("pianoe.wav", False)
            return "pianoe.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxe.wav", False)
            return "saxe.wav"
    def f5(self):
        if self.instrument.lower() == 'piano':
            playsound("pianof.wav", False)
            return "pianof.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxf.wav", False)
            return "saxf.wav"
    def f5sharp(self):
        if self.instrument.lower() == 'piano':
            playsound("pianof#.wav", False)
            return "pianof#.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxf#.wav", False)
            return "saxf#.wav"
    def g5(self):
        if self.instrument.lower() == 'piano':
            playsound("pianog.wav", False)
            return "pianog.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxg.wav", False)
            return "saxg.wav"
    def g5sharp(self):
        if self.instrument.lower() == 'piano':
            playsound("pianog#.wav", False)
            return "pianog#.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxg#.wav", False)
            return "saxg#.wav"
    def a5(self):
        if self.instrument.lower() == 'piano':
            playsound("pianoa.wav", False)
            return "pianoa.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxa.wav", False)
            return "saxa.wav"
    def a5sharp(self):
        if self.instrument.lower() == 'piano':
            playsound("pianoa#.wav", False)
            return "pianoa#.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxa#.wav", False)
            return "saxa#.wav"
    def b5(self):
        if self.instrument.lower() == 'piano':
            playsound("pianob.wav", False)
            return "pianob.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxb.wav", False)
            return "saxb.wav"
    def c6(self):
        if self.instrument.lower() == 'piano':
            playsound("pianohighc.wav", False)
            return "pianohighc.wav"
        elif self.instrument.lower() == 'sax':
            playsound("saxhighc.wav", False)
            return "saxhighc.wav"
        
    
        


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
        
        
        keysatisfy = False
        while keysatisfy == False:
            inputkey = input("Enter a Key, i.e. 'asharpminor'\n")
            if inputkey.lower() in ['cmajor', 'dmajor', 'emajor', 'fmajor', 'gmajor', 'amajor', 'bmajor', 'csharpmajor', 'dsharpmajor', 'fsharpmajor', 'gsharpmajor', 'asharpmajor', 'cminor', 'dminor', 'eminor', 'fminor', 'gminor', 'aminor', 'bminor', 'csharpminor', 'dsharpminor', 'fsharpminor', 'gsharpminor', 'asharpminor']:
                keysatisfy = True
                self.key += inputkey
            else: 
                print("Invalid Key")
                
                
        self.songname = input("Give your song a name!\n")
        
        
    def play_song_inputs(self):
        elapsed = 0
        self.key = eval(self.key)
        while elapsed < self.songinmilli:
            choice = random.choice(self.key)(mysong)
            self.wavfiles.append(choice)
            time.sleep(2)
            elapsed += 2000
            
            
    def compile_song_inputs(self):
        infiles = self.wavfiles
        outfile = f"OutputSongs/{self.songname}.wav"
        
        wav_out = wave.open(outfile, 'wb')
        for wav_path in infiles:
            wav_in = wave.open(wav_path, 'rb')
            if not wav_out.getnframes():
                wav_out.setparams(wav_in.getparams())
            wav_out.writeframes(wav_in.readframes(wav_in.getnframes()))
            
            
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
        self.file_songname = strippedlines[2].split('-')[1]
        
    
    def play_song_file(self):
        elapsed = 0
        self.file_key = eval(self.file_key)
        while elapsed < self.file_songinmilli:
            choice = random.choice(self.file_key)(mysong)
            self.wavfiles.append(choice)
            time.sleep(2)
            elapsed += 2000
        
    
    
    def compile_song_file(self):
        infiles = self.wavfiles
        outfile = f"OutputSongs/{self.file_songname}.wav"
        
        wav_out = wave.open(outfile, 'wb')
        for wav_path in infiles:
            wav_in = wave.open(wav_path, 'rb')
            if not wav_out.getnframes():
                wav_out.setparams(wav_in.getparams())
            wav_out.writeframes(wav_in.readframes(wav_in.getnframes()))   

        
            

        

        
        
        
        
if __name__ == "__main__":
    
    mysong = Song()
    
    paramsatisfy = False
    while paramsatisfy == False:
        parammethod = input("How would you like to create your song? Input a file or answer a series of inputs? Enter 'file' or 'inputs'\n")
        if parammethod.lower() in ['file', 'inputs']:
            paramsatisfy = True
        else:
            print("Invalid Parameter Method. Enter 'file' or 'inputs'")
            
            
    if parammethod.lower() == 'inputs':
        

    
    



    
        mysong.define_song_inputs()

        mysong.play_song_inputs()
    
        answersatisfy = False
    
        while answersatisfy == False:
            answer = input("Would you like to download your song? Enter y or n.\n")
            if answer.lower() in ['y', 'n']:
                answersatisfy = True
            
        if answer.lower() == 'y':
            mysong.compile_song_inputs()
            
            
    elif parammethod.lower() == 'file':
        
        mysong.filename = input("Enter a txt file to be read.\n")
    
        mysong.define_song_file()

        mysong.play_song_file()
    
        answersatisfy = False
    
        while answersatisfy == False:
            answer = input("Would you like to download your song? Enter y or n.\n")
            if answer.lower() in ['y', 'n']:
                answersatisfy = True
            
        if answer.lower() == 'y':
            mysong.compile_song_file()
        
        
