import numpy as np
import scipy.ndimage.filters as filters
import hashlib

class Fingerprints:

	constellation = 5

	def __init__(self, audio) -> None:
		self.data = []
		self.audio = audio
		self.audio.stft()
		self.compute()

	# def findPeaks(self):
	# 	neighborhood_size = (100, 10)
	# 	neighborhood_size = 50
	# 	neighborhood_size = (15, 7)
	# 	data = self.audio.S
	# 	data_max = filters.maximum_filter(data, neighborhood_size)
	# 	maxima = (data == data_max)
	# 	threshold = np.mean(data_max)
	# 	data_min = filters.minimum_filter(data, neighborhood_size)
	# 	diff = ((data_max - data_min) > threshold)
	# 	maxima[diff == 0] = 0
	# 	self.ind = np.transpose(maxima.nonzero())
	# 	return self.ind

	def findPeaks(self):
		neighborhood_size = (15, 11)
		data = np.transpose(self.audio.S)
		data_max = filters.maximum_filter(data, neighborhood_size)
		map = np.logical_and(data == data_max, data_max > 1000)
		self.ind = np.transpose(map.nonzero())
		return self.ind

	def compute(self) -> None:
		self.peaks = self.findPeaks()
		for i in range(0, len(self.peaks)):
			for j in range(1, self.constellation):
				if (i + j) < len(self.peaks):
					f1 = self.peaks[i][1]
					f2 = self.peaks[i + j][1]
					t1 = self.peaks[i][0]
					t2 = self.peaks[i + j][0]
					t_delta = t2 - t1
					h = hashlib.sha1(f"{str(f1)}|{str(f2)}|{str(t_delta)}".encode('utf-8'))
					# self.data.append((h.hexdigest()[0:10], int(t1), self.audio.filename))
					# self.data.append((h.hexdigest()[0:10], int(t1), 0))
					# self.data.append((h.hexdigest(), int(t1), 0))
					# self.data.append((f"{str(f1)}|{str(f2)}|{str(t_delta)}", int(t1), 0))
					h = ((np.uint8(f1) << 8) + np.uint8(f2) << 16) + np.uint16(t_delta)
					self.data.append((int(h), int(t1), self.audio.id))