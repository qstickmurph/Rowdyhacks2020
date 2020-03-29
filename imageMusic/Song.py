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
	
	#@staticmethod
	def note( value, key=1, octave=1):
		#select audio file based on value and key
		#placeholder way to select nodes ( currently independent of key )
		note = ""
		print(str(value))
		if value % 7 == 0:
			note = "ff.C4.wav"
		elif value % 7 == 1:
			note = "ff.B4.wav"
		elif value % 7 == 2:
			note = "ff.A4.wav"
		elif value % 7 == 3:
			note = "ff.E4.wav"
		elif value % 7 == 4:
			note = "ff.F4.wav"
		elif value % 7 == 5:
			note = "ff.G4.wav"
		else:
			note = "ff.D4.wav"
		#
		audio_name = "sounds/"
		audio_name = audio_name + str(octave) + "/" + note
		file = open(audio_name, "r")
		
		return AudioSegment.from_file(audio_name, format="wav")
	
	def concatenate_melody(self, pixel_list):
		octave = 1
		sound = AudioSegment.empty() #initialize empty audio segment
		for i in range(len(pixel_list)):
			print(pixel_list[i])
			sound = sound + Song.note(value=pixel_list[i], key=self.key, octave=1)
		self.song = sound
	
	def download_song(self, name):
		self.song.export(name, format="wav", bitrate="192k")
