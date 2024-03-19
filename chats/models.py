from django.contrib.auth import get_user_model
from django.db import models
from users.models import User
from utils.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)

    def __str__(self):
        return self.user.username


class Message(BaseModel):
    contact = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="author")

    message = models.TextField(blank=True, null=True)
    voice = models.FileField(verbose_name='voice/', blank=True, null=True)
    location = models.CharField(blank=True, null=True)

    is_watched = models.BooleanField(default=False)

    def __str__(self):
        return self.contact.user.username


class Gallery(BaseModel):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="message/", blank=True, null=True)


class Document(BaseModel):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="document")
    document = models.FileField(upload_to="document/", blank=True, null=True)


class Chat(BaseModel):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipient")

    message = models.ManyToManyField(Message, blank=True)

    is_watched = models.BooleanField(default=False)


class Archive(BaseModel):
    contact = models.ForeignKey(Profile, on_delete=models.CASCADE)
