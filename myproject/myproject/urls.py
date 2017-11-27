from django.conf.urls import url
from django.contrib import admin
from sanghyunfood import views as sf
urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^keyboard/', sf.keyboard),
        url(r'^message', sf.message),
]
