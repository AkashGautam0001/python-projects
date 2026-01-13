import os
import json

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(movies, file, indent=2)

def add_movies(movies):
    title = input("Enter the movie name : ").strip().lower()
    if any(movie["title"].lower() == title for movie in movies):
        print("Movie Already Exits!")
        return
    genre = input("Genre : ").strip().lower()
    try:
        rating = float(input("Enter rating(0-10): "))
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Please enter valid number")
        return
    
    movies.append({
        "title":title,
        "genre" : genre,
        "rating" : rating
    })

    save_movies(movies)
    print("Movie added ✅")

def search_movies(movies):
    term = input("Enter the title or genre : ").strip().lower()

    results = [
        movie for movie in movies
        if term in movie["title"].lower() or term in movie["genre"].lower()
    ]
    if not results:
        print("No matching result")
        return
    print(f"Fount {len(results)} result(s)")
    for movie in results:
        if "title" in movie and "genre" in movie and "rating" in movie:
            print(f"{movie['title']} -- {movie['genre']} -- {movie['rating']}")
        else:
            print("Error: Movie object is missing one or more of the required fields")

def view_movies(movies):
    if not movies:
        print("No Movies in DB")    
        return
    print("-"*30)
    print("Your Movies are : ")
    for movie in movies:
        print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")
    print("-"*30)

def run_movie_db():
    movies = load_movies()
    while True:
        print("\n My Moive DB 🍿🥤")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Exit")

        choice = input("Choose an option (1-4) : ").strip()
        match choice: 
            case "1" : add_movies(movies)
            case "2" : view_movies(movies)
            case "3" : search_movies(movies)
            case "4" : break
            case _: print("Enter a valid choice")

if __name__ == "__main__":
    run_movie_db()