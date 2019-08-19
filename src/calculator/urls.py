from django.conf.urls import url
from django.contrib import admin

from calcu.views import CalcuView, get_data

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', CalcuView.as_view()),
    url(r'^api/data/$', get_data, name='api-data'),
]
