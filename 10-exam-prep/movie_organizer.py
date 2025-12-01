def movie_organizer(*movie_genre):
    genre_movies_list = {}  # {genre: [movie_1, movie_2, ...]
    for data in movie_genre:
        movie, genre = data
        if genre not in genre_movies_list:
            genre_movies_list[genre] = []
        genre_movies_list[genre].append(movie)
    
    sorted_genre = sorted(genre_movies_list.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    
    output = []
    for genre, unsorted_movies in sorted_genre:
        output.append(f"{genre} - {len(unsorted_movies)}")
        sorted_movies = sorted(unsorted_movies)
        
        for movie in sorted_movies:
            output.append(f"* {movie}")
    
    return "\n".join(output)


# print(movie_organizer(
#     ("The Matrix", "Sci-fi")))

# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
