from django.contrib import admin
from .models import Post,PostSeries,PostCategory
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	fieldsets=[
		("Title/Date",{"fields":["post_title","post_published"]}),
		("URL",{"fields":["post_slug"]}),
		("Series",{"fields":["post_series"]}),
		("Content",{"fields":["post_text"]})
	]
	formfield_overrides={
		models.TextField:{'widget':TinyMCE()},
	}

admin.site.register(PostSeries)
admin.site.register(PostCategory)
admin.site.register(Post,PostAdmin)
