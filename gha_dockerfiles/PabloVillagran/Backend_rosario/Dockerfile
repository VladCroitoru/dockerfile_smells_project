# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Instalar requisitos para mysqlclient
RUN set -eux && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# copia todos los archivos del repositorio a la carpeta /app
WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

#Expone puerto 9980 para servicios
EXPOSE 9980

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "ws.py"]
ENTRYPOINT [ "python", "api/flaskrun.py"]