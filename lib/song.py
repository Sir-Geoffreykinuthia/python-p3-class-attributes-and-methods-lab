class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        Song.genres.add(self.genre)
        Song.genre_count.setdefault(self.genre, 0)
        Song.genre_count[self.genre] += 1

    def add_to_artists(self):
        Song.artists.add(self.artist)
        Song.artist_count.setdefault(self.artist, 0)
        Song.artist_count[self.artist] += 1

    @classmethod
    def get_total_songs(cls):
        return cls.count