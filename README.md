<<<<<<< HEAD
Concesionario de Autom�viles
Este es un proyecto web desarrollado en Django que implementa un sistema para la gesti�n de un concesionario de autom�viles. El sistema permite administrar clientes, modelos de autos y vendedores. Adem�s, incluye formularios para ingresar datos y realizar b�squedas en la base de datos.
Caracter�sticas
* Implementado con el patr�n MVT de Django.
* Uso de herencia de plantillas en HTML.
* Tres modelos principales: Cliente, Modelo_de_auto y Vendedor.
* Formularios para ingresar datos a cada modelo.
* Un formulario de b�squeda en la base de datos.
* Base de datos SQLite.
Instalaci�n y Ejecuci�n
Requisitos previos
Aseg�rate de tener instalado:
* Python 3
* Django
* pipenv (opcional para gestionar dependencias)
Pasos de instalaci�n
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
6. Accede a la aplicaci�n en tu navegador:
	http://127.0.0.1:8000/
Uso del sistema
* Puedes agregar clientes, modelos de autos y vendedores a trav�s de los formularios en la interfaz web.
* Usa el formulario de b�squeda para encontrar registros espec�ficos en la base de datos.
Estructura del Proyecto
concesionario/
??? app_concesionario/    # Aplicaci�n principal
?   	??? models.py         # Definici�n de los modelos
?   	??? views.py          # L�gica de las vistas
?   	??? forms.py          # Definici�n de formularios
?   	??? urls.py           # Definici�n de rutas
??? concesionario/        # Configuraci�n del proyecto
??? db.sqlite3            # Base de datos SQLite
??? manage.py             # Comando para gestionar el proyecto
??? requirements.txt      # Dependencias del proyecto
??? README.md             # Este archivo
=======
# Concesionario
# 🚗 Concesionario de Autos - Proyecto para Curso CODERHOUSE- Proyecto Django  

Este es un proyecto web desarrollado en Django que simula un sistema de concesionario de automóviles. Permite registrar clientes, vendedores y modelos de autos, así como realizar búsquedas en la base de datos.  

## 📌 **Características del Proyecto**  

✅ Implementa el patrón **MVT (Model-View-Template)** en Django.  
✅ Utiliza **herencia de plantillas HTML** para la estructura de la web.  
✅ Incluye **tres modelos** en la base de datos:  
   - `Cliente`: Representa a los clientes del concesionario.  
   - `ModeloDeAuto`: Representa los modelos de automóviles disponibles.  
   - `Vendedor`: Representa a los vendedores del concesionario.  
✅ Cuenta con **formularios para ingresar datos** en cada modelo.  
✅ Permite **buscar modelos de autos** en la base de datos.  
>>>>>>> 01cedf91b955b0a2db1f169fb2075356272e7d0d
