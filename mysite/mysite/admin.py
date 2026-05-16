from django.contrib import admin
from polls.models import Question, Choice



class CustomAdminSite(admin.AdminSite):
    site_header = "Curso de Python admin"
    site_title = "Curso de Python"
    index_title = "Bem-vindo ao painel"


admin_site = CustomAdminSite(name="custom_admin")

admin_site.register(Question)
admin_site.register(Choice)