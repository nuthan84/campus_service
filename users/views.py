from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from complaints.models import Complaint
from django.db.models import Count


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        Profile.objects.create(
            user=user,
            role=role
        )

        return redirect('login')

    return render(request, 'users/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        selected_role = request.POST['role']

        user = authenticate(username=username, password=password)

        if user:
            # ADMIN (superuser)
            if user.is_superuser and selected_role == 'ADMIN':
                login(request, user)
                return redirect('admin_dashboard')

            # STUDENT / STAFF
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                return render(request, 'users/login.html', {
                    'error': 'Profile not found'
                })

            if profile.role != selected_role:
                return render(request, 'users/login.html', {
                    'error': 'Selected role does not match your account'
                })

            login(request, user)

            if profile.role == 'STUDENT':
                return redirect('dashboard')

            elif profile.role == 'STAFF':
                return redirect('staff_dashboard')

        return render(request, 'users/login.html', {
            'error': 'Invalid credentials'
        })

    return render(request, 'users/login.html')


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('login')

    staff_users = Profile.objects.filter(role='STAFF')

    staff_stats = []
    for staff in staff_users:
        pending = Complaint.objects.filter(
            assigned_staff=staff.user, status='PENDING'
        ).count()
        staff_stats.append({
            'staff': staff.user.username,
            'pending': pending
        })

    total_pending = Complaint.objects.filter(status='PENDING').count()
    total_resolved = Complaint.objects.filter(status='RESOLVED').count()

    return render(request, 'users/admin_dashboard.html', {
        'staff_stats': staff_stats,
        'total_pending': total_pending,
        'total_resolved': total_resolved,
    })
