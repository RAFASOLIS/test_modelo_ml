# 1. Imagen Base
# Usar una imagen oficial de Python slim (ligera)
FROM python:3.13.9-slim

# 2. Establecer el Directorio de Trabajo
# Donde se ejecutará la app dentro del contenedor
WORKDIR /app

# 3. Instalar Dependencias
# Copiar primero el fichero de requisitos para aprovechar el caché de capas de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar los ficheros de la aplicación
# Copia la API y el modelo (que ya debe estar entrenado)
COPY api.py .
COPY modelo_entrenado.pkl .

# 5. Exponer el Puerto
# El puerto que Flask está usando (definido en api.py)
EXPOSE 5000

# 6. Comando de Ejecución
# El comando que se ejecuta cuando el contenedor arranca
CMD ["python", "api.py"]