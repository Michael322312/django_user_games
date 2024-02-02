from games.models import Game, Genre
import django_connect

genre_shooter = Genre(
    name="Shooter", 
    description="In this genre you need to kill enemies by shooting in them"
)

genre_advantures = Genre(
    name="Advantures",
    description="This genre is perfect for players that like to travel and solve mysteries in different places"
)

hogwarts_legacy = Game(
    name="Hogwarts Legacy",
    year=2023,
    rate=9
)

destiny_2 = Game(
    name="Destiny 2",
    year=2017,
    rate=9
)