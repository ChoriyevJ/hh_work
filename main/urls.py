from django.urls import path

from main import views


urlpatterns = [
    # paths for main page
    # path('tags/', views.TagListAPIView.as_view()),
    path('industry/', views.IndustryListAPIView.as_view()),
    path('futured/', views.FuturedInTashkentVacancyListAPIView.as_view()),
    path('specs/', views.SpecializationListAPIView.as_view()),

    path('vacancy/', views.VacancyListAPIView.as_view())
    # path('vacancy/<int:pk>/', views.VacancyDetailAPIView.as_view())

]

