FROM centos/httpd-24-centos7

ENV SUMMARY="PostgreSQL Documentation" \
    DESCRIPTION="PostgreSQL Documentation as it seen in https://www.postgresql.org/docs/ \
The image is based on centos/httpd-24-centos7 to run unprivileged httpd container."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="PostgreSQL Documentation" \
      io.openshift.expose-services="8080:http,8443:https" \
      io.openshift.tags="documentation,docs,postgresql" \
      name="dockerized-docs/postgresql" \
      maintainer="Genadi Postrilko <genadipost@gmail.com>"

ENV PG_VERSION 10.3

user root

WORKDIR /opt/app-root/src/

RUN yum -y groupinstall "Development Tools" && \
    yum -y install yum-utils openjade docbook-dtds docbook-style-dsssl docbook-style-xsl \
                   readline-devel zlib-devel texlive-jadetex texlive-jadetex-doc

RUN curl -L https://ftp.postgresql.org/pub/source/v$PG_VERSION/postgresql-$PG_VERSION.tar.gz -o postgresql-$PG_VERSION.tar.gz && \
    tar -xvf postgresql-$PG_VERSION.tar.gz -C .

WORKDIR /opt/app-root/src/postgresql-$PG_VERSION

RUN ./configure && \
    make STYLE=website html
 
RUN mv /opt/app-root/src/postgresql-$PG_VERSION/doc/src/sgml/html/* /var/www/html/

RUN rm -rf /opt/app-root/src/{postgresql-$PG_VERSION.tar.gz, postgresql-$PG_VERSION}

USER default

CMD ["/usr/bin/run-httpd"]

