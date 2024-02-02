# Start


So first of all lets create django project `django_games` by writing in terminal:
```Terminal
django-admin startproject django_games .
```

After that let's create app `games` by this terminal-command:
```
python3 manage.py startapp games
```

Great! We have django-project `django_games` and django-app `games`

Now lets add in `django_games/settings.py` our app:
```python
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "games",
]
```


## Creating Models
So open file `games/models.py` (Right now it's empty)

```python
from django.db import models

# Create your models here.
```

After that I created model `Genre` with `name` and `description`

```python
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
```

And then model of `Game`
```python
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ManyToManyField("Genre", related_name="genres")
    year = models.IntegerField()
    rate = models.DecimalField(decimal_places=1, max_digits=10)
```

Now let's look at each field

  - `CharField()` - used for short text and has argument `max_length` that set string lentgh limit.
  - `TextField()` - usally used for long text, such as descriptions, bio, info etc.
  - `ManyToMany()` - makes `ForgeinKey` for table that stores column from other table.
  - `IntegerField()` - used for numbers, or in other words `int`.
  - `DecimalField()` - used for floating-point numbers (1.2, 3.33, 7.99).

(I only viewed django-func's that I used, but you can look up more)


### Making migrations of models
To create migration write in terminal:
```
python3 manage.py makemigrations
```

And after that we need to make migration
```
python3 manage.py migrate
```


# Work with DB

Work with django-project/app database you can view here:
```python
import django_connect
from games.models import Game, Genre


def create_genres():
    genre_shooter = Genre(
        name="Shooter", 
        description="In this genre you need to kill enemies by shooting in them"
    )

    genre_advantures = Genre(
        name="Advantures",
        description="This genre is perfect for players that like to travel and solve mysteries in different places"
    )

    genre_shooter.save()
    genre_advantures.save()


def create_games():
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

    hogwarts_legacy.save()
    destiny_2.save()

def add_genres_to_games():
    hogwarts_legacy = Game.objects.filter(name="Hogwarts Legacy", id = 1).first()
    adventure_genre = Genre.objects.get(id=2)

    hogwarts_legacy.genre.add(adventure_genre)

    destiny_2 = Game.objects.get(id=2)
    shooter_genre = Genre.objects.get(id=1)

    destiny_2.genre.add(shooter_genre)


def show_all_games():
    games = Game.objects.all()
    print("All games:\n")
    for game in games:
        print(f"{game.id}. Name: '{game.name}' Genre: '{game.genre}' Year: '{game.year}' Rate: '{game.rate}'")
        print("\n")


show_all_games()
```


