from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup', views.usersignup, name="signup"),
    url(r'^login', views.userlogin, name="login"),
    url(r'^logout', views.userlogout, name="logout"),
    url(r'^create', views.create_bean, name="create" ),
    url(r'^list', views.coffee_list, name="list" ),
    url(r'^update', views.update_bean, name="update" ),
]
