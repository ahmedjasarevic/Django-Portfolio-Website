from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial, TutorialSeries, TutorialCategory, TutorialImage
# Register your models here.




class TutorialImageAdmin(admin.StackedInline):
    model = TutorialImage

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["tutorial_content"]}),
        ("Image", {"fields": ["tutorial_image"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
    inlines = [TutorialImageAdmin]

    class Meta:
       model = Tutorial

@admin.register(TutorialImage)
class TutorialImageAdmin(admin.ModelAdmin):
    pass


