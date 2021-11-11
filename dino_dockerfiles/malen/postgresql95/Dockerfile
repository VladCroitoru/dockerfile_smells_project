FROM malen/centos72:latest

MAINTAINER malen <malen.ma@gmail.com>

RUN yum -y update; yum clean all
#RUN yum -y install sudo epel-release; yum clean all

RUN yum -y install http://yum.postgresql.org/9.5/redhat/rhel-7-x86_64/pgdg-centos95-9.5-2.noarch.rpm
RUN yum -y install postgresql95-server; yum clean all

# Setup gosu for easier command execution
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.6/gosu-amd64" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.6/gosu-amd64.asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && rm -r /root/.gnupg/ \
    && chmod +x /usr/local/bin/gosu

#Sudo requires a tty. fix that.
RUN sed -i 's/.*requiretty$/#Defaults requiretty/' /etc/sudoers
#
#Add shell to docker, and then run it.
ADD ./postgresql95-setup /usr/pgsql-9.5/bin/

#ADD ./start_postgres.sh /start_postgres.sh
#ADD ./postgresql.conf /var/lib/pgsql/data/postgresql.conf

#RUN useradd -r -g postgres --uid=999 postgres

RUN mkdir /docker-entrypoint-initdb.d

ENV PG_MAJOR 9.5
ENV PG_VERSION 9.5.1-1.pgdg80+1
ENV PATH /usr/pgsql-9.5/bin:$PATH
ENV PGDATA var/lib/pgsql/9.5/data

#RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql


RUN chmod +x /usr/pgsql-9.5/bin/postgresql95-setup
#RUN chmod +x /start_postgres.sh
#RUN chown -v postgres.postgres /var/lib/pgsql/9.5/data/postgresql.conf

##RUN /usr/pgsql-9.5/bin/postgresql95-setup initdb

##RUN echo "host  all all 0.0.0.0/0" >> /var/lib/pgsql/9.5/data/pg_hba.conf

VOLUME ["/var/lib/pgsql"]

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
#RUN yum -y install net-tools
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432

CMD ["postgres"]
