from django.db import models
from utils.models import BaseModel


class Team(BaseModel):
    team = models.CharField(max_length=128)


class Status(models.TextChoices):
    VICTORY = "Victory", "L"
    DEFEAT = "Defeat", "W"
    DOUBLE = "Double", "D"


class Game(BaseModel):
    teams = models.ManyToManyField(Team)
    guest_goal = models.IntegerField(default=0)
    team_goal = models.IntegerField(default=0)

    game_date = models.TimeField()
    goal_date = models.TimeField()

    matches_played = models.IntegerField(default=0)
    winds = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    status = models.CharField(max_length=128, choices=Status.choices)

