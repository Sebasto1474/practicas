class MediaError(Exception):
    """Custom exception for media-related errors."""
    def __init__(self, message,obj):
        super().__init__(message)
        self.obj = obj
class Movie:
    """Parent class representing a movie."""
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if year < 1895:
            raise ValueError("Year must be 1895 or later")
        if not director.strip():
            raise ValueError("Director cannot be empty.")
        if duration <= 0:
            raise ValueError("Duration must be positive")
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"

class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    def __init__(self):
        self.items = []

    def add(self,media_item):
        if not isinstance(media_item, Movie):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        return self.items.append(media_item)

    def get_movies(self):
        movies = []
        for m in self.items:
            if type(m) == Movie:
                movies.append(m) # optimizado 'return [item for item in self.items if type(item) is Movie]'
        return movies

    def get_tv_series(self):
        return [item for item in self.items if type(item) is TVSeries]

    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        movies = self.get_movies()
        series = self.get_tv_series()
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        if movies:
            result += "=== MOVIES ===\n"
            for index, movie in enumerate(movies, 1):
                result += f"{index}. {movie}\n"
        if series:
            result += "=== SERIES ===\n"
            for index, serie in enumerate(series,1):
                result += f"{index}. {serie}\n"
        return result
class TVSeries(Movie):
    """Child class representing an entire TV series."""
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title,year,director,duration)
        if seasons < 1:
            raise ValueError("Seasons must be 1 or greater")
        if total_episodes < 1:
            raise ValueError("Total episodes must be 1 or greater")
        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}"


catalogue = MediaCatalogue()

try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    catalogue.add(movie1)
    movie2 = Movie("Lord of the rings: The fellowship of the ring", 2001, "Peter Jackson", 178)
    catalogue.add(movie2)
    series1 = TVSeries("The Wire", 2002, "David Simon", 60, 5, 60)
    catalogue.add(series1)
    series2 = TVSeries("Breaking Bad", 2006, "Vince Gilligan", 60, 5, 75)
    catalogue.add(series2)
    print(catalogue)
except MediaError as e:
    print(f'Media Error: {e}')
    print(f"Unable tu add {e.obj}: {type(e.obj)}")
