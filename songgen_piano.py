import winsound
import random
import time
import wave


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

    def c5(self):
        winsound.PlaySound("pianolowc", winsound.SND_ASYNC)
        return "pianolowc.wav"
    def c5sharp(self):
        winsound.PlaySound("pianoc#", winsound.SND_ASYNC)
        return "pianoc#.wav"
    def d5(self):
        winsound.PlaySound("pianod", winsound.SND_ASYNC)
        return "pianod.wav"
    def d5sharp(self):
        winsound.PlaySound("pianod#", winsound.SND_ASYNC)
        return "pianod#.wav"
    def e5(self):
        winsound.PlaySound("pianoe", winsound.SND_ASYNC)
        return "pianoe.wav"
    def f5(self):
        winsound.PlaySound("pianof", winsound.SND_ASYNC)
        return "pianof.wav"
    def f5sharp(self):
        winsound.PlaySound("pianof#", winsound.SND_ASYNC)
        return "pianof#.wav"
    def g5(self):
        winsound.PlaySound("pianog", winsound.SND_ASYNC)
        return "pianog.wav"
    def g5sharp(self):
        winsound.PlaySound("pianog#", winsound.SND_ASYNC)
        return "pianog#.wav"
    def a5(self):
        winsound.PlaySound("pianoa", winsound.SND_ASYNC)
        return "pianoa.wav"
    def a5sharp(self):
        winsound.PlaySound("pianoa#", winsound.SND_ASYNC)
        return "pianoa#.wav"
    def b5(self):
        winsound.PlaySound("pianob", winsound.SND_ASYNC)
        return "pianob.wav"
    def c6(self):
        winsound.PlaySound("pianohighc", winsound.SND_ASYNC)
        return "pianohighc.wav"


    def define_song(self):
        
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
        
        
    def play_song(self):
        elapsed = 0
        self.key = eval(self.key)
        while elapsed < self.songinmilli:
            choice = random.choice(self.key)(mysong)
            self.wavfiles.append(choice)
            time.sleep(2)
            elapsed += 2000
            
            
    def compile_song(self):
        
        infiles = self.wavfiles
        outfile = f"compiledsongs/{self.songname}.wav"
        
        with wave.open(outfile, 'wb') as wav_out:
            for wav_path in infiles:
                with wave.open(wav_path, 'rb') as wav_in:
                    if not wav_out.getnframes():
                        wav_out.setparams(wav_in.getparams())                              #this line shows an error for some reason but it works anyway
                    wav_out.writeframes(wav_in.readframes(wav_in.getnframes()))            #this line too

        

        
        
        
        
if __name__ == "__main__":
    
    mysong = PianoSong()
    
    mysong.define_song()

    mysong.play_song()
    
    answersatisfy = False
    
    while answersatisfy == False:
        answer = input("Would you like to download your song?\n")
        if answer.lower() in ['y', 'n']:
            answersatisfy = True
            
    if answer.lower() == 'y':
        mysong.compile_song()
