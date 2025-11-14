# Backend

### Estructura del directorio
Para el backend, los módulos se organizarán en sus propias carpetas, cada una conteniendo los siguientes archivos:

- .venv
- modules/
	- nombre del módulo/
		- api.py
		- models.py
		- service.py
- main.py
- requirements.txt

Los siguientes archivos pueden ser ignorados y están incluidos en el `.gitignore`:
- `.venv/`
- `___pycahe__/`
### .venv
Este directorio contiene los ejecutables y librerías del entorno virtual, lo que ayuda a mantener de manera local todas las dependencias necesarias para el proyecto.
### api.py
Este archivo es fundamental para la implementación de la API, según el módulo en el que se integre. Su función principal es facilitar la comunicación y la interacción entre el backend y el frontend mediante la librería de FastAPI.
### models.py
Aquí se defininen las clases de modelos utilizando el formato `@dataclass`. Además, incluye funciones relacionadas con los modelos y, si es necesario, conversiones de tipos de datos.
### service.py
Este archivo contiene funciones internas que son necesarias para el funcionamiento del proyecto, pero que no necesariamente están directamente vinculadas a los modelos. Sin embargo, pueden hacer uso de ellos si es necesario.
### main.py
Este es el código principal que se encarga de ejecutar el backend de la aplicación 
### requirements.txt
Este documento es crucial para mantener un registro de las librerías necesarias para ejecutar la aplicación. Puedes generar este archivo utilizando el comando `pip freeze > requirements.txt`, lo que te permite instalar todas las dependencias necesarias de manera sencilla con `pip install -r requirements.txt`.

# Frontend

### Estructura del directorio
Para el frontend, cada carpeta organiza un tipo de contenido distinto:

- .godot
- addons/
- assets/
	- audio/
		- archivo_de_audio.ogg
		- archivo_de_audio.mp3
		- archivo_de_audio.wav
	- sprites/
		- imagen.png
		- imagen.svg
	- texturas/
		- textura.png
		- textura.svg
	- shaders/
		- shader.tscn
- componentes/
	- nombre del módulo/
		- nombre_del_componente_individual.tscn
- screens/
	- nombre_de_pantalla.tscn
- scripts/
	- script.gd
	- script.cs
- project.godot

Los siguientes archivos pueden ser ignorados y están incluidos en el `.gitignore`:
- `*.import`
- `.godot/`
### .godot
Este directorio contiene los ejecutables y configuraciones del proyecto en Godot.
### addons/
Contiene los addons de Godot implementados en el proyecto, esto incluye herramientas y plugins extras.
### assets/
La carpeta de assets se divide en varias subcarpetas para organizar diferentes tipos de activos del proyecto.
#### audio/
Contiene archivos de audio utilizados en el proyecto, se pueden usar los siguientes formatos:
- .ogg
- .mp3
- .wav
#### sprites/
Almacena las imágenes y sprites utilizados en el proyecto, incluyendo los siguientes formatos:
- .png
- .jpeg
- .gif
- .svg
#### texturas/
Contiene las texturas y patrones utilizados en el proyecto, como los siguientes formatos:
- .png
- .jpeg
- .gif
- .svg
#### shaders/
Almacena los shaders personalizados utilizados en el proyecto, puede ser en los formatos:
- .tscn
- .gdshader
### componentes/
Esta sección se divide en subcarpetas para cada módulo del proyecto, conteniendo componentes específicos de cada uno en formato `.tscn`. Esto contiene los elementos de Interfaz de Usuario o elementos similares.
### screens/
Contiene las pantallas o escenas del proyecto en formato `.tscn`
### scripts/
Almacena los scripts utilizados en el proyecto, en los siguientes formatos:
- .gd (Godot Script)
- .cs (C# Script)
### project.godot
Este archivo es el corazón del proyecto, donde se configura y se ejecuta la aplicación en Godot.

Esta estructura permite una organización clara y eficiente de los activos y código del proyecto, facilitando el desarrollo y mantenimiento del mismo.