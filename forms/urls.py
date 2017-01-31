from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.main_page),
    url(r'^forms_option/', views.forms_option),
    url(r'^fill_form/', views.fill_form),
    url(r'^show_all/', views.show_all),
]