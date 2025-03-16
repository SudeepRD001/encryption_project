from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.encrypt_view, name='home'),  # ✅ Homepage (Default to Encryption)
    path('encrypt/', views.encrypt_view, name='encrypt'),
    path('decrypt/', views.decrypt_view, name='decrypt'),
    path('result/<int:message_id>/', views.result_view, name='result'),  # ✅ Fixed: Now supports message_id
]
