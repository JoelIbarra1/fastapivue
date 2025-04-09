# Proyecto CRUD con MVC usando FastAPI y Vue.js

Este proyecto tiene como objetivo crear una aplicación CRUD utilizando el patrón MVC, con **FastAPI** en el backend y **Vue.js** en el frontend. El enfoque principal es aprender a trabajar con estos frameworks modernos y entender cómo se integran en una arquitectura MVC.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd fastapi_crud

2. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   
3. Activa el entorno virtual:
   ```bash
   .\venv\Scripts\activate

4. Inicia el servidor de desarrollo de FastAPI:
   ```bash
   uvicorn app.main:app --reload
   
Accede a la aplicación en tu navegador en http://127.0.0.1:8000.

## Estructura del Backend

La aplicación de backend sigue el patrón de arquitectura MVC (Modelo-Vista-Controlador) para organizar el código de manera modular. La estructura de carpetas del backend es la siguiente:

El proyecto fastapi_crud está organizado en varias carpetas dentro del directorio app. El archivo principal main.py actúa como el punto de entrada de la aplicación. Dentro de models/, se encuentran los modelos de datos definidos con SQLAlchemy, como user.py. Los esquemas de validación de datos, utilizando Pydantic, se encuentran en la carpeta schemas/, con ejemplos como user.py. La lógica del controlador se organiza en la carpeta controllers/, con archivos como user_controller.py, que manejan las operaciones CRUD. Las rutas de la API están definidas en la carpeta routes/, y un archivo como user_routes.py gestiona los endpoints. Además, database.py se encarga de la conexión y configuración de la base de datos, y config.py incluye configuraciones generales del proyecto.


### Descripción de las carpetas y archivos:

- **main.py**: Es el punto de entrada de la aplicación FastAPI. Aquí se inician las rutas y se configuran los servicios.
- **models/**: Contiene los modelos de datos definidos con SQLAlchemy. En este caso, `user.py` define el modelo para el usuario.
- **schemas/**: Contiene los esquemas de validación creados con Pydantic, que se usan para validar y serializar los datos. En este caso, `user.py` define los esquemas de entrada y salida para los usuarios.
- **controllers/**: Implementa la lógica de control, encargada de procesar las peticiones y las interacciones con la base de datos. `user_controller.py` maneja las operaciones CRUD del modelo User.
- **routes/**: Define las rutas de la API, que conectan las peticiones HTTP con las funciones de los controladores. `user_routes.py` define las rutas relacionadas con los usuarios.
- **database.py**: Contiene la configuración de la base de datos y las conexiones necesarias.
- **config.py**: Archivo de configuración general para variables globales o parámetros de la app.

## Dependencias

Este proyecto utiliza las siguientes dependencias:

- **FastAPI**: Framework para la creación de APIs.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.
- **SQLAlchemy**: ORM para interactuar con la base de datos.
- **aiosqlite**: Conector asincrónico para SQLite con soporte de SQLAlchemy.

## Frontend (Vue.js)

La aplicación frontend está organizada con la estructura estándar de Vue.js. Los archivos principales incluyen:

- **components/**: Contiene los componentes reutilizables de la interfaz de usuario.
  - `UserForm.vue`: Componente para el formulario de creación y edición de usuarios.
  - `UserList.vue`: Componente para mostrar la lista de usuarios.

- **views/**: Aquí se encuentran las vistas principales de la aplicación.
  - `HomeView.vue`: Vista principal donde se integran los componentes como `UserForm` y `UserList`.

- **services/**: Encargada de la comunicación con la API backend.
  - `api.js`: Archivo donde se gestionan las peticiones HTTP al backend utilizando Axios o Fetch.

- **App.vue**: Componente raíz que configura la estructura de la aplicación.
- **main.js**: Archivo de entrada de la aplicación, donde se configura Vue.js y se monta la aplicación en el DOM.

Esta estructura modular y organizada permite que el frontend interactúe de manera eficiente con el backend, manteniendo una separación clara entre la lógica de negocio, la interfaz de usuario y la comunicación con la API.

## Objetivo del Proyecto
El objetivo principal de este proyecto fue aprender y practicar el uso de FastAPI y Vue.js para desarrollar aplicaciones web modernas. A través de la implementación del patrón MVC en el backend, se profundizó en los siguientes conceptos:

Creación de APIs con FastAPI.

Conexión y manipulación de bases de datos usando SQLAlchemy.

Validación de datos de entrada y salida con Pydantic.

Organización de la lógica en controladores, modelos y rutas.

Uso de Vue.js en el frontend para interactuar con la API backend.

## Conclusiones
Este proyecto ha sido una excelente oportunidad para comprender el flujo de datos en una aplicación web moderna, desde la interacción del frontend con la API hasta la lógica del backend y la persistencia de datos en la base de datos. Además, FastAPI ha demostrado ser un framework rápido y fácil de usar para construir APIs, mientras que Vue.js es una excelente opción para crear interfaces de usuario reactivas.

