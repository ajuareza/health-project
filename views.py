from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
import matplotlib.pyplot as plt, numpy as np

def index(request):
    return HttpResponse("Que pasó, parcerooooos")

def get_reader(request): # note: no other params.

  # state = request.GET.get('state', '')  # if we knew the parameters ...
  d = dict(request.GET._iterlists())
  return HttpResponse(str(d))

from django.views.generic import FormView
from .forms import InputForm
from .models import DISEASES_DICT

def form(request):
    disease = request.GET.get('disease', '')
    if not disease: disease = request.POST.get('disease', '')

    params = {'form_action' : reverse_lazy('myapp:form'),
              'form_method' : 'get',
              'form' : InputForm({'disease' : disease}),
              'disease' : disease}

    return render(request, 'webhealth.html', params)

def other(request):
    disease = request.GET.get('disease', '')
    if not disease: disease = request.POST.get('disease', '')

    params = {'form_action' : reverse_lazy('myapp:form'),
              'form_method' : 'get',
              'form' : InputForm({'disease' : disease}),
              'disease' : disease}

    return render(request, 'other.html', params)

def measurements(request):
    disease = request.GET.get('disease', '')
    if not disease: disease = request.POST.get('disease', '')

    params = {'form_action' : reverse_lazy('myapp:form'),
              'form_method' : 'get',
              'form' : InputForm({'disease' : disease}),
              'disease' : disease}

    return render(request, 'measurements.html', params)

from django.views.generic import FormView
class FormClass(FormView):

    template_name = 'webhealth.html'
    form_class = InputForm

def get(self, request):
  disease = request.GET.get('disease', '')
  return render(request, self.webhealth, {'form_action' : reverse_lazy('myapp:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'disease' : disease}),
                                                  'disease' : DISEASES_DICT[disease]})
def post(self, request):
  disease = request.POST.get('disease', '')
  return render(request, self.webhealth, {'form_action' : reverse_lazy('myapp:formclass'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'disease' : disease}),
                                                  'disease' : DISEASES_DICT[disease]})
from os.path import join
from django.conf import settings

def table(request):

    df = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    return HttpResponse(table)

#def display_pic(request):
    #return render(request, 'view_pic.html', {"title" : "Arsenic in Bangladesh",
                                             #"pic_source" : reverse_lazy("myapp:pic")})

def display_pic(request, c = 'r'):

    county = request.GET.get('disease', 'Tuberculosis')

    params = {'title' : disease,
              'form_action' : reverse_lazy('myapp:display_pic'),
              'form_method' : 'get',
              'form' : InputForm({'disease' : disease}),
              'pic_source' : reverse_lazy("myapp:plot", kwargs = {'c' : disease})}

from .forms import InputForm
def display_table(request):
    disease = request.GET.get('disease', 'Tuberculosis')
    filename = join(settings.STATIC_ROOT, 'myapp/data.csv')
    df = pd.read_csv(filename)
    df = df[df["Cause"] == disease]
    if not df.size: return HttpResponse("Choose another disease")

    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {'title' : disease,
              'form_action' : reverse_lazy('myapp:display_pic'),
              'form_method' : 'get',
              'form' : InputForm({'disease' : disease}),
              'html_table' : table,
              'pic_source' : reverse_lazy("myapp:plot", kwargs = {'c' : disease})
              }
    return render(request, 'view_table.html', params)

def csv(request, year = None):
   filename = join(settings.STATIC_ROOT, 'myapp/data.csv')
   df = pd.read_csv(filename)
   table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
   table = table.replace('border="1"','border="0"')
   table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

   return HttpResponse(table)

# def disease(request, dis=None):
#     import pandas as pd
#     import numpy as np
#     import matplotlib.pyplot as plt
#     df = pd.read_csv('alldata.csv')
#     df=df[df['Cause of death or injury']=='Tuberculosis']
#     df=df.groupby(['Location','Cause of death or injury']).sum().reset_index()
#     df.plot (x= "Location", y = "Value", kind='bar')
#     plt.show()
# from django.shortcuts import render
# import matplotlib.pyplot as plt
# from django.http import HttpResponse, Http404, HttpResponseRedirect
#
# def index(request):
#     return HttpResponse("Que pasó, parcerooooos")
#
# import matplotlib.pyplot as plt, numpy as np
#
# def pic(request, c = None):
#
#    t = np.linspace(0, 2 * np.pi, 30)
#    u = np.sin(t)
#
#    plt.figure() # needed, to avoid adding curves in plot
#    plt.plot(t, u, color = c)
#
#    # write bytes instead of file.
#    from io import BytesIO
#    figfile = BytesIO()
#
#    # this is where the color is used.
#    try: plt.savefig(figfile, format = 'png')
#    except ValueError: raise Http404("No such color")
#
#    figfile.seek(0) # rewind to beginning of file
#    return HttpResponse(figfile.read(), content_type="image/png")
#
# from os.path import join
# from django.conf import settings
#
# def mortal(request, region = None , disease = None):
#    import pandas as pd
#
#    filename = join(settings.STATIC_ROOT, 'myapp/alldata.csv')
#
#    df = pd.read_csv(filename)
#
#    if region: df = df[df["Location"] == str(region)]
#    # if disease: df = df[df["Cause of death or injury"] == str(disease)]
#
# #change to code plot
#    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
#    table = table.replace('border="1"','border="0"')
#    table = table.replace('style="text-align: right;"', "")
#
#    return HttpResponse(table)
#
# # def display_table(request, a = "a", b = "b"):
# #
# #     Location = request.GET.get('Location', 'EastAsiaPacific')
# #     disease = request.GET.get('Cause of death or injury', 'Tuberculosis')
# #
# #     params = {'title' : Location,
# #               'form_action' : reverse_lazy('myapp:display_table'),
# #               'form_method' : 'get',
# #               'form' : InputForm1({'Location' : Location}),
# #               'form1' : GradesForm({'Cause of death or injury' : disease,}),
# #               'html_table' : reverse_lazy("myapp:plottable", kwargs = {'a' : Location, 'b' : disease}),
# #               'Location' : Location,
# #               'Variable1' : disease}
# #
# #     return render(request, 'view_table.html', params)
# #
# # def plottable(request, a = "EastAsiaPacific", b = "Tuberculosis"):
# #
# #     filename = join(settings.STATIC_ROOT, 'myapp/alldata.csv')
# #
# #     df = pd.read_csv(filename)
# #
# #     df = df[df["Location"].str.lower() == a.lower()]
# #     af = df.filter(regex= b)
# #     cols=set(af.columns)
# #     cols.add('Value')
# #     cols = list(cols)
# #     df2 = df[cols]
# #     colss = df2.columns.tolist()
# #     colss = colss[-6:] + colss[:-6]
# #     df2 = df2[colss]
# #
# #     table = df2.to_html(float_format = "%.3f", classes = "table table-striped", index = False)
# #     table = table.replace('border="1"','border="3"')
# #     table = table.replace('style="text-align: right;"', "")
# #     table
# #
# #     return HttpResponse(table)
