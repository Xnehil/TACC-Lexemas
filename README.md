# README - Corpus de Quechua Sureño

## Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar un corpus en Quechua Sureño para la creación de una herramienta de generación de textos narrativos. Estos textos están destinados a ser utilizados en material educativo y herramientas de práctica de comprensión escrita.

## Fuentes del Corpus
El corpus ha sido compilado utilizando las siguientes fuentes:

1. **Repositorio de Textos Educativos del MINEDU**
   - Descripción: Colección de textos educativos proporcionados por el Ministerio de Educación del Perú.
   - Método de extracción: Los textos en formato PDF fueron convertidos a texto plano utilizando herramientas de `pdf-to-text`.

2. **Archivos del Summer Institute of Linguistics “Language and Culture Archives”**
   - Descripción: Archivos que contienen datos lingüísticos y culturales sobre el Quechua Sureño.
   - Método de extracción: Utilización de herramientas de OCR para convertir documentos escaneados a texto.

## Estructura del Corpus
El corpus está organizado en un csv con oraciones extraídas de pdfs. Los archivos que se usaron para construir el corpus son los siguientes:

### Renzo
Todas los documentos se obtuvieron de https://repositorio.minedu.gob.pe/browse?type=subject&value=Quechua+Collao
   - 2 Rimana - Qillqasqa Mayt’u Qichwa Qullaw. Texto de Comunicación del 2° Secundaria - Quechua Collao
   - Ayllupi yachasunchik 3 ñiqi Qullaw qichwapi. Texto de Comunicación del 3° Primaria - Quechua Collao
   - Huk kutis kaq kasqa Literatura 2 quechua collao
   - Huk kutis kaq kasqa. Literatura 1 - 5° Primaria - Quechua collao
   - Llaqtanchikpa kawsayninkuna Saberes de los pueblos 2 - 2° Secundaria - Quechua collao
   - Llaqtanchikpa kawsayninkuna. Saberes de los pueblos 1 - 1° Secundaria - Quechua collao
   - Willakuykuna mayt’u - Collao Literatura 1 - 1° Secundaria - Quechua collao
  
### Harvy
   - Kasarakuy raymimanta. [Link](https://repositorio.minedu.gob.pe/handle/20.500.12799/6658)
   - Alelipa munaqusqan waqaychanankuna. Historias y Relatos 5 - Inicial - Quechua Collao. [Link]
   - Ayllunchikpa willakuyninkuna. Historias y relatos 2 - Inicial - Quechua Collao. [Link]
   - Liqichumanta. Historias y relatos 1 - Inicial - Quechua Collao. [Link]
   - Muhu papa rikch’arichiymanta. Historias y relatos 3 - Inicial - Quechua Collao. [Link]
   - Papa allay. Historias y Relatos 4 - Inicial - Quechua Collao. [Link]
   - 1 Rimana. Qichwa - Qullawpi llamk'ana mayt'u. Cuaderno de trabajo - Comunicación 1° - Quechua Collao. [Link]
   - 3 Rimana - Qillqasqa Mayt’u Qichwa Qullaw. Texto de Comunicación del 3° Secundaria - Quechua Collao. [Link]
   - 4 Rimana - Qillqasqa Mayt’u Qichwa Qullaw. Texto de Comunicación del 4° Secundaria - Quechua Collao. [Link]
   - 5 Rimana - Qillqasqa Mayt’u Qichwa Qullaw. Texto de Comunicación del 5° Secundaria - Quechua Collao. [Link]
### Amy
   - Willakuykuna mayt’u - Collao Literatura 1 - 1° Secundaria - Quechua collao. https://hdl.handle.net/20.500.12799/10037
   - Willakuykuna mayt’u - Collao : Literatura - Comunicación quechua, variante Collao. https://hdl.handle.net/20.500.12799/7580
   - Willakuykuna mayt’u - Collao Literatura 2 - 2° Secundaria - Quechua collao. https://hdl.handle.net/20.500.12799/10053
   - Ayllupi yachasunchik 1 ñiqi qullaw qichwapi. Texto de Comunicación del 1° Primaria - Quechua Collao. https://hdl.handle.net/20.500.12799/9978
   

## Proceso de Extracción
La extracción de datos se realizó a través de las siguientes etapas:

1. **Conversión de PDF a Texto**: Se utilizó Adobe Acrobat y herramientas de OCR para convertir los archivos PDF a texto.
2. **Limpieza de Datos**: Se realizó una limpieza inicial para eliminar encabezados, pies de página y cualquier otro contenido no relevante.
3. **Normalización de Texto**: Se normalizaron los caracteres especiales.


