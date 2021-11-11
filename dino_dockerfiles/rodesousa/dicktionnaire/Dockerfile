FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=admin

RUN \
    apt-get update -y \
    && apt-get install python -y \
    && apt-get install python-mysqldb -y

COPY files/ /
