<<<<<<< HEAD
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
2. Crea y activa un entorno virtual (opcional pero recomendado):
python -m venv venv
	source venv/bin/activate  # En Windows usa: venv\Scripts\activate
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
* Usa el formulario de búsqueda para encontrar registros específicos en la base de datos.
Estructura del Proyecto
concesionario/
??? app_concesionario/    # Aplicación principal
?   	??? models.py         # Definición de los modelos
?   	??? views.py          # Lógica de las vistas
?   	??? forms.py          # Definición de formularios
?   	??? urls.py           # Definición de rutas
??? concesionario/        # Configuración del proyecto
??? db.sqlite3            # Base de datos SQLite
??? manage.py             # Comando para gestionar el proyecto
??? requirements.txt      # Dependencias del proyecto
??? README.md             # Este archivo
=======
# Concesionario
# ðŸš— Concesionario de Autos - Proyecto para Curso CODERHOUSE- Proyecto Django  

Este es un proyecto web desarrollado en Django que simula un sistema de concesionario de automÃ³viles. Permite registrar clientes, vendedores y modelos de autos, asÃ­ como realizar bÃºsquedas en la base de datos.  

## ðŸ“Œ **CaracterÃ­sticas del Proyecto**  

âœ… Implementa el patrÃ³n **MVT (Model-View-Template)** en Django.  
âœ… Utiliza **herencia de plantillas HTML** para la estructura de la web.  
âœ… Incluye **tres modelos** en la base de datos:  
   - `Cliente`: Representa a los clientes del concesionario.  
   - `ModeloDeAuto`: Representa los modelos de automÃ³viles disponibles.  
   - `Vendedor`: Representa a los vendedores del concesionario.  
âœ… Cuenta con **formularios para ingresar datos** en cada modelo.  
âœ… Permite **buscar modelos de autos** en la base de datos.  
>>>>>>> 01cedf91b955b0a2db1f169fb2075356272e7d0d
