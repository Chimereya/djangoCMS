from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class PreventLoginSignupMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect the authenticated user to home page
            return redirect(reverse_lazy('main:posts'))

        return super().dispatch(request, *args, **kwargs)


