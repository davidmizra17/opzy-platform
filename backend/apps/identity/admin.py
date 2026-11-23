from django.contrib import admin

from .models import Contact, Organization, Session, Visitor

admin.site.register(Organization)
admin.site.register(Contact)
admin.site.register(Visitor)
admin.site.register(Session)
