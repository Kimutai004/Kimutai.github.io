from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send an email
        send_mail(
            f'Message from {name}',
            f'You have received a new message from {name} ({email}):\n\n{message}',
            'your_email@example.com',
            ['your_email@example.com'],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Message sent successfully!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def index(request):
    return render(request, 'portfolio/index.html')  # Correct template path