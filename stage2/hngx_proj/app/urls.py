from django.urls import path
from . import views

urlpatterns = [ 
    # create 
    path('create_person/', views.create_person, name='add_person'),

    # read
    path('all_persons/', views.get_all_persons, name='get_all_persons'),
    path('get_person/<str:query>/', views.get_person_details, name='get_details'),

    # update
    path('update/', views.update_person, name='update_person'),

    # delete 
    path('delete/<str:query>/', views.delete_person, name='delete_person'),
]