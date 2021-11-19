from django.shortcuts import render,redirect,get_object_or_404
from loc_criminal.models import Criminal
from django.views.generic import (ListView,
                                 )


#def map(request):
#     return render(request,'loc_criminal/criminal_list.html')


class CriminalListView(ListView):
    model = Criminal
    template_name='loc_criminal/criminal_list.html'

    def get_queryset(self):
        return Criminal.objects.all()
