from django.urls import path
from . import views


app_name = "hell_mail"

urlpatterns = [
    path("", views.index, name ="index"),
    path("complete", views.complete, name ="complete"),
]

#path("hell_mail_form/complete/mail/", views.SendMail, name = "sendmail")