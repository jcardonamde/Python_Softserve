import csv
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def export_to_csv(queryset, fieldnames, filename, rowfunc):
    """
    queryset    – Django QuerySet
    fieldnames  – lista de encabezados CSV
    filename    – nombre de fichero (p.ej. "propietarios.csv")
    rowfunc     – función que recibe un objeto y devuelve lista de valores de fila
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    writer = csv.writer(response)
    writer.writerow(fieldnames)
    count = 0
    for obj in queryset:
        writer.writerow(rowfunc(obj))
        count += 1
    logger.info("Exportados %d registros a %s", count, filename)
    return response
