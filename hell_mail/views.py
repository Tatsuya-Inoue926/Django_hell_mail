from django.shortcuts import render, redirect
from .forms import HellmailForm
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect


def index(request):

    if request.method == "POST":
        form = HellmailForm(request.POST)

        if form.is_valid():
            Subject = "地獄通信"
            human = form.cleaned_data["subject"]
            message = "対象者は" +  human + "。\n\nこのメールに「はい」と返信すれば、私と正式に契約を交わしたことになる。怨みの相手は速やかに地獄へ流されるわ。\n\n\nただし、怨みを晴らしたら、あなた自身にも代償を支払ってもらう。\n\n\n「人を呪わば穴二つ」\n\n\n-----後はあなたが決める事よ。\n\n\n\n閻魔あい"
            sender = [ settings.EMAIL_HOST_USER ]
            recipients = []
            recipients.append(form.cleaned_data["sender"])
            try:
                send_mail(Subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect("hell_mail:complete")
    
    else:
        form = HellmailForm()

    return render(request, "hell_mail/index.html", {"form": form})

def complete(request):
    return render(request, "hell_mail/complete.html")