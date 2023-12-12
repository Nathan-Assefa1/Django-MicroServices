from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.generic import TemplateView
import pandas as pd
import io
from django.shortcuts import render
from fpdf import FPDF
from django.http import HttpResponse
from django.core.mail import EmailMessage

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class DatabaseViewSet(viewsets.ModelViewSet):
    serializer_class = DatabaseSerializer
    queryset = Database.objects.all()
    
class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'

    def post(self, request):
        context = {
            'messages':[]
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )

        for record in csv_data.to_dict(orient="records"):
            try:
                Database.objects.create(
                    user_email = record['user_email'],
                    date_of_transaction = record['date_of_transaction'],
                    amount = record['amount']
                )
            except Exception as e:
                context['exceptions_raised'] = e
                
        return render(request, self.template_name, context)
    
class CsvUploader2(TemplateView):
    template_name = 'csv_uploader.html'


    def post(self, request):
        context = {
            'messages':[]
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        keys = []
        values = []
        for record in csv_data.to_dict(orient="records"):  
            try:
              for key, value in record.items():
                   keys.append(key) 
                   values.append(record[key]) 
            except Exception as e:
                context['exceptions_raised'] = e
                
        for i in range(len(values)):     
            pdf.cell(0, 60, keys[i] + ": " + str(values[i]))
            pdf.ln(15)
            
        pdf.output('tuto1.pdf', 'F')
        return render(request, self.template_name, context)


    

class CsvUploader3(TemplateView):
    template_name = 'email_generator.html'

    def post(self, request):
        context = {
            'messages':[]
        }

        pdf = request.FILES['csv']
        user_email = request.POST['email']
        email = EmailMessage(
        'Transactions',
        'This Is Your Attached Transactions PDF',
        'django@mailtrap.club',
        [user_email]
        )

        with open(pdf.name, "rb") as file:
            email.attach(pdf.name, file.read(), 'application/pdf')
    
        email.send()
        return HttpResponse('Message sent!')