# from django.urls import include, path
# from rest_framework import routers
# from feed import views
# from django.contrib import admin

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from feed.views import WorkViewSet, HolderViewSet
from rest_framework import routers
from feed import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'works', views.WorkViewSet)
router.register(r'holders', views.HolderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('works/', WorkViewSet.as_view({'get': 'list'})),
    path('holders/', HolderViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('', include(routers.urls)),
]