from pydub import AudioSegment

class Song:
	def __init__(self):
		self.key = 1
		self.octave = 1
		self.instrumentation = None
		
	def tempo(self, luminosity):
		pass
		
	def key(self, value ):
		keys = 12
		rgb_total_slice = 768/keys
		for i in range(keys):
			if value < rgb_total_slice * i:
				return i
		
		
	def octave(self, value):
		value_max = 1000  / 5 #1000 is a placeholder
		for i in range(5):
			if value < value_max * i:
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
	
	#TODO: Algorithm for choosing proper key
	#TODO: Eliminate redundency
	@staticmethod
	def note( value, key=1, octave=1):
		#select audio file based on value and key
		#placeholder way to select nodes ( currently independent of key )
		tk = 9
		note = ""
		if value % tk == 0:
			note = "ff.C4.wav"
		elif value % tk == 1:
			note = "ff.B4.wav"
		elif value % tk == 2:
			note = "ff.A4.wav"
		elif value % tk == 3:
			note = "ff.E4.wav"
		elif value % tk == 4:
			note = "ff.F4.wav"
		elif value % tk == 5:
			note = "ff.G4.wav"
		elif value % tk == 6:
			note = "ff.D4.wav"
		else: #for now this else conditions is tasked with building chords
		
			note_1 = "ff.C4.wav"
			note_2 = "ff.E4.wav"
			note_3 = "ff.G4.wav"
		
			audio_name_1 = "sounds/" + str(octave) + "/" + note_1
			audio_name_2 = "sounds/" + str(octave) + "/" + note_2
			audio_name_3 = "sounds/" + str(octave) + "/" + note_3
			
			audio_1 = AudioSegment.from_file(audio_name_1, format="wav")
			audio_2 = AudioSegment.from_file(audio_name_2, format="wav")
			audio_3 = AudioSegment.from_file(audio_name_3, format="wav")
			
			return Song.construct_chord(audio_1, audio_2, audio_3)
		audio_name = "sounds/" + str(octave) + "/" + note
		return AudioSegment.from_file(audio_name, format="wav")
		
	
	def concatenate_melody(self, pixel_list):
		octave = 1
		sound = AudioSegment.empty() #initialize empty audio segment
		for i in range(len(pixel_list)):
			sound = sound + Song.note(value=pixel_list[i], key=self.key, octave=1)
		self.song = sound
	
	def download_song(self, name):
		self.song.export(name, format="wav", bitrate="192k")
