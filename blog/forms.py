from django import forms
from . import models

projects = models.project_model.objects.all()
proy = {}

for project in projects:
    proy[project.id] = project.name

class CustomBooleanWidget(forms.widgets.CheckboxInput):
    def value_from_datadict(self, data, files, name):
        print("Llamado a value_from_datadict")
        value = super().value_from_datadict(data, files, name)
        return value == 'on'

class form_task(forms.Form):
    title = forms.CharField(label="titulo",max_length=200)
    description = forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)
    project = forms.ModelChoiceField(label="Proyecto al que pertenece",queryset=models.project_model.objects.all())



class form_project(forms.Form):
    name = forms.CharField(label='Nombre del proyecto',max_length='50',)

class form_tareas(forms.Form):
    title = forms.CharField(label='Tareas',max_length='50')
    description = forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)
    available = forms.BooleanField(label="Disponible",required=False,widget=CustomBooleanWidget())

