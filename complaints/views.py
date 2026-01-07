from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User
from .models import Complaint


@login_required
def add_complaint(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        # Auto-assign least busy staff
        staff_user = User.objects.filter(
            profile__role='STAFF'
        ).annotate(
            work_count=Count('assigned_complaints')
        ).order_by('work_count').first()

        Complaint.objects.create(
            title=title,
            description=description,
            user=request.user,
            assigned_staff=staff_user
        )

        return render(request, 'complaints/success.html')

    return render(request, 'complaints/add_complaint.html')


@login_required
def my_complaints(request):
    complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'complaints/my_complaints.html', {'complaints': complaints})
