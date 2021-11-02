import glob
import os

from Audio import Audio
from Fingerprints import Fingerprints
from DB import DB

db = DB()

path = 'sounds/'
i = 0
for filename in glob.glob(os.path.join(path, '*.wav')):
	i += 1
	audio = Audio(filename, i)
	fp = Fingerprints(audio)
	db.store(fp)
	print(filename)