
from django.conf.urls import url
from django.contrib import admin
from olivia.views import HomeView

from django.conf.urls.static import static
from django.conf import settings

from views import NewContact

urlpatterns = [
    url(r'^contact/$', NewContact.as_view(),name='new_cntct'),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'OLIVIAHOLIDAY ADMIN DASHBOARD'
