from django.shortcuts import render, redirect
from notifications.models import Notification

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Fetch user notifications (latest 10)
    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')[:10]

    return render(request, 'notifications/notificate.html', {'notifications': notifications})