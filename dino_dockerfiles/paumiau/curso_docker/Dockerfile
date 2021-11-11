#
# paumiau
# Instalación de bbdd postsgre desde una imagen ubuntu original.
#


# Sistema operativo base del contenedor.
FROM ubuntu:16.04

# Preparo apt para que soporte los paquetes de postgresql.
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Añado el repositorio de .
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# Instalo el paquete de postgresql 9.3
RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3


#Cambio a la cuenta de postgres para realizar el resto de la instalación.
USER postgres

# Creao un usuario dentro de la bbdd que se llama docker:docker y creo la bbdd que se llama ejemplo con permisos de
# propietario para el usuario docker.
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -O docker docker

# Configuro la base de datos para conexiones remotas.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

# Exponemos el puerto de postgreSql
EXPOSE 5432

# Añado un volumen para almacenar las bbdd, los backups y los logs.
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql", "tmp"]

# Comando por defecto que se ejecutará al iniciar el contenedor.
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]
