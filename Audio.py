from scipy.io import wavfile
from scipy import signal
import numpy as np

class Audio:

	def __init__(self, filename: str, id = 0) -> None:
		self.id = id
		self.filename = filename
		self.load()

	def load(self) -> None:
		self.sr, self.y = wavfile.read(self.filename)

	def stft(self, nperseg: int = 2048, noverlap: int = 1024) -> None:
		self.f, self.t, self.Y = signal.stft(
			self.y, self.sr, nperseg=nperseg, noverlap = noverlap
		)
		# self.S = 10 * np.log10(np.abs(self.Y))
		# self.S = np.power(np.abs(self.Y), 2)
		self.S = np.abs(self.Y[:48, :None])
		
		# band = (self.f < 5000).nonzero()
		# self.S = self.S[band, :][0]

		return self.f, self.t, self.Y, self.S