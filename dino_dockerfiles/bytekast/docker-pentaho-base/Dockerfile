FROM tutum/ubuntu:trusty

MAINTAINER Rowell Belen developer@bytekast.com

# Add a repo where Oracle JDK7 can be found.
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:webupd8team/java

# Auto-accept the Oracle JDK license
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

RUN apt-get update
RUN apt-get install -y oracle-java7-installer

# Install supervisor
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

# Install postgres
RUN apt-get -y install postgresql-9.3

# Add pentaho user
RUN useradd --create-home -s /bin/bash -G sudo pentaho
RUN sed -i.orig 's/%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD:ALL/' /etc/sudoers
RUN cp -rvT /root /home/pentaho
RUN chown -Rv pentaho:pentaho /home/pentaho

# Setup Environment
RUN echo export JAVA_HOME=/usr/lib/jvm/java-7-oracle >>/etc/bash.bashrc
ADD psqlfix.sql /root/
RUN /etc/init.d/postgresql start && \
	sudo -u postgres psql </root/psqlfix.sql && rm /root/psqlfix.sql
ADD psqlfix.sh /root/
RUN sh /root/psqlfix.sh && rm /root/psqlfix.sh

# Add Pentaho database scripts
RUN mkdir -p /home/pentaho/data/postgresql/
ADD data/postgresql/create_quartz_postgresql.sql /home/pentaho/data/postgresql/create_quartz_postgresql.sql
ADD data/postgresql/create_jcr_postgresql.sql /home/pentaho/data/postgresql/create_jcr_postgresql.sql
ADD data/postgresql/create_repository_postgresql.sql /home/pentaho/data/postgresql/create_repository_postgresql.sql
ADD data/postgresql/create_jcr_postgresql.sql /home/pentaho/data/postgresql/pentaho_logging_postgresql.sql
ADD data/postgresql/create_repository_postgresql.sql /home/pentaho/data/postgresql/pentaho_mart_postgresql.sql

# Load Pentaho database scripts
ADD loaddb.sh /home/pentaho/
RUN chmod +x /home/pentaho/loaddb.sh
RUN /etc/init.d/postgresql start && \
	printf 'password\n' | /home/pentaho/loaddb.sh

# Copy supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV AUTHORIZED_KEYS **None**

EXPOSE 5432 22
CMD ["/usr/bin/supervisord"]