from django.utils import timezone
from django.contrib import messages

class DailyPostLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.method == 'POST':
            if 'submit_entry' in request.path:
                from .models import BukuTamu
                today = timezone.now().date()
                if BukuTamu.objects.filter(
                    member=request.user,
                    timestamp__date=today
                ).exists():
                    messages.error(request, 'Anda sudah mengirim pesan hari ini.')
                    return redirect('member_dashboard')

        response = self.get_response(request)
        return response 