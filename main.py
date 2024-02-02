import django_connect
from games.models import Game, Genre

# genre_shooter = Genre(
#     name="Shooter", 
#     description="In this genre you need to kill enemies by shooting in them"
# )

# genre_advantures = Genre(
#     name="Advantures",
#     description="This genre is perfect for players that like to travel and solve mysteries in different places"
# )

# hogwarts_legacy = Game(
#     name="Hogwarts Legacy",
#     year=2023,
#     rate=9
# )

# destiny_2 = Game(
#     name="Destiny 2",
#     year=2017,
#     rate=9
# )

# genre_shooter.save()
# genre_advantures.save()

# hogwarts_legacy.save()
# destiny_2.save()

hogwarts_legacy = Game.objects.filter(name="Hogwarts Legacy", id = 1).first()
adventure_genre = Genre.objects.get(id=2)

hogwarts_legacy.genre.add(adventure_genre)

destiny_2 = Game.objects.get(id=2)
shooter_genre = Genre.objects.get(id=1)

destiny_2.genre.add(shooter_genre)
