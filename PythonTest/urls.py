from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("apps.users.api.urls")),
    path('company/', include("apps.company.api.urls")),
    path('cage/', include("apps.cages.api.urls")),
    path('animal/', include("apps.animals.api.urls")),
    path('login/', include('apps.login_logout.urls')),
    path('report/', include('apps.reports.api.urls'))
]
