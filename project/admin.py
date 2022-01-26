from django.contrib import admin
from .models import Message, Profile, Project, Review, Skill, Tag
# Register your models here.
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Skill)
admin.site.register(Profile)


