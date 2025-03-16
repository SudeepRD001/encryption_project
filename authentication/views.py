from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

User = get_user_model()  # ✅ Use get_user_model() for better compatibility

# ✅ Register User
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"].strip()
        email = request.POST["email"].strip()
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # ✅ Check for empty fields
        if not username or not email or not password:
            messages.error(request, "All fields are required!")
            return redirect("authentication:register")

        # ✅ Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("authentication:register")

        # ✅ Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return redirect("authentication:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists!")
            return redirect("authentication:register")

        # ✅ Create and save user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("authentication:login")

    return render(request, "authentication/register.html")

# ✅ Login User
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"]

        # ✅ Check if fields are empty
        if not username or not password:
            messages.error(request, "Both fields are required!")
            return redirect("authentication:login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("encrypt")  # Redirect to the encryption page
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, "authentication/login.html")

# ✅ Logout User
def logout_view(request):
    if request.method == "POST" or request.method == "GET":  # ✅ Accept both GET & POST
        logout(request)
        messages.success(request, "You have logged out successfully!")
        return redirect("authentication:login")
    
    return redirect("authentication:login")  # Fallback redirect