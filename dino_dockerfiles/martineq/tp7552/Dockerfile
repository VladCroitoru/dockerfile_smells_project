##########################################
## Dockerfile para el uso del Servidor  ##
## Basado en Ubuntu 14.04               ##
##########################################

# Seteo la imagen base (Ubuntu oficial, versión 14.04)
FROM ubuntu:14.04

# Autor: mart / Mantiene: mart
MAINTAINER mart mart

# Copio los directorios del repositorio
COPY ./ /home

# Uso el script de instalación con parámetro para Docker
RUN cd /home/server && chmod 777 server_install_v0.5.sh && ./server_install_v0.5.sh -docker

# Defino el directorio para correr
WORKDIR /home/server/build

# Defino el comando estándar
CMD ["bash"]

