from django.shortcuts import render

def confirm_email_view(request):
    return render(request, 'protect/confirm_email.html')