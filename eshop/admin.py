from django.contrib import admin

# Register your models here.
from eshop.models import *

admin.site.register(Adresa)
admin.site.register(Vyrobce)
admin.site.register(Komponenty)
admin.site.register(Pracovnik)
admin.site.register(Zakaznik)
admin.site.register(Sestava)
admin.site.register(Faktura)
admin.site.register(Attachment)