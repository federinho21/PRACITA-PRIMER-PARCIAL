"""Datos iniciales: cada religión se registra una sola vez.

Fechas aproximadas para la práctica, no fechas exactas de fundación.
None indica un dato desconocido o que no tiene una única respuesta.
Las relaciones constituyen un modelo didáctico simplificado.
"""
from Religion import Religion


DATOS_RELIGIONES = [
    {
        'nombre': 'Judaísmo',
        'deidad': 'Dios (YHWH)',
        'anio_origen': -950,
        'lugar_origen': 'Antiguo Israel y Judá, Oriente Próximo',
        'fundador': None,
        'creencias': ['monoteísmo', 'alianza', 'justicia', 'oración'],
        'libros_sagrados': ['Tanaj'],
        'descripcion': 'Alianza con Dios, cumplimiento de la Torá y vida justa.',
    },
    {
        'nombre': 'Cristianismo',
        'deidad': 'Dios: Padre, Hijo y Espíritu Santo en las ramas trinitarias',
        'anio_origen': 33,
        'lugar_origen': 'Judea, Oriente Próximo',
        'fundador': 'Jesús de Nazaret, figura fundacional',
        'creencias': ['monoteísmo', 'resurrección', 'amor al prójimo', 'oración'],
        'libros_sagrados': ['Biblia'],
        'descripcion': 'Fe en Jesucristo, amor a Dios y al prójimo y esperanza de salvación.',
    },
    {
        'nombre': 'Islam',
        'deidad': 'Alá (Dios)',
        'anio_origen': 610,
        'lugar_origen': 'Península arábiga',
        'fundador': 'Mahoma, profeta central',
        'creencias': ['monoteísmo', 'oración', 'caridad', 'ayuno', 'peregrinación'],
        'libros_sagrados': ['Corán'],
        'descripcion': 'Unicidad de Dios y vida guiada por la fe y los cinco pilares.',
    },
    {
        'nombre': 'Catolicismo',
        'deidad': 'Dios: Padre, Hijo y Espíritu Santo',
        'anio_origen': None,
        'lugar_origen': 'Mediterráneo y comunidades cristianas antiguas',
        'fundador': None,
        'creencias': ['monoteísmo', 'resurrección', 'sacramentos', 'amor al prójimo', 'oración'],
        'libros_sagrados': ['Biblia'],
        'descripcion': 'Fe en Cristo, vida sacramental y comunión con la Iglesia católica.',
    },
    {
        'nombre': 'Ortodoxia oriental',
        'deidad': 'Dios: Padre, Hijo y Espíritu Santo',
        'anio_origen': None,
        'lugar_origen': 'Mediterráneo oriental y comunidades cristianas antiguas',
        'fundador': None,
        'creencias': ['monoteísmo', 'resurrección', 'sacramentos', 'amor al prójimo', 'oración'],
        'libros_sagrados': ['Biblia'],
        'descripcion': 'Unión con Dios mediante la fe, la liturgia y la tradición apostólica.',
    },
    {
        'nombre': 'Protestantismo',
        'deidad': 'Dios; mayoritariamente entendido como Trinidad',
        'anio_origen': 1517,
        'lugar_origen': 'Europa occidental',
        'fundador': 'Martín Lutero y otros reformadores',
        'creencias': ['monoteísmo', 'resurrección', 'autoridad de las Escrituras', 'oración'],
        'libros_sagrados': ['Biblia'],
        'descripcion': 'Centralidad de las Escrituras, la fe y la gracia, con diferencias entre ramas.',
    },
    {
        'nombre': 'Religión védica',
        'deidad': 'Indra, Agni, Varuna y Soma, entre otros',
        'anio_origen': -1700,
        'lugar_origen': 'Noroeste del subcontinente indio',
        'fundador': None,
        'creencias': ['orden cósmico', 'ritual', 'ofrendas', 'divinidades'],
        'libros_sagrados': ['Rigveda', 'Samaveda', 'Yajurveda', 'Atharvaveda'],
        'descripcion': 'Mantenimiento del orden cósmico mediante himnos y prácticas rituales.',
    },
    {
        'nombre': 'Hinduismo',
        'deidad': 'Visnú, Shiva, Devi y otras deidades, según tradición',
        'anio_origen': None,
        'lugar_origen': 'Subcontinente indio',
        'fundador': None,
        'creencias': ['karma', 'renacimiento', 'liberación', 'dharma', 'ritual'],
        'libros_sagrados': ['Vedas', 'Upanishads', 'Bhagavad-gita', 'Puranas'],
        'descripcion': 'Diversas vías de práctica y conocimiento orientadas al dharma y la liberación.',
    },
    {
        'nombre': 'Budismo',
        'deidad': None,
        'anio_origen': -520,
        'lugar_origen': 'Norte del subcontinente indio',
        'fundador': 'Siddhartha Gautama (Buda)',
        'creencias': ['karma', 'renacimiento', 'liberación', 'meditación', 'compasión'],
        'libros_sagrados': ['Cánones budistas, según escuela'],
        'descripcion': 'Comprender y superar el sufrimiento mediante ética, meditación y sabiduría. '
                       'No se centra en un dios creador; esto no excluye seres celestiales.',
    },
    {
        'nombre': 'Budismo theravada',
        'deidad': None,
        'anio_origen': -250,
        'lugar_origen': 'Sur de Asia, con desarrollo importante en Sri Lanka',
        'fundador': None,
        'creencias': ['karma', 'renacimiento', 'liberación', 'meditación', 'compasión'],
        'libros_sagrados': ['Canon pali (Tipitaka)'],
        'descripcion': 'Disciplina, meditación y sabiduría orientadas a la liberación. '
                       'Buda es el maestro despierto, no un dios creador.',
    },
    {
        'nombre': 'Budismo mahayana',
        'deidad': 'Budas y bodhisattvas venerados, como Amitabha y Avalokiteshvara; no un dios creador',
        'anio_origen': 100,
        'lugar_origen': 'Subcontinente indio',
        'fundador': None,
        'creencias': ['karma', 'renacimiento', 'liberación', 'meditación', 'compasión', 'bodhisattva'],
        'libros_sagrados': ['Sutras mahayana', 'Sutra del Loto', 'Sutras de la Perfección de la Sabiduría'],
        'descripcion': 'Camino del bodhisattva y búsqueda del despertar para beneficio de todos los seres.',
    },
    {
        'nombre': 'Budismo vajrayana',
        'deidad': 'Budas y figuras meditativas tántricas; no un dios creador',
        'anio_origen': 800,
        'lugar_origen': 'India, con posterior desarrollo en Tíbet y otras regiones',
        'fundador': None,
        'creencias': ['karma', 'renacimiento', 'liberación', 'meditación', 'compasión', 'práctica tántrica'],
        'libros_sagrados': ['Tantras budistas', 'Kangyur y Tengyur en la tradición tibetana'],
        'descripcion': 'Prácticas tántricas orientadas al despertar, con iniciación y guía de un maestro.',
    },
]


