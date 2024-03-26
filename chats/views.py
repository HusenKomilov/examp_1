from django.core.cache import cache
from django.db.models import Count
from rest_framework import generics, response

from chats import models, serializers


class ChatListCreateView(generics.ListCreateAPIView):
    queryset = models.Chat.objects.all()
    serializer_class = serializers.ChatSerializer

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(sender_id=self.kwargs["sender_id"], recipient_id=self.kwargs["recipient_id"])
            .select_related("sender", "profile")
            .prefetch_related("message")
        )

    def list(self, request):
        cached_data = cache.get("chat_data")
        if cached_data:
            return response.Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set("chat_data", data, timeout=60)

        return response.Response(data)

    def create(self, request):
        cache.delete("chat_data")

        return super().create(request)

    def update(self, request, *args, **kwargs):
        cache.delete("chat_data")

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        cache.delete("chat_data")

        return super().destroy(request, *args, **kwargs)


class ProfileListAPIView(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializers

    def get_queryset(self):
        queryset = super().get_queryset().filter(user_id=self.kwargs["user_id"]).annotate(count=Count("chat"))
        return queryset
