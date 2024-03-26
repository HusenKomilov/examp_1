from django.contrib import admin

from chats.models import Chat, Document, Gallery, Message, Profile


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ("pk", "user")


class DocumentAdmin(admin.TabularInline):
    fk_name = "message"
    model = Document
    extra = 1


class GalleryAdmin(admin.TabularInline):
    fk_name = "message"
    model = Gallery
    extra = 1


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("message",)
    model = Message
    inlines = [DocumentAdmin, GalleryAdmin]


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient")
