from django.urls import path
from . import views


urlpatterns = [
    path('diary/', views.DiaryListView.as_view()),
    path('diary/add/', views.DiaryCreate.as_view()),
    path('diary/<int:pk>/update/', views.DiaryUpdate.as_view()),
    path('diary/<int:pk>/delete/', views.DiaryDelete.as_view()),  
    path('money', views.MoneyListView.as_view()),
    path('money/add/', views.MoneyCreate.as_view()),
    path('money/<int:pk>/update/', views.MoneyUpdate.as_view()),
    path('money/<int:pk>/delete/', views.MoneyDelete.as_view()),  
]