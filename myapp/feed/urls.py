from django.urls import path, include
from . import views
from users import views as user_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserListView )
router.register('profiles', views.ProfileView )

urlpatterns = [
    # path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('', include(router.urls)),

    # path('', user_views.UserListView)
]
