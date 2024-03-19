from django.contrib.auth.models import AbstractUser, UserManager as BaseManager
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from utils.models import BaseModel


class UserManager(BaseManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    unique_field = models.CharField(max_length=256, unique=True)

    is_delete = models.BooleanField(default=False)

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def delete(self):
        self.is_delete = True
        self.is_active = False
        self.save()

    def login(self):
        if self.is_delete:
            pass
        else:
            raise "Siz akkaund yaratishingiz kerak"

    @classmethod
    def register(self):
        self.save()


class Worker(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="worker")

    def __str__(self):
        return self.user.username


class Employer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
