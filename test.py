from Audio import Audio
from Fingerprints import Fingerprints
from DB import DB
from collections import Counter

import matplotlib.pyplot as plt

def visualize(fp):
	plt.figure(fp.audio.filename)
	plt.imshow(fp.audio.S, origin='lower')
	plt.title('STFT Magnitude')
	plt.ylabel('Frequency bins')
	plt.xlabel('Time bins')

	t, f = zip(*fp.ind)
	plt.plot(t, f, 'ro')

db = DB('test')

# Audio
audio = Audio('excerpts/cant_ex.wav')
fp = Fingerprints(audio)
visualize(fp)
db.store(fp)

# Excerpt
audio2 = Audio('excerpts/cant_ex_ex.wav')
fp2 = Fingerprints(audio2)
visualize(fp2)

times = []
res = []
for row in fp2.data:
	entries = db.get(row)
	for entry in entries:
		times.append(entry[1] - row[1])
		res.append((row[2], entry[1] - row[1]))

occurence_count = Counter(times)
res = occurence_count.most_common(1)[0][0]
print(occurence_count)