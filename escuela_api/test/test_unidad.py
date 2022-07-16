from asyncio.windows_events import NULL
from escuela_api import api

def test_lista_estudiante():
    assert api.eliminar_asistencia_por_cedula('12345678') == 'asistencias eliminada'