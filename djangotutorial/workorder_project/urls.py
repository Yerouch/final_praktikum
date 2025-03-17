from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("workorder_project/", include("workorder_project.urls")),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]