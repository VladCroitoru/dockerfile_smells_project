# Usa como base el entorno de python oficial, versión 2.7-slim
FROM python:3.7-rc-slim
# Cambia el directorio de trabajo a /app (en el host)
WORKDIR /app
# Copia el directorio actual (local) en /app (del contenedor)
ADD . /app
# Instala las librerías necesarias dep python, según indica "requirements.txt"
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Permite que el puerto 80 esté accesible desde el exterior del contenedor
EXPOSE 80
# Define una variable de entorno
ENV NAME World
# Ejecuta "app.py" cuando arranca el contenedor
CMD ["python", "app.py"]
