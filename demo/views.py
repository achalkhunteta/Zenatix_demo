from django.views.generic import TemplateView, CreateView
from models import Station
import ujson as json
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import FormMixin
from forms import StationForm

class InitChart(TemplateView):
    '''
    Class Based View to Initialize the Chart Creation Page
    '''

    template_name = 'create_chart.html'

    def get_context_data(self, **kwargs):
        '''
        Overriding the get_context_data method to add
        some more data in contet variable
        '''

        context = super(InitChart, self).get_context_data(**kwargs)

        # Get info of all the available stations
        stations_info = Station.objects.all()
        context['stations'] = stations_info

        return context


class AddStation(CreateView):
    '''
    Class Based View to add a New City/Station
    '''
    template_name = 'add_station.html'
    model= Station
    form_class = StationForm
    success_url =  reverse_lazy('create_chart')
