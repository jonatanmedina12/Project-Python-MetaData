# Herramientas de Información y Extracción de Metadatos

Este proyecto en Python proporciona un conjunto de herramientas para recopilar información sobre dominios, números de teléfono, realizar consultas WHOIS y extraer metadatos de diversos tipos de archivos. 

## Características

1. Búsqueda DNS
2. Información de Números de Teléfono
3. Información de Dominio WHOIS
4. Extracción de Metadatos de Archivos (Imágenes, PDF, DOCX)

## Requisitos

Para ejecutar este proyecto, necesitarás Python 3.x y las siguientes bibliotecas:

```
pip install -r .\requirements.txt
```

## Uso

### Búsqueda DNS

```python
from dns_config import DnsConfig

busqueda_dns = DnsConfig("ejemplo.com")
busqueda_dns.dns_search()
```

### Información de Número de Teléfono

```python
from phone_config import PhoneConfig

info_telefono = PhoneConfig("+34123456789")
info = info_telefono.phone_search()
print(info)
info_telefono.mapa(info["Pais"])
```

### Consulta WHOIS

```python
from whois_config import WhoisConfig

consulta_whois = WhoisConfig("ejemplo.com")
consulta_whois.whois_search()
```

### Extracción de Metadatos

```python
from metadata_extractor import extract_metadata

resultado = extract_metadata("ruta/del/archivo")
if resultado["success"]:
    print(resultado["metadata"])
else:
    print(f"Error: {resultado['error']}")
```

## Detalles de la Extracción de Metadatos

La extracción de metadatos soporta los siguientes tipos de archivos:

- Imágenes (JPG, JPEG, PNG)
- PDF
- DOCX (Microsoft Word)

Para cada tipo de archivo, se extraen diferentes tipos de metadatos:

- Imágenes: Información EXIF y metadatos generales.
- PDF: Metadatos del documento, texto extraído y correos electrónicos encontrados.
- DOCX: Propiedades del documento y texto extraído.

## Nota de Seguridad

Este conjunto de herramientas está diseñado para fines educativos y de investigación. Asegúrate de usar estas herramientas de manera responsable y en cumplimiento con las leyes y regulaciones aplicables. Algunos usos pueden requerir autorización adecuada.

## Contribuir

Se agradecen las contribuciones a este proyecto. Si tienes alguna mejora o nueva funcionalidad, no dudes en hacer un fork del repositorio y enviar un pull request.

## Licencia

Mozilla Public License Version 2.0