# Son nombres que se resuelven a los objetos ya registrados, no fichas duplicadas.
# derivacion: rama o desarrollo dentro de una tradición.
# influencia: relación de influencia, sin afirmar que sea una rama directa.
DATOS_RELACIONES = [
    ('Judaísmo', 'Cristianismo', 'derivacion'),
    ('Cristianismo', 'Catolicismo', 'derivacion'),
    ('Cristianismo', 'Ortodoxia oriental', 'derivacion'),
    ('Cristianismo', 'Protestantismo', 'derivacion'),
    ('Judaísmo', 'Islam', 'influencia'),
    ('Cristianismo', 'Islam', 'influencia'),
    ('Religión védica', 'Hinduismo', 'derivacion'),
    ('Religión védica', 'Budismo', 'influencia'),
    ('Budismo', 'Budismo theravada', 'derivacion'),
    ('Budismo', 'Budismo mahayana', 'derivacion'),
    ('Budismo mahayana', 'Budismo vajrayana', 'derivacion'),
]


def cargar_religiones():
    """Devuelve un diccionario nombre -> objeto Religion, sin duplicados."""
    religiones = {}
    for datos in DATOS_RELIGIONES:
        # Copiar listas para que editar un objeto no altere los datos iniciales.
        valores = {campo: valor.copy() if isinstance(valor, list) else valor
                   for campo, valor in datos.items()}
        religion = Religion(**valores)
        if religion.nombre in religiones:
            raise ValueError('Religión repetida: ' + religion.nombre)
        religiones[religion.nombre] = religion
    return religiones


def cargar_relaciones(religiones):
    """Cada tupla contiene (objeto origen, objeto destino, tipo)."""
    relaciones = []
    for origen, destino, tipo in DATOS_RELACIONES:
        if origen not in religiones or destino not in religiones:
            raise ValueError('Una relación menciona una religión que no está registrada.')
        relaciones.append((religiones[origen], religiones[destino], tipo))
    return relaciones


if __name__ == '__main__':
    religiones = cargar_religiones()
    relaciones = cargar_relaciones(religiones)
    for religion in religiones.values():
        print('\n' + religion.nombre.upper())
        print('Deidad o figuras espirituales:', religion.deidad or 'No tiene un dios creador central')
        print('Año aproximado:', religion.anio_origen if religion.anio_origen is not None else 'Sin fecha única')
        print('Lugar:', religion.lugar_origen)
        print('Fundador:', religion.fundador or 'Sin fundador único identificado')
        print('Creencias:', ', '.join(religion.creencias))
        print('Libros:', ', '.join(religion.libros_sagrados))
        print('Pilar:', religion.descripcion)
    print('\nRELACIONES')
    for origen, destino, tipo in relaciones:
        print(f'{origen.nombre} -> {destino.nombre} ({tipo})')
