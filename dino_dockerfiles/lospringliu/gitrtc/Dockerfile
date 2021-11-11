FROM ibmjava:latest
MAINTAINER Xinchun Liu <lospringliu@gmail.com>
RUN apt-get update && apt-get install -y telnet iputils-ping net-tools vim python3-pip libmysqlclient-dev git libldap2-dev libsasl2-dev && pip3 install --upgrade pip && pip3 install "django<2" docutils mysqlclient pyldap django-mptt django-reversion
EXPOSE 8000
