from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from complaints.models import Complaint


@login_required
def staff_dashboard(request):
    complaints = Complaint.objects.filter(
        assigned_staff=request.user
    )
    return render(request, 'staff/staff_dashboard.html', {
        'complaints': complaints
    })



@login_required
def update_status(request, cid):
    complaint = Complaint.objects.get(id=cid)

    if request.method == 'POST':
        complaint.status = request.POST['status']
        complaint.save()
        return redirect('staff_dashboard')

    return render(request, 'staff/update_status.html', {
        'complaint': complaint
    })
