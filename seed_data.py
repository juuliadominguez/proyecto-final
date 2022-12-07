from ejemplo.models import Familiar
from datetime import datetime
Familiar(nombre="Pedro", direccion= "Av. Libertador 00", numero_pasaporte=123123, fecha_de_nacimiento=datetime(2005, 7, 5)).save()
Familiar(nombre="Emilia", direccion= "Cabello 1880", numero_pasaporte=345345, fecha_de_nacimiento=datetime(1999, 1, 26)).save()
Familiar(nombre="Alejandro", direccion= "Mansilla 123", numero_pasaporte=890890, fecha_de_nacimiento=datetime(1969, 6, 11)).save()
Familiar(nombre="Veronica", direccion= "Rio Parana 745", numero_pasaporte=567567, fecha_de_nacimiento=datetime(1970, 11, 28)).save()
print("Se cargo con éxito los usuarios de pruebas")