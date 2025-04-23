from django.urls import path, include  # Добавляем include для вложенных маршрутов
from . import views  # Импортируем views.py из cvapp

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('select-template/', views.SelectTemplate.as_view(), name="select_template"),  # Страница для выбора шаблона
    path('resumeTemplate/', views.Accept.as_view(), name='accept'),  # Шаблон для резюме
    path('list/', views.list, name="list"),  # Список резюме
    path('list/<int:id>/', views.UserDetail, name="viewing"),  # Просмотр конкретного резюме по ID
    path('resume/<int:template_id>/', views.resume, name="resume"),  # Резюме по шаблону
    path('update/<int:id>/', views.update_form, name="update"),  # Форма для обновления
    path('delete/<int:id>/', views.delete_form, name="deleteform"),  # Удаление резюме по ID
    path('prediction/', include('SalaryPredictionApp.urls')),  # Включаем URL для предсказания зарплаты
]
