FROM mysql:5.7
LABEL maintainer "okisanjp <okisan.jp@gmail.com>"

ENV MYSQL_ROOT_USER="root" \
    MYSQL_ROOT_PASSWORD="passw0rd" \
    MYSQL_DATABASE="myapp_db" \
    MYSQL_USER="myapp" \
    MYSQL_PASSWORD="myapp_passw0rd"

ADD myapp.cnf /etc/mysql/conf.d/
