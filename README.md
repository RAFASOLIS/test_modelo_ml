# Proyecto Base de Regresión (ML Service)

Este repositorio contiene el código para entrenar un modelo de regresión (Lineal y Random Forest) y exponerlo a través de una API RESTful dockerizada.

## 🎯 Objetivo

El objetivo es predecir [Variable Objetivo] basándose en [Features Principales].

## 🛠️ Estructura del Proyecto

* `modelo.ipynb`: Notebook de exploración, entrenamiento y guardado del modelo.
* `api.py`: API (Flask/FastAPI) para servir el modelo.
* `Dockerfile`: Define el contenedor para ejecutar la API.
* `requirements.txt`: Dependencias de Python.
* `modelo_entrenado.pkl`: (Generado por el Notebook) El modelo serializado.

## 🚀 Uso y Ejecución

### 1. Requisitos Previos

* Python 3.9+
* Docker

### 2. Entrenamiento (Local)

1.  Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
2.  Ejecuta el Notebook `modelo.ipynb` para generar `modelo_entrenado.pkl`.

### 3. Ejecución (Docker)

1.  Construye la imagen de Docker:
    ```bash
    docker build -t mi_api_ml .
    ```
2.  Ejecuta el contenedor:
    ```bash
    docker run -p 5000:5000 mi_api_ml
    ```

### 4. Probar la API

Envía una petición POST al endpoint `/predict`:

```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"feature1": 10, "feature2": 5}'