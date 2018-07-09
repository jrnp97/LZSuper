from __future__ import absolute_import

from django.core.mail import EmailMessage
from celery import current_app
import os
from django.contrib.auth.models import User
import xlsxwriter

app = current_app


@app.task
def crear_archivo_xls():
    user = User.objects.filter(is_active=1)

    workbook = xlsxwriter.Workbook('media/usuario.xls', {'remove_timezone': True, 'default_date_format': 'dd/mm/yy'})
    worksheet = workbook.add_worksheet()

    header = ["id", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff",
              "is_active", "date_joined"]

    worksheet.write_row(0, 0, header)
    [worksheet.write_row(values + 1, 0, list(map(lambda x: user[values].__dict__[x], header))) for values in
     range(len(user))]
    workbook.close()

    return 'media/usuario.xls'


@app.task
def send_email():
    e = EmailMessage()
    e.subject = 'Reporte Usuarios'
    e.to = ['johnflorez_1289@hotmail.com', ]
    e.from_email = 'ivanspoof@gmail.com'
    e.body = 'Anexo reporte en archivo xls'
    #e.attach_file(ruta)
    e.send()

    return 'Mensaje Enviado'


# @app.task
# def borra_archivo(ruta):
#     os.remove(ruta)
#
#
# @app.task(bind=True)
# def reporte_usuario(self):
#     (crear_archivo_xls.s() | send_email.s() | borra_archivo.s())()


@app.task
def prueba():
    return 'Hola Mundo'