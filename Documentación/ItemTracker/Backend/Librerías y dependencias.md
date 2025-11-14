Se utilizarán las siguientes librerías de Python para el desarrollo del proyecto:

### PyMongo

PyMongo es una librería que permite interactuar con bases de datos MongoDB. Su función principal es facilitar la comunicación entre la aplicación y la base de datos, permitiendo realizar operaciones de lectura y escritura de datos de manera eficiente.  
Documentación: [https://pymongo.readthedocs.io/en/stable/](https://pymongo.readthedocs.io/en/stable/)

### FastAPI

FastAPI es un framework de Python que permite crear APIs RESTful de manera sencilla y rápida. Soporta los métodos HTTP estándar:

- GET: para leer datos
- POST: para crear nuevos datos
- PUT: para actualizar datos existentes
- PATCH: para actualizar parcialmente datos existentes
- DELETE: para eliminar datos 

Estos métodos se utilizan comúnmente para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar), que son fundamentales en el desarrollo de aplicaciones. FastAPI simplifica la creación de APIs y permite una comunicación eficiente entre el frontend y el backend a través de un puerto local.  
Documentación: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

### Habiticalib

Habiticalib es una librería de Python diseñada para interactuar con la API de Habitica. Permite a los desarrolladores autenticarse con su usuario y contraseña, lo que les da acceso a la información del servidor y les permite enviar datos hacia él. Esta librería es útil para aquellos que desean integrar funcionalidades de Habitica en sus propias aplicaciones.  
Documentación: [https://tr4nt0r.github.io/habiticalib/](https://tr4nt0r.github.io/habiticalib/)