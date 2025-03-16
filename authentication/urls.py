from django.urls import path
from authentication.views import register_view, login_view, logout_view
from django.contrib.auth.views import LoginView

# ✅ Namespace for authentication
app_name = "authentication"

urlpatterns = [
    path("register/", register_view, name="register"),  
    path("login/", login_view, name="login"),  # ✅ Use your custom login view
    path("logout/", logout_view, name="logout"),  

    # ✅ Optional: Use Django's built-in login view if needed
    # path("login/", LoginView.as_view(template_name="authentication/login.html"), name="login"),
]
