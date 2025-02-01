from django.contrib import admin
from .models import Team, Person,  Osoba, Stanowisko




admin.site.register(Team)


class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    list_filter = ['nazwa']

class PersonAdmin(admin.ModelAdmin):
    @admin.display(description = "shirt size (id)")
    def team_with_id(self,obj):
        if obj.team :
            return f'{obj.team} ({obj.team.id})'
        return 'No team'

    list_display = ["name", "nickname", "shirt_size", "month_added", "team_with_id"]
    list_filter = ['team']

admin.site.register(Person, PersonAdmin)

class OsobaAdmin(admin.ModelAdmin):

    @admin.display(description="Stanowisko (ID)")
    def stanowisko_with_id(self, obj):
        if obj.stanowisko:
            return f'{obj.stanowisko} ({obj.stanowisko.id})'
        return "Brak stanowiska"

    list_display = ["imie", "nazwisko", "plec", "stanowisko_with_id", "data_dodania"]
    list_filter = ['stanowisko', 'data_dodania']

admin.site.register(Osoba, OsobaAdmin)
