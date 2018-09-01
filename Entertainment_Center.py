import Movie_Website
import Fresh_tomatoes

toy_story=Movie_Website.Movie('Toy Story','A story of a boy and his toys that come to life','https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg','https://www.youtube.com/watch?v=KYz2wyBy3kc')

#print toy_story.storyline
#toy_story.show_trailer()

avatar = Movie_Website.Movie('Avatar','A marine on alien planet','https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg','https://www.youtube.com/watch?v=d1_JBMrrYw8')

#print avatar.storyline
#avatar.show_trailer()

wallE = Movie_Website.Movie('Wall-E','A robot on earth','https://en.wikipedia.org/dwiki/WALL-E#/meia/File:WALL-Eposter.jpg','https://www.youtube.com/watch?v=ZisWjdjs-gM')
#print wallE.storyline
#wallE.show_trailer()

movies=[toy_story,avatar,wallE]
Fresh_tomatoes.open_movies_page(movies)
#print Movie_Website.Movie.VALID_RATING
#print Movie_Website.Movie.__doc__ +"  "+ Movie_Website.Movie.__name__+"  "+ Movie_Website.Movie.__module__
