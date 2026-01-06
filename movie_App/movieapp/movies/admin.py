from django.contrib import admin

from movies.models import Contact, Genre, Movie, Person, Video

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

admin.site.register(Movie, MoviesAdmin)

admin.site.register(Person, PersonelAdmin)
admin.site.register(Contact)
admin.site.register(Genre)
admin.site.register(Video)



