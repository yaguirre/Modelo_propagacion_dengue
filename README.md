## Modelo Matemático de Propagación del Dengue

Este modelo matemático  fue creado para predecir la propagación del virus del Dengue en la ciudad de Bello, Antioquia siguiendo un modelo matemático que utiliza sistemas de ecuaciones diferenciales ordinarias, desarrollado por el semillero de investigación matemática de la Universidad EAFIT de Medellín. **El modelo matemático fue construido por el semillero, en este trabajo solo lo llevamos a la implementación en python**

### Tecnologías usadas
<img src="django.png" alt="Django" style="float: left; margin-right: 10px;" /> 

<img src="javascript.png" alt="Javascript" style="float: left; margin-right: 10px;" /> 

<img src="python.png" alt="Python" style="float: left; margin-right: 10px;" /> 

<img src="numpy.png" alt="Numpy" style="float: left; margin-right: 10px;" /> 



### Equipo de trabajo

El equipo de trabajo fue conformado por 5 miembros:

- Geralin Stefania Fernandez Bedoya
Ingeniera de sistemas - Universidad EAFIT

- Valentín Quintero Castrillón
Ingeniero de sistemas - Universidad EAFIT

- Yorman Andres Aguirre Martinez
Ingeniero de sistemas  - Universidad EAFIT

- Christian Londoño Cañas
Ingeniero de sistemas - Universidad EAFIT

- Juan Diego Saldarriaga
Ingeniero de sistemas - Universidad EAFIT

## Instrucciones
#### 1. Instalar Python (3.6.4 recommended)
Debido a que el proyecto fue desarrollado usando el framework de desarrollo web para python, 'Django', es necesario tener instalado en tu maquina una versión de python para poder ejecutar el proyecto. Recomendamos la versión 3.6.4 debido a que fue con esta versión que se desarrollo el proyecto.

#### 2. Clonar el repositorio
```bash
$ git clone https://github.com/yaguirre/Modelo_propagacion_dengue.git your_project_folder\
```

#### 3. Ambiente virtual de python (Virtualenv)
Es una herramienta para crear entornos python aislados. Desde python 3.3, un subconjunto se ha integrado en la biblioteca estándar bajo el módulo venv. Para instalar esta herramienta es necesario tener instalado python y el manejador de paquetes **pip**.

```bash
$ pip install virtualenv
$ virtualenv -p python3 your_project_folder\
```
#### 4. Iniciar ambiente virtual
Seguidamente debemos movernos al directorio donde creamos el ambiente virtual e inicializarlo, para esto debemos seguir dar los siguientes comandos
```
$ cd your_project_folder\

# Windows
$ Scripts\activate.bat

# Linux
$ source Scripts\activate
```
Una vez hecho esto, el prompt de la terminal que estemos usando deberia cambiar a algo similar a esto:

```bash
(your_project_folder)$ 
```

#### 5. Instalar dependencias 
En el archivo plano 'requirements.txt' clonado del repositorio, se encuentran todas las librerias y dependencias que usa el proyecto para su correcto funcionamiento, estas deben ser instaladas:

```bash
(your_project_folder)$ pip install -r requirements.txt
```

#### 6. Ejecutar el servidor
Al instalar el archivo con los requerimientos, una de las dependencias que tendremos en nuestro sistemas sera la de Django, al tener Django podemos ejecutar el servidor integrado de pruebas del que este dispone. Para ejecutarlo y poder visualizar el proyecto en acción solo tendremos que seguir los pasos listados a continuación:

```
(your_project_folder)$ cd src\
(your_project_folder)$ python manage.py runserver
August 19, 2019 - 13:43:12
Django version 1.11.20, using settings 'calculator.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Al poner en nuestro navegador la dirección local: ***http://127.0.0.1:8000/*** o  ***http://localhost:8000/*** podremos visualizar el simulador del modelo de propagación del dengue.
