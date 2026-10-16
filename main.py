from datos_religiones import cargar_religiones, cargar_relaciones
from arbolReligiones import arbolReligiones

religiones = cargar_religiones()
relaciones = cargar_relaciones(religiones)

arbol = arbolReligiones()

for religion in religiones.values():
    arbol.agregar_religion(religion)

print("RELIGIONES")
arbol.listar_religiones()

print("\nRELACIONES")
for origen, destino, tipo in relaciones:
    print(f"{origen.nombre} -> {destino.nombre} ({tipo})")

encontrada = arbol.buscar("Cristianismo")

if encontrada is not None:
    print(f"\nSe encontró la religión: {encontrada.nombre}, Año de origen: {encontrada.anio_origen}")
else:
    print("\nNo se encontró la religión.")
