from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse, Http404, HttpResponseRedirect


def index(request):
    return HttpResponse("Que pasó, parcerooooos")

import matplotlib.pyplot as plt, numpy as np

def pic(request, c = None):

   t = np.linspace(0, 2 * np.pi, 30)
   u = np.sin(t)

   plt.figure() # needed, to avoid adding curves in plot
   plt.plot(t, u, color = c)

   # write bytes instead of file.
   from io import BytesIO
   figfile = BytesIO()

   # this is where the color is used.
   try: plt.savefig(figfile, format = 'png')
   except ValueError: raise Http404("No such color")

   figfile.seek(0) # rewind to beginning of file
   return HttpResponse(figfile.read(), content_type="image/png")
