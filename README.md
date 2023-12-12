# Django MicroServices
A Basic API application that provides four independent services:
1. A basic API that accepts a period of time (two dates) and the user's email address ID.
2. A database service that collects the CSV files with relevant transactions
3. A PDF generation service that takes in the above data and generates a PDF of the transaction list
4. An email service that sends the above PDF to the user's email address as an attachment

# What I Learned
- Using Django's HTML Templates to request files
- Requesting and Parsing CSV Files
- Converting CSV Data into a PDF File using PYFPDF
- Using Email Hosting to send PDF files to a given email address
- Practiced using function-based and class-based Django views
