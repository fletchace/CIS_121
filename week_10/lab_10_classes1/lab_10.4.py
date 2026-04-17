class Movie:
    def __init__(self, title, director, runtime_minutes):
        self.title = title
        self.director = director
        self.runtime_minutes = runtime_minutes

    # Getters
    def get_title(self):
        return self.title

    def get_director(self):
        return self.director

    def get_runtime_minutes(self):
        return self.runtime_minutes

    # Setters
    def set_title(self, new_title):
        self.title = new_title

    def set_director(self, new_director):
        self.director = new_director

    def set_runtime_minutes(self, new_runtime):
        self.runtime_minutes = new_runtime


# Create an instance of the class
my_movie = Movie("Inception", "Christopher Nolan", 148)

# Example usage (optional)
print(my_movie.get_title())
print(my_movie.get_director())
print(my_movie.get_runtime_minutes())