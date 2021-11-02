from Audio import Audio
from Fingerprints import Fingerprints
from DB import DB

import time

# Load database
db = DB()

# Load excerpt
audio = Audio('excerpts/01 - La Mauvaise Réputation.wav')
audio = Audio('excerpts/03 - Le Gorille.wav')
audio = Audio('excerpts/07 - La Chasse aux papillons.wav')
fp = Fingerprints(audio)

# Search best match
diff_counter = {}
best_count = 0
best_align = 0
song_id = -1

start = time.time()

for row in fp.data:
	entries = db.get(row)
	for entry in entries:

		delta = entry[1] - row[1]

		if entry[2] not in diff_counter:
			diff_counter[entry[2]] = {}

		if delta not in diff_counter[entry[2]]:
			diff_counter[entry[2]][delta] = 0

		diff_counter[entry[2]][delta] += 1

		if diff_counter[entry[2]][delta] > best_count:
			best_count = diff_counter[entry[2]][delta]
			best_align = delta
			song_id = entry[2]

end = time.time()
print("Match time : ", end - start)

print("Match found in song {} at {} seconds".format(song_id, best_align * 1024 / 44100))

# occurence_count = Counter(diff_counter)
# # res = occurence_count.most_common(1)[0][0]
# print(occurence_count)