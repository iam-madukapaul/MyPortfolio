from django.shortcuts import render, redirect
from app.models import AboutMe, Skill, TechTools, Project, MyInfo
from app.forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('client_email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            html = render_to_string('app/contactmessage.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })
            send_mail('Contact Us', html, settings.DEFAULT_FROM_EMAIL, ['john@gmail.com'], fail_silently=False, html_message=html)
            messages.success(request, "Your message has been sent. Thank you!")
            return redirect('index')
        else:
            messages.warning(request, "Something went wrong, please try again.")

    about_me = AboutMe.objects.all()
    skills = Skill.objects.all()
    tech_tools = TechTools.objects.all()
    projects = Project.objects.all()
    my_info = MyInfo.objects.all()
    context = {
        'about_me': about_me,
        'skills': skills,
        'tech_tools': tech_tools,
        'projects': projects,
        'my_info': my_info,
        'form': form,
        }
    return render(request, 'app/index.html', context)

