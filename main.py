from Religion import Religion
from arbolReligiones import arbolReligiones

#datos de algunas religiones
datos = [
    ("Hinduismo",-1000),
    ("Budismo",-500),
    ("Judaísmo",-950),
    ("Cristianismo",33),
    ("Islam",630),
    ("Sijismo",1469),
    ("Taoísmo",-500),
    ("Confucianismo",-500),
    ("Shinto",660),
    ("Zoroastrismo",-600)
]


religiones = []

for nombre,anio in datos:
    religion = Religion(nombre=nombre,anio_origen=anio)
    religiones.append(religion)


arbol = arbolReligiones()   
for religion in religiones:
    arbol.agregar_religion(religion)

arbol.listar_religiones()

encontrada = arbol.buscar("Cristianismo")

if encontrada is not None:
    print(f"\nSe encontró la religión: {encontrada.nombre}, Año de origen: {encontrada.anio_origen}")
else:
    print("\nNo se encontró la religión.")   
