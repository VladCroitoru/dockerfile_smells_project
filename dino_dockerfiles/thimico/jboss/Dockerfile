FROM thimico/jre7:latest

MAINTAINER thimico

ENV JBOSS_HOME /opt/jboss-as-7.1.1.Final

WORKDIR /build

# Instalar libreoffice
RUN apk update && apk add libreoffice

RUN mkdir -p /opt \
 && apk add --update bash && rm -rf /var/cache/apk/* \
 && wget http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-as-7.1.1.Final.tar.gz \
 && tar -zxf jboss-as-7.1.1.Final.tar.gz -C /opt \
 && rm -rf /build

ADD content/libreoffice_iniciar.sh /usr/bin/libreoffice_iniciar.sh
ADD content/sofficerc /etc/sofficerc
ADD content/selodigital.txt /opt/jboss-as-7.1.1.Final
 RUN mkdir -p /opt/jboss-as-7.1.1.Final/modules/org/postgres/main/mod
 ADD content/module.xml /opt/jboss-as-7.1.1.Final/modules/org/postgres/main
 ADD content/postgresql-9.3-1102.jdbc41.jar /opt/jboss-as-7.1.1.Final/modules/org/postgres/main
 ADD content/postgresql-9.3-1102.jdbc41.jar.index /opt/jboss-as-7.1.1.Final/modules/org/postgres/main
 ADD content/standalone.conf /opt/jboss-as-7.1.1.Final/bin
  RUN   mkdir /usr/share/fonts
 RUN   mkdir /usr/share/fonts/truetrype
ADD content/Fonts /usr/share/fonts/truetrype
 RUN fc-cache

# Expose the ports we're interested in
EXPOSE 8080 8443 9990 8100
 
VOLUME ["/tmp"]

RUN chmod +x /usr/bin/libreoffice_iniciar.sh

# Set the default command to run on boot
# This will boot WildFly in the standalone mode and bind to all interface
CMD  ["/usr/bin/libreoffice_iniciar.sh"]

#rodar o comando: docker run --name jbossdt -v ~/docker_volumes/jbossdt:/opt/jboss-as-7.1.1.Final/standalone -p 8080:8080 jboss