FROM soriyath/debian-swissfr
MAINTAINER Sumi Straessle

ENV DEBIAN_FRONTEND noninteractive

RUN	apt-get update \
	&& apt-get install -y postgresql-9.4 postgresql-client-9.4 \
	&& apt-get install -y postgresql-contrib-9.4
USER postgres
RUN /etc/init.d/postgresql start \
	&& pg_dropcluster --stop 9.4 main \
	&& pg_createcluster --start -e UTF-8 9.4 main \
	&& psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" \
	&& createdb -O docker docker \
	&& echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.4/main/pg_hba.conf \
	&& echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf
EXPOSE 5432
USER root
RUN apt-get clean \
	&& apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /srv/www

ADD postgresql.sv.conf /etc/supervisor/conf.d/postgresql.sv.conf

CMD ["supervisord", "-c", "/etc/supervisor/supervisor.conf"]
