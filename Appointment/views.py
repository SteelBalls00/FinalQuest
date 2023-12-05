from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import EmailMultiAlternatives, mail_admins
from datetime import datetime

from django.template.loader import render_to_string
from .models import Appointment

# Рассылка новостей админам
class AppointmentView(View):
    template_name = 'make_appointment.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'appointment/make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        mail_admins(
            subject=f'{appointment.client_name} {appointment.date.strftime("%d %m %Y")}',
            message=appointment.message,
        )

        return redirect('appointment:make_appointment')


        # html_content = render_to_string(
        #     'appointment/appointment_created.html', {'appointment': appointment, }
        # )
        #
        # msg = EmailMultiAlternatives(
        #     subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
        #     body=appointment.message,  # это то же, что и message
        #     from_email='steelballs00@yandex.ru',
        #     to=['predator7151753@mail.ru'],  # это то же, что и recipients_list
        # )
        # msg.attach_alternative(html_content, "text/html")  # добавляем html
        # msg.send()  # отсылаем
        #
        # return redirect('appointment:make_appointment')