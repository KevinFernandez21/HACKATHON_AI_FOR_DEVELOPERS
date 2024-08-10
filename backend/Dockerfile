# Utilizamos la imagen ligera de Python
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Permitir que las declaraciones y los mensajes de registro aparezcan inmediatamente en los registros de Knative
ENV PYTHONUNBUFFERED True

# Copiamos el código local al contenedor
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Instalamos el servidor para que pueda correr nuestra aplicación 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ejecute el servicio web al iniciar el contenedor. Aquí usamos el gunicorn
# servidor web, con un proceso de trabajo y 8 subprocesos.
# Para entornos con varios núcleos de CPU, aumente la cantidad de trabajadores
# para ser igual a los núcleos disponibles.
# El tiempo de espera se establece en 0 para deshabilitar los tiempos de espera de los trabajadores para permitir que Cloud Run maneje el escalado de instancias.
CMD exec uvicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.main:app

