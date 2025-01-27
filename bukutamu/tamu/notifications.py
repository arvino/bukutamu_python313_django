from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email(user):
    """
    Kirim email selamat datang ke member baru
    """
    subject = 'Selamat Datang di Buku Tamu'
    html_message = render_to_string('emails/welcome.html', {
        'user': user,
    })
    
    send_mail(
        subject=subject,
        message='',
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )

def send_entry_notification(entry):
    """
    Kirim notifikasi email ke admin saat ada pesan baru
    """
    subject = 'Pesan Buku Tamu Baru'
    html_message = render_to_string('emails/new_entry.html', {
        'entry': entry,
    })
    
    # Kirim ke semua admin
    admin_emails = list(Member.objects.filter(role='admin').values_list('email', flat=True))
    
    send_mail(
        subject=subject,
        message='',
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=admin_emails,
        fail_silently=False,
    ) 