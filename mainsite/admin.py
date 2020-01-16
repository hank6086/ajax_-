from django.contrib import admin
from .models import testPost,post2,id_ap,megall
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_data')
class Post2Admin(admin.ModelAdmin):
    list_display = ('stname','number','time')
class idAdmin(admin.ModelAdmin):
    list_display=('idname','uid',)
class megAdmin(admin.ModelAdmin):
    list_display=('meg_text','user_uid')

admin.site.register(testPost,PostAdmin)
admin.site.register(post2,Post2Admin)
admin.site.register(id_ap,idAdmin)
admin.site.register(megall,megAdmin)

