from project1 import media
from project1.ud036_StarterCode import fresh_tomatoes

tbbt = media.Movie("The Big Bang Theory",
                   "https://images8.alphacoders.com/431/431311.jpg",
                   "https://www.youtube.com/watch?v=PAm8PV47jMM")


modern_family = media.Movie("Modern Family",
                            ("https://images.tenplay.com.au/~/media/TV%20Shows"
                             "/Modern%20Family/Season%208/ModernFamily_S8_Logo"
                             "_620x349.jpg"),
                            "https://www.youtube.com/watch?v=meF4MfQ3jMw")

broken_girls = media.Movie("2 Broken Girls",
                           "http://i.gtimg.cn/qqlive/img/jpgcache/files/"
                           "qqvideo/2/2ih1wnad4h30y5n.jpg",
                           "https://www.youtube.com/watch?v=f-V6dYUkneU")

flipped = media.Movie("Flipped",
                      ("https://images-na.ssl-images-amazon."
                       "com/images/M/MV5BMTU2NjQ1Nzc4MF5BMl5BanBnXkFtZ"
                       "TcwNTM0NDk1Mw@@._V1_UY1200_CR89,0,6301200_AL_.jpg"),
                      "https://www.youtube.com/watch?v=RDlXdujRSD8")

movies = [tbbt, modern_family, broken_girls, flipped]

fresh_tomatoes.open_movies_page(movies)
