from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Gatos, Perros
from ejemplo.forms import Buscar, FamiliarForm, GatosForm, PerrosForm
from django.views import View

def index(request):
    return render(request, "ejemplo/saludar.html")


def saludar_a(request, nombre):
    return render(request, 
    'ejemplo/saludar_a.html',
    {"nombre": nombre}
    )


def sumar(request, a, b):
    return render(request, 
    'ejemplo/sumar.html',
    {"a": a,
     "b": b,
     "resultado": a + b
    }
    )


def buscar(request):
    lista_de_nombres= ["German", "Daniel", "Romero", "Alvaro", ]
    query= request.GET ['q']

    if query in lista_de_nombres:
        indice_del_resultado= lista_de_nombres.index(query)
        resultado= lista_de_nombres[indice_del_resultado]
    else:
        resultado= "no hay match"
   

    return render(request, 'ejemplo/buscar.html', {"resultado": resultado})


def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})


def mostrar_gatos(request):
  lista_gatos = Gatos.objects.all()
  return render(request, "ejemplo/gatos.html", {"lista_gatos": lista_gatos})


def mostrar_perros(request):
  lista_perros = Perros.objects.all()
  return render(request, "ejemplo/perros.html", {"lista_perros": lista_perros})



class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})


class AltaFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares= Familiar.objects.all
      return render(request, self.template_name, {'lista_familiares': familiares})



class BuscarGatos(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_gatos.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_gatos = Gatos.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_gatos':lista_gatos})
        return render(request, self.template_name, {"form": form})

class AltaGatos(View):
    form_class = GatosForm
    template_name = 'ejemplo/alta_gatos.html'
    initial = {"nombre":"", "edad":"", "sexo":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el gato {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarGatos(View):
  form_class = GatosForm
  template_name = 'ejemplo/actualizar_gatos.html'
  initial = {"nombre":"", "edad":"", "sexo":""}
  
  def get(self, request, pk): 
      gatos = get_object_or_404(Gatos, pk=pk)
      form = self.form_class(instance=gatos)
      return render(request, self.template_name, {'form':form,'gatos': gatos})

  def post(self, request, pk): 
      gatos = get_object_or_404(Gatos, pk=pk)
      form = self.form_class(request.POST ,instance=gatos)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el gato {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'gatos': gatos,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarGatos(View):
  template_name = 'ejemplo/gatos.html'
  
  def get(self, request, pk): 
      gatos = get_object_or_404(Gatos, pk=pk)
      gatos.delete()
      gatos= Gatos.objects.all
      return render(request, self.template_name, {'lista_gatos': gatos})


class BuscarPerros(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_perros.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_perros = Perros.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_perros':lista_perros})
        return render(request, self.template_name, {"form": form})


class AltaPerros(View):
    form_class = PerrosForm
    template_name = 'ejemplo/alta_perros.html'
    initial = {"nombre":"", "edad":"", "sexo":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el perro {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarPerros(View):
  form_class = PerrosForm
  template_name = 'ejemplo/actualizar_perros.html'
  initial = {"nombre":"", "edad":"", "sexo":""}
  
  def get(self, request, pk): 
      perros = get_object_or_404(Perros, pk=pk)
      form = self.form_class(instance=perros)
      return render(request, self.template_name, {'form':form,'perros': perros})

  def post(self, request, pk): 
      perros = get_object_or_404(Perros, pk=pk)
      form = self.form_class(request.POST ,instance=perros)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el perro {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'perros': perros,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarPerros(View):
  template_name = 'ejemplo/perros.html'
  
  def get(self, request, pk): 
      perros = get_object_or_404(Perros, pk=pk)
      perros.delete()
      perros= Perros.objects.all
      return render(request, self.template_name, {'lista_perros': perros})

