
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_records/', views.add_records, name='add_records'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

    #path('url at which site will be loaded' , view.function in view, name=)
]
