from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict

from .models import Person


# Create your views here.
def xss_t(request):
    response = HttpResponseRedirect("http://192.168.3.20:8080/#/homePage")
    response.set_cookie("tokenZhunru", "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2OTk0NzE5LCJqdGkiOiIzYjhlODM4NmVkMDk0M2NhOWI3NTJlOGNlMmYzNzkyNSIsInVzZXJfaWQiOjh9.OsDQsPKjacy360i7sbfbR4XWpsaG-5RRZQVMzIka0u0")
    return response


def csrf_t(request):
    return render(request, "security_t/csrf_t.html")


def cors_t(request):
    return HttpResponse("success")


def sqlinject_t(request):
    pk = request.GET.get('pk')
    # 原生sql，存在注入风险 zhangsan' or '1  =》 select * from test where name='zhangsan' or '1'
    # qs = Person.objects.raw("select * from test where name='%s'" % pk)
    # django orm 不存在注入问题 zhangsan' or '1  =》 SELECT * FROM `test` WHERE `test`.`name` = zhangsan' or '1
    qs = Person.objects.filter(name=pk)
    print(qs.query)
    res = [model_to_dict(i) for i in qs]
    return HttpResponse(res)
