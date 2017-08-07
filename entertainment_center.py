import media
from ud036_StarterCode import fresh_tomatoes

"""the instances and show final website"""

tbbt = media.Movie("The Big Bang Theory",
                   ("http://i.cdn.turner.com/v5cache/TBS/Images/Dynamic/"
                    "i450/vizio-the-big-bang-theory-960x1440.png"),
                   "https://www.youtube.com/watch?v=PAm8PV47jMM")

modern_family = media.Movie("Modern Family",
                            ("https://almostelysian.files.wordpress.com/"
                             "2015/09/modern-family.jpg?w=640"),
                            "https://www.youtube.com/watch?v=meF4MfQ3jMw")

broken_girls = media.Movie("2 Broken Girls",
                           ("http://i.gtimg.cn/qqlive/img/jpgcache/files/"
                            "qqvideo/2/2ih1wnad4h30y5n.jpg"),
                           "https://www.youtube.com/watch?v=f-V6dYUkneU")

flipped = media.Movie("Flipped",
                      ("https://images-na.ssl-images-amazon."
                       "com/images/M/MV5BMTU2NjQ1Nzc4MF5BMl5BanBnXkFtZ"
                       "TcwNTM0NDk1Mw@@._V1_UY1200_CR89,0,6301200_AL_.jpg"),
                      "https://www.youtube.com/watch?v=RDlXdujRSD8")

house_of_cards = media.Movie("House of Cards",
                             ("http://img1.gtimg.com/tech/pics/hv1/18/14/1259/"
                              "81870063.jpg"),
                             "https://www.youtube.com/watch?v=8QnMmpfKWvo")

devious_maids = media.Movie("Devious Maids",
                            ("http://i.gtimg.cn/qqlive/img/jpgcache/files/"
                             "qqvideo/q/qk8vyb5drwnn174.jpg"),
                            "https://www.youtube.com/watch?v=JAh-5K2F7dI")

movies = [tbbt, modern_family, broken_girls, flipped, house_of_cards,
          devious_maids]

fresh_tomatoes.open_movies_page(movies)
