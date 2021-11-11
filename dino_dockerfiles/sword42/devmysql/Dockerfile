FROM mysql
RUN apt-get update && apt-get install -y curl
RUN curl -o /etc/mysql/conf.d/devmin.cnf https://raw.githubusercontent.com/sword42/devmysql/master/devmin.cnf
