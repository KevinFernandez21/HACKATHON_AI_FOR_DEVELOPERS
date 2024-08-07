# Utiliza una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos
COPY backend/app/requirements.txt /app/

# Instala los requisitos
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de tu aplicación al contenedor
COPY backend/app /app

# Establece la variable de entorno para el puerto
ENV PORT 8000

# Expone el puerto en el que la aplicación correrá
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]