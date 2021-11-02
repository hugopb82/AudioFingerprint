import sqlite3

class DB:

	# CREATE_FINGERPRINTS_TABLE = """
	# 	CREATE TABLE IF NOT EXISTS fingerprints (
	# 		hash TEXT NOT NULL,
	# 		offset INT UNSIGNED NOT NULL,
	# 		song VARCHAR(255) NOT NULL
	# 	)
	# """

	CREATE_FINGERPRINTS_TABLE = """
		CREATE TABLE IF NOT EXISTS fingerprints (
			hash INT UNSIGNED NOT NULL,
			offset INT UNSIGNED NOT NULL,
			song INT UNSIGNED NOT NULL
		)
	"""
	# CONSTRAINT `uq_fingerprints` UNIQUE (hash, offset, song_id)

	INSERT_FINGERPRINT = """
		INSERT INTO fingerprints 
			(hash, offset, song) 
		VALUES 
			(?, ?, ?);
	"""

	GET_FINGERPRINT = """
		SELECT * FROM fingerprints WHERE hash = ?
	"""

	def __init__(self, db: str = 'example') -> None:
		self.con = sqlite3.connect('db/{}.db'.format(db))
		self.cur = self.con.cursor()
		self.setup()

	def setup(self) -> None:
		self.cur.execute(self.CREATE_FINGERPRINTS_TABLE)

	def store(self, fingerprints) -> None:
		self.cur.executemany(self.INSERT_FINGERPRINT, fingerprints.data)
		self.con.commit()

	def get(self, hash):
		self.cur.execute(self.GET_FINGERPRINT, [hash[0]])
		return self.cur.fetchall()