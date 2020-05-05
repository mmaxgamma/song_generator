import random
import time
import wave
from playsound import playsound #pip install playsound


class PianoSong:
    
    def __init__(self):
        self.songinmilli = 0
        self.key = 'self.'
        
        #MAJOR KEYS
        self.chromatic = [PianoSong.c5, PianoSong.c5sharp, PianoSong.d5, PianoSong.d5sharp, PianoSong.e5, PianoSong.f5, PianoSong.f5sharp, PianoSong.g5, PianoSong.g5sharp, PianoSong.a5, PianoSong.a5sharp, PianoSong.b5, PianoSong.c6]
        self.cmajor = [PianoSong.c5, PianoSong.d5, PianoSong.e5, PianoSong.f5, PianoSong.g5, PianoSong.a5, PianoSong.b5, PianoSong.c6]
        self.dmajor = [PianoSong.d5, PianoSong.e5, PianoSong.f5sharp, PianoSong.g5, PianoSong.a5, PianoSong.b5, PianoSong.c5sharp]
        self.emajor = [PianoSong.e5, PianoSong.f5sharp, PianoSong.g5sharp, PianoSong.a5, PianoSong.b5, PianoSong.c5sharp, PianoSong.d5sharp]
        self.fmajor = [PianoSong.f5, PianoSong.g5, PianoSong.a5, PianoSong.a5sharp, PianoSong.c5, PianoSong.d5, PianoSong.e5, PianoSong.f5]
        self.gmajor = [PianoSong.g5, PianoSong.a5, PianoSong.b5, PianoSong.c5, PianoSong.d5, PianoSong.e5, PianoSong.f5sharp]
        self.amajor = [PianoSong.a5, PianoSong.b5, PianoSong.c5sharp, PianoSong.d5, PianoSong.e5, PianoSong.f5sharp, PianoSong.g5sharp]
        self.bmajor = [PianoSong.b5, PianoSong.c5sharp, PianoSong.d5sharp, PianoSong.e5, PianoSong.f5sharp, PianoSong.g5sharp, PianoSong.a5sharp]
        self.csharpmajor = [PianoSong.c5sharp, PianoSong.d5sharp, PianoSong.f5, PianoSong.f5sharp, PianoSong.g5sharp, PianoSong.a5sharp, PianoSong.c5]
        self.dsharpmajor = [PianoSong.d5sharp, PianoSong.f5, PianoSong.g5, PianoSong.g5sharp, PianoSong.a5sharp, PianoSong.c5, PianoSong.d5]
        self.fsharpmajor = [PianoSong.f5sharp, PianoSong.g5sharp, PianoSong.a5sharp, PianoSong.b5, PianoSong.c5sharp, PianoSong.d5sharp, PianoSong.f5]
        self.gsharpmajor = [PianoSong.g5sharp, PianoSong.a5sharp, PianoSong.c5, PianoSong.c5sharp, PianoSong.d5sharp, PianoSong.f5, PianoSong.g5]
        self.asharpmajor = [PianoSong.a5sharp, PianoSong.c5, PianoSong.d5, PianoSong.d5sharp, PianoSong.f5, PianoSong.g5, PianoSong.a5]    
        
        #MINOR KEYS
        self.cminor = [PianoSong.c5, PianoSong.d5, PianoSong.d5sharp, PianoSong.f5, PianoSong.g5, PianoSong.g5sharp, PianoSong.a5sharp, PianoSong.c6]
        self.dminor = [PianoSong.d5, PianoSong.e5, PianoSong.f5, PianoSong.g5, PianoSong.a5, PianoSong.a5sharp, PianoSong.c5]
        self.eminor = [PianoSong.e5, PianoSong.f5sharp, PianoSong.g5, PianoSong.a5, PianoSong.b5, PianoSong.c5, PianoSong.d5]
        self.fminor = [PianoSong.f5, PianoSong.g5, PianoSong.g5sharp, PianoSong.a5sharp, PianoSong.c5, PianoSong.c5sharp, PianoSong.d5sharp]
        self.gminor = [PianoSong.g5, PianoSong.a5, PianoSong.a5sharp, PianoSong.c5, PianoSong.d5, PianoSong.d5sharp, PianoSong.f5]
        self.aminor = [PianoSong.a5, PianoSong.b5, PianoSong.c5, PianoSong.d5, PianoSong.e5, PianoSong.f5, PianoSong.g5]
        self.bminor = [PianoSong.b5, PianoSong.c5sharp, PianoSong.d5, PianoSong.e5, PianoSong.f5sharp, PianoSong.g5, PianoSong.a5]
        self.csharpminor = [PianoSong.c5sharp, PianoSong.d5sharp, PianoSong.e5, PianoSong.f5sharp, PianoSong.g5sharp, PianoSong.a5, PianoSong.b5]
        self.dsharpminor = [PianoSong.d5sharp, PianoSong.f5, PianoSong.f5sharp, PianoSong.g5sharp, PianoSong.a5sharp, PianoSong.b5, PianoSong.c5sharp]
        self.fsharpminor = [PianoSong.f5sharp, PianoSong.g5sharp, PianoSong.a5, PianoSong.b5, PianoSong.c5sharp, PianoSong.d5, PianoSong.e5]
        self.gsharpminor = [PianoSong.g5sharp, PianoSong.a5sharp, PianoSong.b5, PianoSong.c5sharp, PianoSong.d5sharp, PianoSong.e5, PianoSong.f5sharp]
        self.asharpminor = [PianoSong.a5sharp, PianoSong.c5, PianoSong.c5sharp, PianoSong.d5sharp, PianoSong.f5, PianoSong.f5sharp, PianoSong.g5sharp]
        
        
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
        playsound("pianolowc.wav", False)
        return "pianolowc.wav"
    def c5sharp(self):
        playsound("pianoc#.wav", False)
        return "pianoc#.wav"
    def d5(self):
        playsound("pianod.wav", False)
        return "pianod.wav"
    def d5sharp(self):
        playsound("pianod#.wav", False)
        return "pianod#.wav"
    def e5(self):
        playsound("pianoe.wav", False)
        return "pianoe.wav"
    def f5(self):
        playsound("pianof.wav", False)
        return "pianof.wav"
    def f5sharp(self):
        playsound("pianof#.wav", False)
        return "pianof#.wav"
    def g5(self):
        playsound("pianog.wav", False)
        return "pianog.wav"
    def g5sharp(self):
        playsound("pianog#.wav", False)
        return "pianog#.wav"
    def a5(self):
        playsound("pianoa.wav", False)
        return "pianoa.wav"
    def a5sharp(self):
        playsound("pianoa#.wav", False)
        return "pianoa#.wav"
    def b5(self):
        playsound("pianob.wav", False)
        return "pianob.wav"
    def c6(self):
        playsound("pianohighc.wav", False)
        return "pianohighc.wav"


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
    
    paramsatisfy = False
    while paramsatisfy == False:
        parammethod = input("How would you like to create your song? Input a file or answer a series of inputs? Enter 'file' or 'inputs'\n")
        if parammethod.lower() in ['file', 'inputs']:
            paramsatisfy = True
        else:
            print("Invalid Parameter Method. Enter 'file' or 'inputs'")
            
            
    if parammethod.lower() == 'inputs':
        

    
    
        mysong = PianoSong()


    
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
        
        mysong = PianoSong()
        
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
        
        
