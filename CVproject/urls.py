from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь к админке Django
    path('', include('cvapp.urls')),  # Путь для главной страницы из cvapp
    path('salary/', include('SalaryPredictionApp.urls')),  # Путь для SalaryPredictionApp
    path('accounts/', include('accounts.urls')),  # Путь для страниц аккаунтов пользователей
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
