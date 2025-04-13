from django.contrib import admin
from app.models import AboutMe, Skill, TechTools, Project, Contact, MyInfo

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(TechTools)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(MyInfo)
