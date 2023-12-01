from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CodeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views import View
from .models import Code


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = "/login/"


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = "/verify/"


class CodeVerificationView(View):
    template_name = "verify.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = CodeForm(request.POST)

        if form.is_valid():
            entered_code = form.cleaned_data["code"]
            user = request.user
            print(entered_code)

            # Retrieve the Code instance associated with the user
            code_instance = Code.objects.get(user=user)
            print(code_instance)

            if entered_code == code_instance.code:
                # Code is correct, log in the user
                user = authenticate(
                    request, username=user.username, password=user.password
                )
                login(request, user)

                messages.success(
                    request, "Verification successful. You are now logged in."
                )
                return redirect(
                    "/"
                )  
            else:
                # Incorrect code
                messages.error(request, "Incorrect verification code.")

        return render(request, self.template_name, {"form": form})
