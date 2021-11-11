FROM alejandrofcarrera/phusion.maven
MAINTAINER Miguel Esteban Gutierrez

# Exports
ENV HARVESTER_HOME="/opt/org-harvester"

COPY files/pom.xml $HARVESTER_HOME/pom.xml

# Configure runit
ADD ./my_init.d/ /etc/my_init.d/
ONBUILD ADD ./my_init.d/ /etc/my_init.d/

WORKDIR /opt/org-harvester
RUN mvn -U

CMD ["/sbin/my_init"]

EXPOSE 80
