from django.urls import path

from .views import MessageView, StartConversationView

urlpatterns = [
    path("conversations", StartConversationView.as_view(), name="conversation-start"),
    path(
        "conversations/<uuid:conversation_id>/messages",
        MessageView.as_view(),
        name="conversation-messages",
    ),
]
