import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story 4", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", "https://www.youtube.com/watch?v=wmiIUN-7qhE")

#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://images-na.ssl-images-amazon.com/images/I/61OUGpUfAyL._SY679_.jpg", "https://www.youtube.com/watch?v=6ziBFh3V1aM")

#print(avatar.storyline)

#avatar.show_trailer()

harry_potter = media.Movie("Harry Potter", "The boy who lived", "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/harry-potter-and-the-chamber-of-secrets-poster-1545148861.jpg", "https://www.youtube.com/watch?v=VyHV0BRtdxo")

#harry_potter.show_trailer()

movies = [toy_story, avatar, harry_potter]

fresh_tomatoes.open_movies_page(movies)
