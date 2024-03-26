from django.urls import path

from chats import views

urlpatterns = [
    path("chats/<int:sender_id>/<int:recipient_id>/", views.ChatListCreateView.as_view()),
    path("chats/<int:user_id>", views.ProfileListAPIView.as_view()),
]
