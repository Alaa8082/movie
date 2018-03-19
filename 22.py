
import fresh_tomatoes
import media

Inception = media.Movie("Inception",
						"Dom Cobb  is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious.",
						"https://upload.wikimedia.org/wikipedia/en/1/18/Inception_OST.jpg",
						"https://www.youtube.com/watch?v=66TuSJo4dZM")

#print (Inception.storyline)
#Inception.show_trailer()


Interstellar = media.Movie("Interstellar",
						"In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole.",
						"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
						"https://www.youtube.com/watch?v=zSWdZVtXT7E")


rise_of_an_empire = media.Movie("300 rise of an empire",
						"While King Leonidas and his 300 Spartans have their date with destiny at Thermopylae, another battle against the Persians is brewing, this time at sea.",
						"https://upload.wikimedia.org/wikipedia/en/9/91/300_Rise_of_an_Empire.jpg",
						"https://www.youtube.com/watch?v=XDnXI6KXoeg")

liste_monies=[Inception,Interstellar,rise_of_an_empire]
#movies = [Inception,Interstellar,rise_of_an_empire]
#fresh_tomatoes.open_movies_page(movies)
#alaa hassan
print (media.Movie.__name__)
print (media.Movie.__module__)

