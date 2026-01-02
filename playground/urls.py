import debug_toolbar
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.say_hello), # IMP In storefront/urls.py, we included playground app URLs 
                                    # so this URL will be accessible at /playground/home/
    # say_hello is reference not function call (no parentheses) we crealy see it
# path()
path('__debug__/', include(debug_toolbar.urls)),  # debug toolbar URLs
] 