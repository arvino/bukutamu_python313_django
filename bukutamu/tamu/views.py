from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from .models import Member, BukuTamu
from .forms import MemberRegistrationForm, BukuTamuForm, MemberUpdateForm
import csv
import xlsxwriter
from io import BytesIO
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .utils import send_telegram_notification
from .notifications import send_welcome_email, send_entry_notification

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

def public_list(request):
    tamu_list = BukuTamu.objects.all()
    return render(request, 'tamu/public_list.html', {'tamu_list': tamu_list})

def register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Kirim email selamat datang
            send_welcome_email(user)
            messages.success(request, 'Registrasi berhasil! Silakan cek email Anda.')
            return redirect('login')
    else:
        form = MemberRegistrationForm()
    return render(request, 'tamu/register.html', {'form': form})

@login_required
def member_dashboard(request):
    user_entries = BukuTamu.objects.filter(member=request.user)
    can_submit = not BukuTamu.objects.filter(
        member=request.user,
        timestamp__date=timezone.now().date()
    ).exists()
    
    return render(request, 'tamu/member_dashboard.html', {
        'user_entries': user_entries,
        'can_submit': can_submit
    })

@login_required
def submit_entry(request):
    if request.method == 'POST':
        form = BukuTamuForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.member = request.user
            
            if entry.can_submit_today():
                entry.save()
                # Kirim notifikasi
                send_telegram_notification(f"""
<b>Pesan Buku Tamu Baru</b>
Dari: {entry.member.username}
Email: {entry.member.email}
Pesan: {entry.messages[:100]}...
""")
                send_entry_notification(entry)
                messages.success(request, 'Pesan berhasil ditambahkan!')
                return redirect('member_dashboard')
            else:
                messages.error(request, 'Anda sudah mengirim pesan hari ini.')
    else:
        form = BukuTamuForm()
    
    return render(request, 'tamu/submit_entry.html', {'form': form})

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(BukuTamu, id=entry_id)
    
    # Cek kepemilikan entry
    if entry.member != request.user and not request.user.role == 'admin':
        raise PermissionDenied
    
    if request.method == 'POST':
        form = BukuTamuForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pesan berhasil diperbarui!')
            return redirect('member_dashboard')
    else:
        form = BukuTamuForm(instance=entry)
    
    return render(request, 'tamu/edit_entry.html', {
        'form': form,
        'entry': entry
    })

@login_required
def profile(request):
    if request.method == 'POST':
        form = MemberUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil berhasil diperbarui!')
            return redirect('profile')
    else:
        form = MemberUpdateForm(instance=request.user)
    
    return render(request, 'tamu/profile.html', {'form': form})

@user_passes_test(is_admin)
def admin_dashboard(request):
    all_entries = BukuTamu.objects.all()
    all_members = Member.objects.filter(role='member')
    return render(request, 'tamu/admin_dashboard.html', {
        'entries': all_entries,
        'members': all_members
    })

@user_passes_test(is_admin)
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bukutamu.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Tanggal', 'Member', 'Email', 'Pesan'])
    
    entries = BukuTamu.objects.all().select_related('member')
    for entry in entries:
        writer.writerow([
            entry.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            entry.member.username,
            entry.member.email,
            entry.messages
        ])
    
    return response

@user_passes_test(is_admin)
def export_excel(request):
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    
    # Add header
    headers = ['Tanggal', 'Member', 'Email', 'Pesan']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)
    
    # Add data
    entries = BukuTamu.objects.all().select_related('member')
    for row, entry in enumerate(entries, 1):
        worksheet.write(row, 0, entry.timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        worksheet.write(row, 1, entry.member.username)
        worksheet.write(row, 2, entry.member.email)
        worksheet.write(row, 3, entry.messages)
    
    workbook.close()
    output.seek(0)
    
    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="bukutamu.xlsx"'
    return response

@user_passes_test(is_admin)
def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bukutamu.pdf"'
    
    # Create PDF
    p = canvas.Canvas(response, pagesize=letter)
    y = 750  # Starting y position
    
    # Add title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Laporan Buku Tamu")
    y -= 30
    
    # Add data
    p.setFont("Helvetica", 12)
    entries = BukuTamu.objects.all().select_related('member')
    for entry in entries:
        if y < 50:  # Check if we need a new page
            p.showPage()
            y = 750
        
        p.drawString(50, y, f"Tanggal: {entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        y -= 20
        p.drawString(50, y, f"Member: {entry.member.username}")
        y -= 20
        p.drawString(50, y, f"Email: {entry.member.email}")
        y -= 20
        p.drawString(50, y, f"Pesan: {entry.messages[:100]}...")
        y -= 40
    
    p.showPage()
    p.save()
    return response 