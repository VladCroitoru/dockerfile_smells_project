FROM golang:latest

MAINTAINER Abhinav Ajgaonkar <abhi@crowdriff.com>

RUN \
	apt-get update; \
	apt-get install -y -qq postgresql; \
	rm /etc/postgresql/9.4/main/pg_hba.conf; \
	echo 'local   all             all                                     trust' >> /etc/postgresql/9.4/main/pg_hba.conf; \
	echo 'host    all             all             127.0.0.1/8             trust' >> /etc/postgresql/9.4/main/pg_hba.conf; \
	echo 'host    all             all             ::1/128                 trust' >> /etc/postgresql/9.4/main/pg_hba.conf; \
	echo 'host    all             all             ::0/0                   trust' >> /etc/postgresql/9.4/main/pg_hba.conf; \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/bin/bash"]
