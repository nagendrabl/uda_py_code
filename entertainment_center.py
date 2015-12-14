import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwZH85NQC4")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock",
                        "STory Line",
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                        "STory Line",
                        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")


midnight_in_paris = media.Movie("Midnight in Paris",
                        "STory Line",
                        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=atLg2wQQxvU")


hunger_games = media.Movie("Hunger Games",
                        "STory Line",
                        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=PbA63ayH0bo")

movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
print(media.Movie.__doc__)
#fresh_tomatoes.open_movies_page(movies)
#avatar.showtrailer()




