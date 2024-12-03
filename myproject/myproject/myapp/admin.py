from django.contrib import admin

# Register your models here.
from .models import Team, Person, Osoba, Stanowisko

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Stanowisko)
class OsobaAdmin (admin.ModelAdmin):
    list_display = ["imie", "nazwisko", "plec", "stanowisko", "data_dodania"]
admin.site.register(Osoba, OsobaAdmin)