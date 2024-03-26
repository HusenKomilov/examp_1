from rest_framework import serializers

from chats import models


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ("user", "avatar")


class ProfileListSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(default=0)

    class Meta:
        model = models.Profile
        fields = ("id", "user", "avatar", "count")


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = ("message", "image")


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Document
        fields = ("message", "document")


class MessageCreateSerializer(serializers.ModelSerializer):
    contact = ProfileSerializers(read_only=True)
    images = GallerySerializer(many=True, read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)
    upload_images = serializers.ListSerializer(
        child=serializers.FileField(max_length=128, allow_empty_file=False, use_url=False), write_only=True
    )
    upload_documents = serializers.ListSerializer(
        child=serializers.FileField(max_length=128, allow_empty_file=False, use_url=False), write_only=True
    )

    class Meta:
        model = models.Message
        fields = ("contact", "message", "voice", "location", "is_watched", "images", "documents")

    def create(self, validated_data):
        upload_images = validated_data.pop("upload_images")
        upload_documents = validated_data.pop("upload_documents")
        message = models.Message.objects.create(**validated_data)
        if upload_images:
            for image in upload_images:
                models.Gallery.objects.create(message=message, image=image)

        if upload_documents:
            for document in upload_documents:
                models.Document.objects.create(message=message, document=document)
        return message


class ChatSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(default=0)
    sender = serializers.StringRelatedField()

    message = MessageCreateSerializer()

    class Meta:
        model = models.Chat
        fields = ("id", "sender", "recipient", "message", "is_watched", "count", "created_ad")
