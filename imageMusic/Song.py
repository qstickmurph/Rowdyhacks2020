from pydub import AudioSegment

class Song:
	def __init__(self):
		self.key = 2
		self.octave = 1
		self.tempo = 4
		self.instrumentation = None
		
	def tempo(self, luminosity):
		val = 768 / 4
		if luminosity < val:
			self.tempo = 1
		elif luminosity < val * 2:
			self.tempo = 2
		elif luminosity < val * 3:
			self.tempo = 3
		else:
			self.tempo = 4
		
	def key(self, value ):
		keys = 12
		rgb_total_slice = 768/keys
		for i in range(keys):
			if value < rgb_total_slice * i:
				self.key = i
				return i
		
	def octave(self, value):
		value_max = value / 5 #5 is a placeholder
		for i in range(5):
			if value < value_max * i:
				self.octave = i
				return i
	
	def instrumentation(self, value):
		pass
	
	@staticmethod
	def construct_chord(audio_1, audio_2, audio_3):
		new_sound = AudioSegment.empty()
		if len(audio_1) > len(audio_2):
			new_sound = audio_1.overlay(audio_2)
		else:
			new_sound = audio_2.overlay(audio_1)
			
		if len(new_sound) > len(audio_3):
			new_sound = new_sound.overlay(audio_3)
		else:
			new_sound = audio_3.overlay(new_sound)
		return new_sound
	
	@staticmethod
	def note( value, key=1, octave=1):
		#select audio file based on value and key
		note_list = Song.get_key_notes(key)
		tk = 9
		note = ""
		if value % tk == 0:
			note = note_list[0]
		elif value % tk == 1:
			note = note_list[1]
		elif value % tk == 2:
			note = note_list[2]
		elif value % tk == 3:
			note = note_list[3]
		elif value % tk == 4:
			note = note_list[4]
		elif value % tk == 5:
			note = note_list[5]
		elif value % tk == 6:
			note = note_list[6]
		else: #for now this else conditions is tasked with building chords
		
			audio_name_1 = "sounds/" + str(octave) + "/" + note_list[0]
			audio_name_2 = "sounds/" + str(octave) + "/" + note_list[1]
			audio_name_3 = "sounds/" + str(octave) + "/" + note_list[2]
			
			audio_1 = AudioSegment.from_file(audio_name_1, format="wav")
			audio_2 = AudioSegment.from_file(audio_name_2, format="wav")
			audio_3 = AudioSegment.from_file(audio_name_3, format="wav")
			
			return Song.construct_chord(audio_1, audio_2, audio_3)
		audio_name = "sounds/" + str(octave) + "/" + note
		return AudioSegment.from_file(audio_name, format="wav")
	
	def get_key_notes(key):
		if(key == 1):#C major
			return ["ff.C4.wav", "ff.B4.wav", "ff.A4.wav", "ff.E4.wav", "ff.F4.wav", "ff.G4.wav", "ff.D4.wav"]
		elif(key == 2):#c minor
			return ["ff.C4.wav", "ff.Bb4.wav", "ff.Ab4.wav", "ff.Eb4.wav", "ff.F4.wav", "ff.G4.wav", "ff.D4.wav"]
		elif(key == 3):#D major
			return ["ff.Db4.wav", "ff.Bb4.wav", "ff.Ab4.wav", "ff.Eb4.wav", "ff.F4.wav", "ff.Gb4.wav", "ff.D4.wav"]
		elif(key == 4):#D minor
			return ["ff.C4.wav", "ff.Bb4.wav", "ff.A4.wav", "ff.E4.wav", "ff.F4.wav", "ff.G4.wav", "ff.D4.wav"]
		elif(key == 5):#E major
			return ["ff.Db4.wav", "ff.B4.wav", "ff.A4.wav", "ff.E4.wav", "ff.Gb4.wav", "ff.G4.wav", "ff.Eb4.wav"]
		elif(key == 6):# E minor (same notes as d minor)
			return ["ff.C4.wav", "ff.Bb4.wav", "ff.A4.wav", "ff.E4.wav", "ff.Gb.wav", "ff.G4.wav", "ff.D4.wav"]
	
	def concatenate_melody(self, pixel_list):
		octave = 1
		sound = AudioSegment.empty() #initialize empty audio segment
		for i in range(len(pixel_list)):
			sound_temp = Song.note(value=pixel_list[i], key=self.key, octave=self.octave)
			sound_temp = self.adjust_for_tempo(sound_temp)
			sound = sound + sound_temp
		self.song = sound
		
	def adjust_for_tempo(self, audio):
		truncator = AudioSegment.empty()
		if self.tempo == 1:
			truncator = AudioSegment.silent(duration=1000)
			truncator.fade_out(duration=600)
		elif self.tempo ==  2:
			truncator = AudioSegment.silent(duration=2000)
			truncator.fade_out(duration=1500)
		else:
			truncator = AudioSegment.silent(duration=3000)
			truncator.fade_out(duration=2500)
		
		return truncator.overlay(audio)
	
	def download_song(self, name):
		self.song.export(name, format="wav", bitrate="192k")
		
	def set_key(self, key):
		self.key = key
		
	def set_tempo(self, tempo):
		self.tempo = tempo
		
	def set_octabe(self, oct):
		self.octave = oct