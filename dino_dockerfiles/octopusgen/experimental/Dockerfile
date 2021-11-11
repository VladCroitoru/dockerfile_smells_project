#############################################################
# DockerFile: v0.3
# Autor: @bashs
# Basado en una imagen de Debian.
#############################################################

# Establece la imagen de base a utilizar para los servicios a implementar
FROM debian

# Matenedor del archivo
MAINTAINER Leonardo Olmos

# Actualización de la lista de fuentes del repositorio de aplicaciones por defecto
RUN apt-get update

# Instalamos algunas herramientas necesarias para trabajar dentro del contenedor.
RUN apt-get install -y vim nano htop screen

########## Para ser utilizado con Memcached ##############################
# Instalar Memcached
#RUN apt-get install -y memcached
# Puerto para exponer (por defecto: 11211)
#EXPOSE 11211
# Comando Memcached por defecto con algunos argumentos
#CMD ["-u", "root", "-m", "128"]
# Establece el usuario para ejecutar el demonio Memcached
#USER daemon
# Establece el punto de entrada para los binarios de Memcached
#ENTRYPOINT memcached
##########################################################################