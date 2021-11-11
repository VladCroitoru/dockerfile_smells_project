FROM ubuntu:14.04
MAINTAINER sawanoboriyu@higanworks.com

RUN apt-get update
RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd

RUN apt-get install -y apache2
RUN mkdir -p /var/lock/apache2 /var/run/apache2

RUN apt-get install -y libapache2-mod-uwsgi build-essential git sqlite3 supervisor libpq-dev libmysqlclient-dev postgresql mysql-client
RUN apt-get install -y python python-pip python-dev python-setuptools uwsgi-plugin-python
ADD provision.sh /provision.sh
RUN /provision.sh && rm -f /provision.sh
RUN a2enmod rewrite

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY config /config
COPY sudoers /etc/sudoers

ADD uwsgi.ini /opt/uwsgi/uwsgi.ini
ADD run.sh /run.sh
ADD startup.sh /startup.sh
RUN chmod 755 /*.sh

EXPOSE 22 80
CMD ["/run.sh"]
