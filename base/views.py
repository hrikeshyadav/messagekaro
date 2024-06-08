from django.http import HttpResponse
from django.shortcuts import redirect, render
from base.models import Message

# Create your views here.

def check(request):
    return HttpResponse('hello')


def message(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        un = request.POST['un']
        ne = request.POST['uemail']
        nm = request.POST['umob']
        m = request.POST['msg']
        ms = Message.objects.create(name=un, email=ne, mob=nm, msg=m )
        ms.save()

        return redirect('/showmsg')


def showmsg(request):
    m = Message.objects.all()
    context={'data':m}
    return render(request,'showmessage.html',context )

def delete(request,did):
    m = Message.objects.filter(id = did)
    m.delete()
    return redirect('/showmsg')  ## redirect is used to go one url to another url
def edit(request, eid):
    # print(eid)
    # return HttpResponse('this is edit function '+ eid)
   if request.method == 'GET':
        m = Message.objects.filter(id = eid)
        context ={}
        context['data'] = m
        return render(request,'edit.html',context)
   else:
        un = request.POST['uname']
        ue = request.POST['email']
        um = request.POST['mob']
        umsg = request.POST['msg']
        # print(un)
        # print(ue)
        # print(um)
        # print(umsg)
        m = Message.objects.filter(id = eid)
        m.update(name = un, email=ue, mob=um, msg=umsg)
        return redirect( '/showmsg')

    