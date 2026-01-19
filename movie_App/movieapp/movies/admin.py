from django.contrib import admin

from movies.models import Contact, Genre, Movie, Person, Video
from movies.models import Comment

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'budget')
    list_display_links = ('id', 'title')
    prepopulated_fields={"slug":("title",)}
    list_filter=("genres","language")
    search_fields = ("title","description")
class PersonelAdmin(admin.ModelAdmin):
    list_display = ("id","full_name",  'duty_type',"gender",)
    list_display_links = ('id', "full_name")
    list_filter=("duty_type","gender")
class CommentAdmin(admin.ModelAdmin):
    list_display= ("full_name","movie",)
    list_filter = ("full_name","movie",)
    search_fields = ("movie__title","text")
    
    
admin.site.register(Movie, MoviesAdmin)
admin.site.register(Person, PersonelAdmin)
admin.site.register(Contact)
admin.site.register(Genre)
admin.site.register(Video)
admin.site.register(Comment,CommentAdmin)



