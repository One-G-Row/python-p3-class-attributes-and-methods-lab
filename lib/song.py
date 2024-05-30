class Song:
    count = 0
    genres = []
    genre_count = {"Rap": 5, "Rock": 1, "Country": 3}
    artists = []
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_genres(genre)
        Song.add_song_to_count()
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    """  @classmethod
    def show_genres(cls):
        print([genre.name for genre in cls.genres]) """

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
jireh = Song("jireh", "maverick city", "gospel")
#print(Song.genres)
