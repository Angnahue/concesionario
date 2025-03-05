Concesionario de Automóviles
Este es un proyecto web desarrollado en Django que implementa un sistema para la gestión de un concesionario de automóviles. El sistema permite administrar clientes, modelos de autos y vendedores. Además, incluye formularios para ingresar datos y realizar búsquedas en la base de datos.
Características

* Implementado con el patrón MVT de Django.
* Uso de herencia de plantillas en HTML.
* Tres modelos principales: Cliente, Modelo_de_auto y Vendedor.
* Formularios para ingresar datos a cada modelo.
* Un formulario de búsqueda en la base de datos.
* Base de datos SQLite.

Instalación y Ejecución

Requisitos previos
Asegúrate de tener instalado:
* Python 3
* Django
* pipenv (opcional para gestionar dependencias)


Pasos de instalación
1. Clona el repositorio desde GitHub:
	git clone https://github.com/Angnahue/concesionario.git
	cd concesionario
EN POWERSHELL
2. Crea y activa un entorno virtual (opcional pero recomendado):
	python -m venv venv
	venv\Scripts\activate
3. Instala las dependencias del proyecto:
	pip install -r requirements.txt
4. Aplica las migraciones a la base de datos:
	python manage.py migrate
5. Ejecuta el servidor de desarrollo:
	python manage.py runserver
6. Accede a la aplicación en tu navegador:
	http://127.0.0.1:8000/
Uso del sistema
* Puedes agregar clientes, modelos de autos y vendedores a través de los formularios en la interfaz web.

Este es un proyecto web desarrollado en Django que simula un sistema de concesionario de automóviles. Permite registrar clientes, vendedores y modelos de autos, así­ como realizar búsquedas en la base de datos.  

**CaracterÃ­sticas del Proyecto**  

Implementa el patrÃ³n **MVT (Model-View-Template)** en Django.  
Utiliza **herencia de plantillas HTML** para la estructura de la web.  
Incluye **tres modelos** en la base de datos:  
   - `Cliente`: Representa a los clientes del concesionario.  
   - `ModeloDeAuto`: Representa los modelos de automÃ³viles disponibles.  
   - `Vendedor`: Representa a los vendedores del concesionario.  
