from django.urls import path
from . import views

app_name = 'sqlapp'

urlpatterns = [
    path('disease_type/', views.disease_type, name='disease_type'),
    path('create_disease_type/', views.create_disease_type, name='create_disease_type'),
    path('edit_disease_type/<int:id>/', views.edit_disease_type, name='edit_disease_type'),
    path('delete_disease_type/<int:id>/', views.delete_disease_type, name='delete_disease_type'),

    path('country/', views.country, name='country'),
    path('disease/', views.disease, name='disease'),
    path('discover/', views.discover, name='discover'),
    path('users/', views.users, name='users'),
    path('public_servant/', views.public_servant, name='public_servant'),
    path('doctor/', views.doctor, name='doctor'),
    path('specialize/', views.specialize, name='specialize'),
    path('record/', views.record, name='record')



]