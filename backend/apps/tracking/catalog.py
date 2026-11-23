"""Catálogo de eventos aceptados. Un nombre que no esté aquí se rechaza."""

EVENT_NAMES = frozenset(
    {
        # Landing
        "page_view", "cta_clicked", "section_viewed", "scroll_depth", "language_switched",
        # Widget
        "widget_opened", "widget_closed", "starter_prompt_selected", "message_sent",
        "voice_note_sent", "file_attached", "quick_reply_selected", "human_requested",
        # Triage
        "summary_shown", "summary_confirmed", "summary_corrected", "route_assigned",
        "escalated_to_ops",
        # Páginas
        "page_created", "page_updated", "page_reverted", "preview_viewed", "page_approved",
        "page_published",
        # Comercial
        "offer_presented", "contact_captured", "checkout_started", "payment_succeeded",
        "payment_failed",
    }
)
