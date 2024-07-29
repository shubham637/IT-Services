from decimal import Decimal

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView

from application.custom_classes import AjayDatatableView
from apps.service.forms import ServiceForm
from apps.service.models import Service


# Create your views here.
def Test(request):
    return HttpResponse('Test-Service-app')


class ServiceTemplate(TemplateView):
    template_name = 'service/list.html'


class CreateService(CreateView, SuccessMessageMixin):
    model = Service
    form_class = ServiceForm
    template_name = 'service/form.html'
    success_url = reverse_lazy('service-template')
    success_message = 'Service Create Successfully'


class ServiceListViewJson(AjayDatatableView):
    model = Service
    columns = ['service_name', 'payment_terms', 'service_price', 'service_package', 'service_tax', 'service_image',
              'active', 'actions']
    extra_search_columns = 'actions'

    def get_initial_queryset(self):
        return self.model.objects.filter(active=True)

    def render_column(self, row, column):
        if column=='service_image':
            return f'<img src="{row.service_image.url}" height=50px alt="Image Invalid">'

        if column=='active':
            if row.active:
                return '<span class="badge badge-success">Active</span>'

        if column == 'actions':
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('service-update', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('service-delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
        else:
            return super(ServiceListViewJson, self).render_column(row, column)


class ServiceUpdateView(UpdateView, SuccessMessageMixin):
    model = Service
    form_class = ServiceForm
    template_name = 'service/form.html'
    success_url = reverse_lazy('service-template')
    success_message = 'Service Update Successfully'


class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('service-template')