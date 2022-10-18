from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Domain

# Create your views here.
def index(request):
    domains = Domain.objects.all()
    resp_ctx = ''
    for domain in domains:
        resp_ctx += '# {}\n{} {}\n'.format(domain.desc, domain.ipaddr, domain.domain)
    return HttpResponse(resp_ctx)