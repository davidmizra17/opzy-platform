import uuid

import pytest

from apps.conversations import services


@pytest.mark.django_db
def test_daily_conversation_limit(settings):
    settings.MAX_CONVERSATIONS_PER_VISITOR_PER_DAY = 2
    visitor_id = uuid.uuid4()
    services.start_conversation(visitor_id=visitor_id)
    services.start_conversation(visitor_id=visitor_id)
    with pytest.raises(services.LimitReached):
        services.start_conversation(visitor_id=visitor_id)


@pytest.mark.django_db
def test_agent_turn_limit(settings):
    settings.MAX_AGENT_TURNS_PER_CONVERSATION = 1
    conversation = services.start_conversation(visitor_id=uuid.uuid4())
    services.add_agent_message(conversation, "Hola")
    conversation.refresh_from_db()
    with pytest.raises(services.LimitReached):
        services.add_agent_message(conversation, "Otra vez")
