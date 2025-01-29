from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from .models import Member, BukuTamu
from .forms import MemberRegistrationForm, BukuTamuForm, MemberUpdateForm

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

def public_list(request):
    tamu_list = BukuTamu.objects.all()
    return render(request, 'tamu/public_list.html', {'tamu_list': tamu_list})

def register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrasi berhasil! Silakan login.')
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
