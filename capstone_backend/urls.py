"""capstone_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from things.views import ThingViews, BlacklistTokenView, CollectionViews, ContainerViews, PlaceViews, UserViews, GroupViews, UserCreate, ThingListDetailFilter
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView)

router = DefaultRouter()
router.register(r'things', ThingViews, basename='thing')
router.register(r'collections', CollectionViews)
router.register(r'containers', ContainerViews)
router.register(r'places', PlaceViews)
router.register(r'users', UserViews)
router.register(r'groups', GroupViews)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/register/', UserCreate.as_view(), name='create_user'),
    path('api/search/', ThingListDetailFilter.as_view(), name='thingsearch'),
    path('api/user/logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist'),
    path('', include(router.urls)),
    # path('thing/create/', CreateThing.as_view(), name='creatething'),
    # path('thing/edit/thingdetail/<int:pk>/', EditThingDetail.as_view(), name='thingdetail'),
    # path('thing/edit/<int:pk>/', EditThing.as_view(), name='editthing'),
    # path('thing/delete/<int:pk>/', DeleteThing.as_view(), name='deletething')
]
