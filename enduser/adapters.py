from .forms import CustomUserCreationForm, CustomLoginForm
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_form_class(self, request):
        return CustomUserCreationForm

    # def get_login_form(self, request=None):
    #     return CustomLoginForm