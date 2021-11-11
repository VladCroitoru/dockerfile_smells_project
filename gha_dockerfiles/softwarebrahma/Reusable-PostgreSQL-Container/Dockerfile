# Dockerfile
FROM postgres:14.0
ENV POSTGRES_USER dbadmin
ENV POSTGRES_DB postgres
ENV POSTGRES_PASSWORD postgres
# COPY init.sh /usr/local/bin/
# RUN chmod 777 /usr/local/bin/init.sh
# ENTRYPOINT []
COPY init.sh /docker-entrypoint-initdb.d/
