# Juego_Halloween
Creación de juego en Phyton para Halloween

# Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Calls](#calls)
5. [Collaboration](#collaboration)
6. [FAQs](#faqs)
## General Info
***
Desarrollo de un juego simple en Phyton, utilizando la librería Pygame.
El juego se trata de un laberinto y el usuario tendrá que escapar de el pudiendo utilizar ayudas u objetos por el camino.
Resultado:
:white_check_mark: Proyecto terminado :white_check_mark:
## Screenshot
***
```json
[
  {
    "nombre": "Ana",
    "apellido": "López",
    "fecha_nacimiento": "2002-01-15",
    "direccion": "Calle A, Ciudad A",
    "telefono": "123456789",
    "estudiantes_id": "1"
  },
  {
    "nombre": "Juan",
    "apellido": "Gómez",
    "fecha_nacimiento": "2003-02-28",
    "direccion": "Calle B, Ciudad B",
    "telefono": "987654321",
    "estudiantes_id": "2"
  },
  ...
]
```

## Technologies
***
* [Docker](https://www.docker.com/): _Version 24.0.6_
* [Apache2](https://apache.org/): _Version 2.4.56_
* [MySQL](https://www.mysql.com/): _Version 8.1.0_
* [PHP](https://www.php.net/): _Version 7.4.33_
## Installation
***
Crea la imagen en base al `docker-compose` en docker mediante el siguiente comando 
```bash
docker-compose build
```
Levanta los contenedores con los servicios especificados en Dockerfile y docker-compose mediante el siguiente comando
```bash
docker-compose up -d
```
Accede a la base de datos mediante, por ejemplo, `DBeaver` y completala con tablas y datos.

## Calls
***
Mediante el programa `Postman`, verifica el funcionamiento de las APIs con las siguientes búsquedas:

### GET (Find Data)
````bash
http://localhost:8080/estudiantes/
http://localhost:8080/estudiantes/?id=#indicar un id#

http://localhost:8080/profesores/
http://localhost:8080/profesores/?id=#indicar un id#

http://localhost:8080/calificaciones/
http://localhost:8080/calificaciones/?id=#indicar un id#

http://localhost:8080/inscripciones/
http://localhost:8080/inscripciones/?id=#indicar un id#

http://localhost:8080/asignatura/
http://localhost:8080/asignatura/?id=#indicar un id#
````

### PUT (Create/Add Data)
````bash
http://localhost:8080/estudiantes/
````

### POST (Update Data)
````bash
http://localhost:8080/estudiantes/
http://localhost:8080/estudiantes/#indicar un id#
````

### DELETE (Remove Data)
````bash
http://localhost:8080/estudiantes/?id=#indicar un id#
````

## Collaboration
***
## FAQs
***
Listado de preguntas frecuentes
1. **¿Tiene una utilidad práctica?**

No, se trata de un ejercicio. Sirve para comprender el funcionamiento de las APIs

