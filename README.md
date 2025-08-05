# Prueba Técnica - Microservicio Django REST

Este proyecto es un microservicio desarrollado con **Django 4.2+** y **Django REST Framework** para la gestión de productos, cumpliendo con los requisitos de la prueba técnica. La aplicación expone una API RESTful para realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) en un modelo `Producto`.

## Tecnologías utilizadas

* **Django 4.2+** 
* **Django REST Framework** 
* **SQLite** (como base de datos) 
* **Docker y docker-compose** (para el entorno del proyecto) 

## Estructura de la API

El sistema expone una API para el modelo `Producto` con los siguientes campos:

* `id`: Auto-generado 
* `nombre`: Campo de texto corto (char), requerido 
* `descripcion`: Campo de texto largo, opcional 
* `precio`: Campo decimal, requerido 
* `disponible`: Campo booleano, con valor por defecto `True` 

## Endpoints de la API

La API expone los siguientes endpoints:

* **`GET /api/productos/`**
    * **Función:** Listar todos los productos. [cite: 23, 24]
* **`POST /api/productos/`**
    * **Función:** Crear un nuevo producto. [cite: 25, 26]
* **`GET /api/productos/{id}/`**
    * **Función:** Obtener un producto específico por su ID. 
* **`PUT /api/productos/{id}/`**
    * **Función:** Actualizar un producto existente. [cite: 28, 29]
* **`DELETE /api/productos/{id}/`**
    * **Función:** Eliminar un producto. [cite: 30, 31]

## Instrucciones de uso

### 1. Instalación local

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_del_repositorio>
    cd mi_proyecto_drf
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar migraciones:** 
    ```bash
    python manage.py makemigrations productos_api
    python manage.py migrate
    ```

5.  **Iniciar el servidor:** 
    ```bash
    python manage.py runserver
    ```
    La API estará disponible en `http://127.0.0.1:8000/api/`

### 2. Instalación con Docker

1.  **Construir y ejecutar los contenedores:** 
    ```bash
    docker-compose up --build
    ```

2.  **Ejecutar las migraciones dentro del contenedor:**
    * Abre una nueva terminal.
    * ```bash
        docker-compose exec web python manage.py makemigrations productos_api
        docker-compose exec web python manage.py migrate
        ```
    La API ya estará accesible en `http://127.0.0.1:8000/api/`.

### 3. Ejecutar pruebas

Para ejecutar las pruebas básicas, utiliza el siguiente comando: [cite: 20, 37]

```bash
python manage.py test