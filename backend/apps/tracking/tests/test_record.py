import uuid

import pytest

from apps.tracking import services


@pytest.mark.django_db
def test_record_is_idempotent():
    event_id, visitor_id = uuid.uuid4(), uuid.uuid4()
    services.record("page_view", event_id=event_id, visitor_id=visitor_id)
    services.record("page_view", event_id=event_id, visitor_id=visitor_id)
    from apps.tracking.models import Event

    assert Event.objects.count() == 1


def test_unknown_event_is_rejected():
    with pytest.raises(services.UnknownEvent):
        services.record("made_up_event", visitor_id=uuid.uuid4())
