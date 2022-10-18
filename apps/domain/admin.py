from django.contrib import admin
from django import forms

from .models import Domain


class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ('__all__')
        labels = {
            'domain': 'Domain',
            'ipaddr': 'Ip address',
            'desc': 'Description'
        }
        help_texts = {
            'domain': 'Domain, example: test.example.com',
            'ipaddr': 'Ip address, example: 66.66.66.66',
            'desc': 'Description, example: test domain'
        }


@admin.action(description='Modify ip address')
def modify_ipaddr(modeladmin, request, queryset):
    print(modeladmin, request, queryset)


class DomainAdmin(admin.ModelAdmin):
    list_display = ['domain', 'ipaddr', 'desc']
    search_fields = ['domain', 'ipaddr','desc']
    list_editable = ['ipaddr', 'desc']
    list_per_page = 10
    form = DomainForm
    actions = ['modify_ipaddr']


# Register your models here.
admin.site.register(Domain, DomainAdmin)