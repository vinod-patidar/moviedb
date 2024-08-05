from django.db import models

class Person(models.Model):
  nconst = models.CharField(max_length=20, unique=True)
  full_name = models.CharField(max_length=100, null=True)
  birthYear = models.CharField(max_length=20, null=True, blank=True)
  deathYear = models.CharField(max_length=20, null=True, blank=True)
  profession = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return f"{self.full_name}"


class Movie(models.Model):
  nconst = models.CharField(max_length=20, unique=True)
  title = models.CharField(max_length=200, null=True)
  orig_title = models.CharField(max_length=200, null=True, blank=True)
  type = models.CharField(max_length=100, null=True, blank=True)
  is_adult = models.BooleanField(default=False)
  startYear = models.CharField(max_length=20, null=True, blank=True)
  endYear = models.CharField(max_length=50, null=True, blank=True)
  runtimeMinutes = models.CharField(max_length=20, null=True, blank=True)
  genres = models.CharField(max_length=200, null=True, blank=True)
  persons = models.ManyToManyField(Person, through='MoviePerson')

  def __str__(self):
    return self.title


class MoviePerson(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  person = models.ForeignKey(Person, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('movie', 'person')

  def __str__(self):
    return f"{self.person} in {self.movie}"
