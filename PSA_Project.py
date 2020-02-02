import wave
import numpy as np
import simpleaudio as sa
from tkinter import *
from tkinter.ttk import *
import array
import random
        
class chord_type_switch(object):
    def switch(self, chord_type, key, scale, i, chord_duration):
        func_name="generate_chord_type_" + str(chord_type)
        func = getattr(self, func_name)
        return func(key, scale, i, chord_duration)

    layer1=np.zeros(shape=[64,2])
    layer2=np.zeros(shape=[64,2])
    layer3=np.zeros(shape=[64,2])
    layer4=np.zeros(shape=[64,2])
    layer5=np.zeros(shape=[64,2])
    audio=np.zeros(shape=[441000,2])

    def switch_duration_id_shift(self, chord_duration):
        switch_shift = {
            1: 0,
            2: 1,
            3: 2,
            4: 3,
            6: 4,
            8: 5,
            12: 6,
            16: 7
        }
        return switch_shift.get(chord_duration)
    def switch_density_to_duration(self, density):
        switch_duration = {
            0: [16],
            1: [8,16],
            2: [4,8,12,16],
            3: [4,8],
            4: [2,4,6,8],
            5: [2,4],
            6: [1,2,3,4],
            7: [1,2]
        }
        return switch_duration.get(density)

    def generate_chord_type_0(self, key, scale, time, chord_duration):
        base_note=random.randrange(0,5,1)
        self.layer1[time][0]=int(c4_id-scales[scale][base_note]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer1[time][1]=int(chord_duration)
        self.layer2[time][0]=int(c4_id-scales[scale][base_note+2]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer2[time][1]=int(chord_duration)
        self.layer3[time][0]=int(c4_id-scales[scale][base_note+4]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer3[time][1]=int(chord_duration)

    def generate_chord_type_1(self, key, scale, time, chord_duration):
        base_note = chord_sus2[random.randrange(0,4,1)]
        self.layer1[time][0]=int(c4_id-scales[scale][base_note]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer1[time][1]=int(chord_duration)
        self.layer2[time][0]=int(c4_id-scales[scale][base_note+1]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer2[time][1]=int(chord_duration)
        self.layer3[time][0]=int(c4_id-scales[scale][base_note+4]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer3[time][1]=int(chord_duration)

    def generate_chord_type_2(self, key, scale, time, chord_duration):
        base_note = chord_sus2[random.randrange(0,4,1)]
        self.layer1[time][0]=int(c4_id-scales[scale][base_note]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer1[time][1]=int(chord_duration)
        self.layer2[time][0]=int(c4_id-scales[scale][base_note+3]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer2[time][1]=int(chord_duration)
        self.layer3[time][0]=int(c4_id-scales[scale][base_note+4]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer3[time][1]=int(chord_duration)

    def generate_chord_type_3(self, key, scale, time, chord_duration):
        base_note=random.randrange(0,5,1)
        self.layer1[time][0]=int(c4_id-scales[scale][base_note]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer1[time][1]=int(chord_duration)
        self.layer2[time][0]=int(c4_id-scales[scale][base_note+2]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer2[time][1]=int(chord_duration)
        self.layer3[time][0]=int(c4_id-scales[scale][base_note+4]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer3[time][1]=int(chord_duration)
        self.layer4[time][0]=int(c4_id-scales[scale][base_note+7]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer4[time][1]=int(chord_duration)

    def generate_chord_type_4(self, key, scale, time, chord_duration):
        base_note=random.randrange(0,5,1)
        self.layer1[time][0]=int(c4_id-scales[scale][base_note]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer1[time][1]=int(chord_duration)
        self.layer2[time][0]=int(c4_id-scales[scale][base_note+2]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer2[time][1]=int(chord_duration)
        self.layer3[time][0]=int(c4_id-scales[scale][base_note+4]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer3[time][1]=int(chord_duration)
        self.layer4[time][0]=int(c4_id-scales[scale][base_note+1]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer4[time][1]=int(chord_duration)

    def generate_chord_type_5(self, key, scale, time, chord_duration):
        base_note=random.randrange(0,5,1)
        self.layer1[time][0]=int(c4_id-scales[scale][base_note]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer1[time][1]=int(chord_duration)
        self.layer2[time][0]=int(c4_id-scales[scale][base_note+2]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer2[time][1]=int(chord_duration)
        self.layer3[time][0]=int(c4_id-scales[scale][base_note+4]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer3[time][1]=int(chord_duration)
        self.layer4[time][0]=int(c4_id-scales[scale][base_note+3]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer4[time][1]=int(chord_duration)

    def generate_chord_type_6(self, key, scale, time, chord_duration):
        self.layer1[time][0]=int(c4_id-scales[scale][6]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer1[time][1]=int(chord_duration)
        self.layer2[time][0]=int(c4_id-scales[scale][1]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer2[time][1]=int(chord_duration)
        self.layer3[time][0]=int(c4_id-scales[scale][3]*8-key*8+self.switch_duration_id_shift(chord_duration))
        self.layer3[time][1]=int(chord_duration)

    def wav_to_table(self):
        self.audio=self.audio.astype(np.int16)
        t=0
        pos=int(0)
        while pos<64:
            t=int(pos/8.6*44100)
            t3=1
            if self.layer1[pos][0]>0:
                if self.layer4[pos][0]>0:
                    if self.layer5[pos][0]>0:
                        wav=wave.open(filenames[int(self.layer1[pos][0])])
                        wav.setpos(0)
                        t2=t+wav.getnframes()
                        wav2=wave.open(filenames[int(self.layer2[pos][0])])
                        wav2.setpos(0)
                        wav3=wave.open(filenames[int(self.layer3[pos][0])])
                        wav3.setpos(0)
                        wav4=wave.open(filenames[int(self.layer4[pos][0])])
                        wav4.setpos(0)
                        wav5=wave.open(filenames[int(self.layer5[pos][0])])
                        wav5.setpos(0)
                        temp=wav.readframes(wav.getnframes())
                        temp_wav=np.fromstring(temp, dtype=np.int16)
                        temp2=wav2.readframes(wav2.getnframes())
                        temp_wav2=np.fromstring(temp2, dtype=np.int16)
                        temp3=wav3.readframes(wav3.getnframes())
                        temp_wav3=np.fromstring(temp3, dtype=np.int16)
                        temp4=wav4.readframes(wav4.getnframes())
                        temp_wav4=np.fromstring(temp4, dtype=np.int16)
                        temp5=wav5.readframes(wav5.getnframes())
                        temp_wav5=np.fromstring(temp5, dtype=np.int16)
                        print(wav.getnframes())
                        print(temp_wav3.size)
                        print(t2)
                        while t<t2:
                            self.audio[t][0]+=temp_wav[t3-1]+temp_wav2[t3-1]+temp_wav3[t3-1]+temp_wav4[t3-1]+temp_wav5[t3-1]
                            self.audio[t][1]+=temp_wav[t3]+temp_wav2[t3]+temp_wav3[t3]+temp_wav4[t3]+temp_wav5[t3]
                            t+=1
                            t3+=2
                        #audio[t:t2][0]+=temp_wav+temp_wav2+temp_wav3+temp_wav4+temp_wav5
                        #audio[t:t2][1]+=temp_wav+temp_wav2+temp_wav3+temp_wav4+temp_wav5
                        pos=pos+int(self.layer1[pos][1])
                    else:
                        wav=wave.open(filenames[int(self.layer1[pos][0])])
                        wav.setpos(0)
                        t2=t+wav.getnframes()
                        wav2=wave.open(filenames[int(self.layer2[pos][0])])
                        wav2.setpos(0)
                        wav3=wave.open(filenames[int(self.layer3[pos][0])])
                        wav3.setpos(0)
                        wav4=wave.open(filenames[int(self.layer4[pos][0])])
                        wav4.setpos(0)
                        temp=wav.readframes(wav.getnframes())
                        temp_wav=np.fromstring(temp, dtype=np.int16)
                        temp2=wav2.readframes(wav2.getnframes())
                        temp_wav2=np.fromstring(temp2, dtype=np.int16)
                        temp3=wav3.readframes(wav3.getnframes())
                        temp_wav3=np.fromstring(temp3, dtype=np.int16)
                        temp4=wav4.readframes(wav4.getnframes())
                        temp_wav4=np.fromstring(temp4, dtype=np.int16)
                        print(wav.getnframes())
                        print(temp_wav3.size)
                        print(t2)
                        while t<t2:
                            self.audio[t][0]+=temp_wav[t3-1]+temp_wav2[t3-1]+temp_wav3[t3-1]+temp_wav4[t3-1]
                            self.audio[t][1]+=temp_wav[t3]+temp_wav2[t3]+temp_wav3[t3]+temp_wav4[t3]
                            t+=1
                            t3+=2
                        #audio[t:t2][0]+=temp_wav+temp_wav2+temp_wav3+temp_wav4
                        #audio[t:t2][1]+=temp_wav+temp_wav2+temp_wav3+temp_wav4
                        pos=pos+int(self.layer1[pos][1])
                else:

                    wav=wave.open(filenames[int(self.layer1[pos][0])])
                    wav.setpos(0)
                    t2=t+wav.getnframes()
                    wav2=wave.open(filenames[int(self.layer2[pos][0])])
                    wav2.setpos(0)
                    wav3=wave.open(filenames[int(self.layer3[pos][0])])
                    wav3.setpos(0)
                    temp=wav.readframes(wav.getnframes())
                    temp_wav=np.fromstring(temp, dtype=np.int16)
                    temp2=wav2.readframes(wav2.getnframes())
                    temp_wav2=np.fromstring(temp2, dtype=np.int16)
                    temp3=wav3.readframes(wav3.getnframes())
                    temp_wav3=np.fromstring(temp3, dtype=np.int16)
                    print(wav.getnframes())
                    print(temp_wav3.size)
                    print(t2)
                    while t<t2:
                        self.audio[t][0]+=temp_wav[t3-1]+temp_wav2[t3-1]+temp_wav3[t3-1]
                        self.audio[t][1]+=temp_wav[t3]+temp_wav2[t3]+temp_wav3[t3]
                        t+=1
                        t3+=2
              #      audio[t:t2][0]+=temp_wav[0::2]+temp_wav2[0::2]+temp_wav3[0::2]
              #      audio[t:t2][1]+=temp_wav[1::2]+temp_wav2[1::2]+temp_wav3[1::2]
                    pos=pos+int(self.layer1[pos][1])
            else:
                pos+=1
        self.audio*=int(32767/np.max(np.abs(self.audio)))

    def play_audio(self):
        playback=sa.play_buffer(self.audio, 2, 2, 44100)

chord_type_switcher=chord_type_switch()

def generate_progression():
    scale = scale_combobox.current()
    key = key_combobox.current()
    complexity = complexity_combobox.current()
    density = density_combobox.current()
    timeline=0
    while timeline<64:
        if complexity!=0:
            chord_type = random.randrange(0,complexity-1,1)
        else:
            chord_type=0
        chord_duration = random.choice(chord_type_switcher.switch_density_to_duration(density))
        chord_type_switcher.switch(chord_type, key, scale, timeline, chord_duration)
        timeline+=chord_duration
        if timeline-64>0:
            chord_duration = chord_duration+64-timeline
    chord_type_switcher.wav_to_table()
    print("Finished.")

filenames = [ "resources\\pause.wav", "resources\\B7_1.wav", "resources\\B7_2.wav", "resources\\B7_3.wav", "resources\\B7_4.wav", "resources\\B7_6.wav", "resources\\B7_8.wav", "resources\\B7_12.wav", "resources\\B7_16.wav", "resources\\A#7_1.wav", "resources\\A#7_2.wav", "resources\\A#7_3.wav", "resources\\A#7_4.wav", "resources\\A#7_6.wav", "resources\\A#7_8.wav", "resources\\A#7_12.wav", "resources\\A#7_16.wav", "resources\\A7_1.wav", "resources\\A7_2.wav", "resources\\A7_3.wav", "resources\\A7_4.wav", "resources\\A7_6.wav", "resources\\A7_8.wav", "resources\\A7_12.wav", "resources\\A7_16.wav", "resources\\G#7_1.wav", "resources\\G#7_2.wav", "resources\\G#7_3.wav", "resources\\G#7_4.wav", "resources\\G#7_6.wav", "resources\\G#7_8.wav", "resources\\G#7_12.wav", "resources\\G#7_16.wav", "resources\\G7_1.wav", "resources\\G7_2.wav", "resources\\G7_3.wav", "resources\\G7_4.wav", "resources\\G7_6.wav", "resources\\G7_8.wav", "resources\\G7_12.wav", "resources\\G7_16.wav", "resources\\F#7_1.wav", "resources\\F#7_2.wav", "resources\\F#7_3.wav", "resources\\F#7_4.wav", "resources\\F#7_6.wav", "resources\\F#7_8.wav", "resources\\F#7_12.wav", "resources\\F#7_16.wav", "resources\\F7_1.wav", "resources\\F7_2.wav", "resources\\F7_3.wav", "resources\\F7_4.wav", "resources\\F7_6.wav", "resources\\F7_8.wav", "resources\\F7_12.wav", "resources\\F7_16.wav", "resources\\E7_1.wav", "resources\\E7_2.wav", "resources\\E7_3.wav", "resources\\E7_4.wav", "resources\\E7_6.wav", "resources\\E7_8.wav", "resources\\E7_12.wav", "resources\\E7_16.wav", "resources\\D#7_1.wav", "resources\\D#7_2.wav", "resources\\D#7_3.wav", "resources\\D#7_4.wav", "resources\\D#7_6.wav", "resources\\D#7_8.wav", "resources\\D#7_12.wav", "resources\\D#7_16.wav", "resources\\D7_1.wav", "resources\\D7_2.wav", "resources\\D7_3.wav", "resources\\D7_4.wav", "resources\\D7_6.wav", "resources\\D7_8.wav", "resources\\D7_12.wav", "resources\\D7_16.wav", "resources\\C#7_1.wav", "resources\\C#7_2.wav", "resources\\C#7_3.wav", "resources\\C#7_4.wav", "resources\\C#7_6.wav", "resources\\C#7_8.wav", "resources\\C#7_12.wav", "resources\\C#7_16.wav", "resources\\C7_1.wav", "resources\\C7_2.wav", "resources\\C7_3.wav", "resources\\C7_4.wav", "resources\\C7_6.wav", "resources\\C7_8.wav", "resources\\C7_12.wav", "resources\\C7_16.wav", "resources\\B6_1.wav", "resources\\B6_2.wav", "resources\\B6_3.wav", "resources\\B6_4.wav", "resources\\B6_6.wav", "resources\\B6_8.wav", "resources\\B6_12.wav", "resources\\B6_16.wav", "resources\\A#6_1.wav", "resources\\A#6_2.wav", "resources\\A#6_3.wav", "resources\\A#6_4.wav", "resources\\A#6_6.wav", "resources\\A#6_8.wav", "resources\\A#6_12.wav", "resources\\A#6_16.wav", "resources\\A6_1.wav", "resources\\A6_2.wav", "resources\\A6_3.wav", "resources\\A6_4.wav", "resources\\A6_6.wav", "resources\\A6_8.wav", "resources\\A6_12.wav", "resources\\A6_16.wav", "resources\\G#6_1.wav", "resources\\G#6_2.wav", "resources\\G#6_3.wav", "resources\\G#6_4.wav", "resources\\G#6_6.wav", "resources\\G#6_8.wav", "resources\\G#6_12.wav", "resources\\G#6_16.wav", "resources\\G6_1.wav", "resources\\G6_2.wav", "resources\\G6_3.wav", "resources\\G6_4.wav", "resources\\G6_6.wav", "resources\\G6_8.wav", "resources\\G6_12.wav", "resources\\G6_16.wav", "resources\\F#6_1.wav", "resources\\F#6_2.wav", "resources\\F#6_3.wav", "resources\\F#6_4.wav", "resources\\F#6_6.wav", "resources\\F#6_8.wav", "resources\\F#6_12.wav", "resources\\F#6_16.wav", "resources\\F6_1.wav", "resources\\F6_2.wav", "resources\\F6_3.wav", "resources\\F6_4.wav", "resources\\F6_6.wav", "resources\\F6_8.wav", "resources\\F6_12.wav", "resources\\F6_16.wav", "resources\\E6_1.wav", "resources\\E6_2.wav", "resources\\E6_3.wav", "resources\\E6_4.wav", "resources\\E6_6.wav", "resources\\E6_8.wav", "resources\\E6_12.wav", "resources\\E6_16.wav", "resources\\D#6_1.wav", "resources\\D#6_2.wav", "resources\\D#6_3.wav", "resources\\D#6_4.wav", "resources\\D#6_6.wav", "resources\\D#6_8.wav", "resources\\D#6_12.wav", "resources\\D#6_16.wav", "resources\\D6_1.wav", "resources\\D6_2.wav", "resources\\D6_3.wav", "resources\\D6_4.wav", "resources\\D6_6.wav", "resources\\D6_8.wav", "resources\\D6_12.wav", "resources\\D6_16.wav", "resources\\C#6_1.wav", "resources\\C#6_2.wav", "resources\\C#6_3.wav", "resources\\C#6_4.wav", "resources\\C#6_6.wav", "resources\\C#6_8.wav", "resources\\C#6_12.wav", "resources\\C#6_16.wav", "resources\\C6_1.wav", "resources\\C6_2.wav", "resources\\C6_3.wav", "resources\\C6_4.wav", "resources\\C6_6.wav", "resources\\C6_8.wav", "resources\\C6_12.wav", "resources\\C6_16.wav", "resources\\B5_1.wav", "resources\\B5_2.wav", "resources\\B5_3.wav", "resources\\B5_4.wav", "resources\\B5_6.wav", "resources\\B5_8.wav", "resources\\B5_12.wav", "resources\\B5_16.wav", "resources\\A#5_1.wav", "resources\\A#5_2.wav", "resources\\A#5_3.wav", "resources\\A#5_4.wav", "resources\\A#5_6.wav", "resources\\A#5_8.wav", "resources\\A#5_12.wav", "resources\\A#5_16.wav", "resources\\A5_1.wav", "resources\\A5_2.wav", "resources\\A5_3.wav", "resources\\A5_4.wav", "resources\\A5_6.wav", "resources\\A5_8.wav", "resources\\A5_12.wav", "resources\\A5_16.wav", "resources\\G#5_1.wav", "resources\\G#5_2.wav", "resources\\G#5_3.wav", "resources\\G#5_4.wav", "resources\\G#5_6.wav", "resources\\G#5_8.wav", "resources\\G#5_12.wav", "resources\\G#5_16.wav", "resources\\G5_1.wav", "resources\\G5_2.wav", "resources\\G5_3.wav", "resources\\G5_4.wav", "resources\\G5_6.wav", "resources\\G5_8.wav", "resources\\G5_12.wav", "resources\\G5_16.wav", "resources\\F#5_1.wav", "resources\\F#5_2.wav", "resources\\F#5_3.wav", "resources\\F#5_4.wav", "resources\\F#5_6.wav", "resources\\F#5_8.wav", "resources\\F#5_12.wav", "resources\\F#5_16.wav", "resources\\F5_1.wav", "resources\\F5_2.wav", "resources\\F5_3.wav", "resources\\F5_4.wav", "resources\\F5_6.wav", "resources\\F5_8.wav", "resources\\F5_12.wav", "resources\\F5_16.wav", "resources\\E5_1.wav", "resources\\E5_2.wav", "resources\\E5_3.wav", "resources\\E5_4.wav", "resources\\E5_6.wav", "resources\\E5_8.wav", "resources\\E5_12.wav", "resources\\E5_16.wav", "resources\\D#5_1.wav", "resources\\D#5_2.wav", "resources\\D#5_3.wav", "resources\\D#5_4.wav", "resources\\D#5_6.wav", "resources\\D#5_8.wav", "resources\\D#5_12.wav", "resources\\D#5_16.wav", "resources\\D5_1.wav", "resources\\D5_2.wav", "resources\\D5_3.wav", "resources\\D5_4.wav", "resources\\D5_6.wav", "resources\\D5_8.wav", "resources\\D5_12.wav", "resources\\D5_16.wav", "resources\\C#5_1.wav", "resources\\C#5_2.wav", "resources\\C#5_3.wav", "resources\\C#5_4.wav", "resources\\C#5_6.wav", "resources\\C#5_8.wav", "resources\\C#5_12.wav", "resources\\C#5_16.wav", "resources\\C5_1.wav", "resources\\C5_2.wav", "resources\\C5_3.wav", "resources\\C5_4.wav", "resources\\C5_6.wav", "resources\\C5_8.wav", "resources\\C5_12.wav", "resources\\C5_16.wav", "resources\\B4_1.wav", "resources\\B4_2.wav", "resources\\B4_3.wav", "resources\\B4_4.wav", "resources\\B4_6.wav", "resources\\B4_8.wav", "resources\\B4_12.wav", "resources\\B4_16.wav", "resources\\A#4_1.wav", "resources\\A#4_2.wav", "resources\\A#4_3.wav", "resources\\A#4_4.wav", "resources\\A#4_6.wav", "resources\\A#4_8.wav", "resources\\A#4_12.wav", "resources\\A#4_16.wav", "resources\\A4_1.wav", "resources\\A4_2.wav", "resources\\A4_3.wav", "resources\\A4_4.wav", "resources\\A4_6.wav", "resources\\A4_8.wav", "resources\\A4_12.wav", "resources\\A4_16.wav", "resources\\G#4_1.wav", "resources\\G#4_2.wav", "resources\\G#4_3.wav", "resources\\G#4_4.wav", "resources\\G#4_6.wav", "resources\\G#4_8.wav", "resources\\G#4_12.wav", "resources\\G#4_16.wav", "resources\\G4_1.wav", "resources\\G4_2.wav", "resources\\G4_3.wav", "resources\\G4_4.wav", "resources\\G4_6.wav", "resources\\G4_8.wav", "resources\\G4_12.wav", "resources\\G4_16.wav", "resources\\F#4_1.wav", "resources\\F#4_2.wav", "resources\\F#4_3.wav", "resources\\F#4_4.wav", "resources\\F#4_6.wav", "resources\\F#4_8.wav", "resources\\F#4_12.wav", "resources\\F#4_16.wav", "resources\\F4_1.wav", "resources\\F4_2.wav", "resources\\F4_3.wav", "resources\\F4_4.wav", "resources\\F4_6.wav", "resources\\F4_8.wav", "resources\\F4_12.wav", "resources\\F4_16.wav", "resources\\E4_1.wav", "resources\\E4_2.wav", "resources\\E4_3.wav", "resources\\E4_4.wav", "resources\\E4_6.wav", "resources\\E4_8.wav", "resources\\E4_12.wav", "resources\\E4_16.wav", "resources\\D#4_1.wav", "resources\\D#4_2.wav", "resources\\D#4_3.wav", "resources\\D#4_4.wav", "resources\\D#4_6.wav", "resources\\D#4_8.wav", "resources\\D#4_12.wav", "resources\\D#4_16.wav", "resources\\D4_1.wav", "resources\\D4_2.wav", "resources\\D4_3.wav", "resources\\D4_4.wav", "resources\\D4_6.wav", "resources\\D4_8.wav", "resources\\D4_12.wav", "resources\\D4_16.wav", "resources\\C#4_1.wav", "resources\\C#4_2.wav", "resources\\C#4_3.wav", "resources\\C#4_4.wav", "resources\\C#4_6.wav", "resources\\C#4_8.wav", "resources\\C#4_12.wav", "resources\\C#4_16.wav", "resources\\C4_1.wav", "resources\\C4_2.wav", "resources\\C4_3.wav", "resources\\C4_4.wav", "resources\\C4_6.wav", "resources\\C4_8.wav", "resources\\C4_12.wav", "resources\\C4_16.wav", "resources\\B3_1.wav", "resources\\B3_2.wav", "resources\\B3_3.wav", "resources\\B3_4.wav", "resources\\B3_6.wav", "resources\\B3_8.wav", "resources\\B3_12.wav", "resources\\B3_16.wav", "resources\\A#3_1.wav", "resources\\A#3_2.wav", "resources\\A#3_3.wav", "resources\\A#3_4.wav", "resources\\A#3_6.wav", "resources\\A#3_8.wav", "resources\\A#3_12.wav", "resources\\A#3_16.wav", "resources\\A3_1.wav", "resources\\A3_2.wav", "resources\\A3_3.wav", "resources\\A3_4.wav", "resources\\A3_6.wav", "resources\\A3_8.wav", "resources\\A3_12.wav", "resources\\A3_16.wav", "resources\\G#3_1.wav", "resources\\G#3_2.wav", "resources\\G#3_3.wav", "resources\\G#3_4.wav", "resources\\G#3_6.wav", "resources\\G#3_8.wav", "resources\\G#3_12.wav", "resources\\G#3_16.wav", "resources\\G3_1.wav", "resources\\G3_2.wav", "resources\\G3_3.wav", "resources\\G3_4.wav", "resources\\G3_6.wav", "resources\\G3_8.wav", "resources\\G3_12.wav", "resources\\G3_16.wav", "resources\\F#3_1.wav", "resources\\F#3_2.wav", "resources\\F#3_3.wav", "resources\\F#3_4.wav", "resources\\F#3_6.wav", "resources\\F#3_8.wav", "resources\\F#3_12.wav", "resources\\F#3_16.wav", "resources\\F3_1.wav", "resources\\F3_2.wav", "resources\\F3_3.wav", "resources\\F3_4.wav", "resources\\F3_6.wav", "resources\\F3_8.wav", "resources\\F3_12.wav", "resources\\F3_16.wav", "resources\\E3_1.wav", "resources\\E3_2.wav", "resources\\E3_3.wav", "resources\\E3_4.wav", "resources\\E3_6.wav", "resources\\E3_8.wav", "resources\\E3_12.wav", "resources\\E3_16.wav", "resources\\D#3_1.wav", "resources\\D#3_2.wav", "resources\\D#3_3.wav", "resources\\D#3_4.wav", "resources\\D#3_6.wav", "resources\\D#3_8.wav", "resources\\D#3_12.wav", "resources\\D#3_16.wav", "resources\\D3_1.wav", "resources\\D3_2.wav", "resources\\D3_3.wav", "resources\\D3_4.wav", "resources\\D3_6.wav", "resources\\D3_8.wav", "resources\\D3_12.wav", "resources\\D3_16.wav", "resources\\C#3_1.wav", "resources\\C#3_2.wav", "resources\\C#3_3.wav", "resources\\C#3_4.wav", "resources\\C#3_6.wav", "resources\\C#3_8.wav", "resources\\C#3_12.wav", "resources\\C#3_16.wav", "resources\\C3_1.wav", "resources\\C3_2.wav", "resources\\C3_3.wav", "resources\\C3_4.wav", "resources\\C3_6.wav", "resources\\C3_8.wav", "resources\\C3_12.wav", "resources\\C3_16.wav", "resources\\B2_1.wav", "resources\\B2_2.wav", "resources\\B2_3.wav", "resources\\B2_4.wav", "resources\\B2_6.wav", "resources\\B2_8.wav", "resources\\B2_12.wav", "resources\\B2_16.wav", "resources\\A#2_1.wav", "resources\\A#2_2.wav", "resources\\A#2_3.wav", "resources\\A#2_4.wav", "resources\\A#2_6.wav", "resources\\A#2_8.wav", "resources\\A#2_12.wav", "resources\\A#2_16.wav", "resources\\A2_1.wav", "resources\\A2_2.wav", "resources\\A2_3.wav", "resources\\A2_4.wav", "resources\\A2_6.wav", "resources\\A2_8.wav", "resources\\A2_12.wav", "resources\\A2_16.wav", "resources\\G#2_1.wav", "resources\\G#2_2.wav", "resources\\G#2_3.wav", "resources\\G#2_4.wav", "resources\\G#2_6.wav", "resources\\G#2_8.wav", "resources\\G#2_12.wav", "resources\\G#2_16.wav", "resources\\G2_1.wav", "resources\\G2_2.wav", "resources\\G2_3.wav", "resources\\G2_4.wav", "resources\\G2_6.wav", "resources\\G2_8.wav", "resources\\G2_12.wav", "resources\\G2_16.wav", "resources\\F#2_1.wav", "resources\\F#2_2.wav", "resources\\F#2_3.wav", "resources\\F#2_4.wav", "resources\\F#2_6.wav", "resources\\F#2_8.wav", "resources\\F#2_12.wav", "resources\\F#2_16.wav", "resources\\F2_1.wav", "resources\\F2_2.wav", "resources\\F2_3.wav", "resources\\F2_4.wav", "resources\\F2_6.wav", "resources\\F2_8.wav", "resources\\F2_12.wav", "resources\\F2_16.wav", "resources\\E2_1.wav", "resources\\E2_2.wav", "resources\\E2_3.wav", "resources\\E2_4.wav", "resources\\E2_6.wav", "resources\\E2_8.wav", "resources\\E2_12.wav", "resources\\E2_16.wav", "resources\\D#2_1.wav", "resources\\D#2_2.wav", "resources\\D#2_3.wav", "resources\\D#2_4.wav", "resources\\D#2_6.wav", "resources\\D#2_8.wav", "resources\\D#2_12.wav", "resources\\D#2_16.wav", "resources\\D2_1.wav", "resources\\D2_2.wav", "resources\\D2_3.wav", "resources\\D2_4.wav", "resources\\D2_6.wav", "resources\\D2_8.wav", "resources\\D2_12.wav", "resources\\D2_16.wav", "resources\\C#2_1.wav", "resources\\C#2_2.wav", "resources\\C#2_3.wav", "resources\\C#2_4.wav", "resources\\C#2_6.wav", "resources\\C#2_8.wav", "resources\\C#2_12.wav", "resources\\C#2_16.wav", "resources\\C2_1.wav", "resources\\C2_2.wav", "resources\\C2_3.wav", "resources\\C2_4.wav", "resources\\C2_6.wav", "resources\\C2_8.wav", "resources\\C2_12.wav", "resources\\C2_16.wav", ]
scales = [[0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23], [0, 2, 3, 5, 7, 9, 10, 12, 14, 15, 17, 19, 21, 22], [0, 1, 3, 5, 7, 8, 10, 12, 13, 15, 17, 19, 20, 22], [0, 2, 4, 6, 7, 9, 11, 12, 14, 16, 18, 19, 21, 23], [0, 2, 4, 5, 7, 9, 10, 12, 14, 16, 17, 19, 21, 22], [0, 2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22]]

chord_sus2 = [0, 1, 3, 4, 5]
chord_sus4 = [0, 1, 2, 4, 5]
c4_id=377

key = 0    #0-11, 0 is C, 11 is B
scale = 0   #0-5, 0 is major, 5 is minor
complexity = 0
density = 0

main_window = Tk()
main_window.title("Chordify v1.0")
generate_button = Button(main_window, text="Generate progression", width=30, command=generate_progression)
generate_button.pack()
scale_combobox = Combobox(main_window, height=6, state="readonly", values=["Major", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Minor"], width=12)
scale_combobox.pack()
key_combobox = Combobox(main_window, height=12, state="readonly", values=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], width=5)
key_combobox.pack()
complexity_combobox = Combobox(main_window, height=8, state="readonly", values=["1", "2", "3", "4", "5", "6", "7", "8"], width=5)
complexity_combobox.pack()
density_combobox = Combobox(main_window, height=8, state="readonly", values=["1", "2", "3", "4", "5", "6", "7", "8"], width=5)
density_combobox.pack()
play_button = Button(main_window, text="Play", width=10, command=chord_type_switcher.play_audio)
play_button.pack()
stop_button = Button(main_window, text="Stop", width=10)
stop_button.pack()
save_button = Button(main_window, text="Save progression", width=20)
save_button.pack()
load_button = Button(main_window, text="Load progression", width=20)
load_button.pack()


main_window.mainloop()
