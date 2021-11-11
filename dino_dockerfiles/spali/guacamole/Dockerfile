FROM debian:wheezy

#######################################################################################

# Version of guacamole to be installed
ENV GUAC_VER 0.9.6
# Version of mysql-connector-java to install
ENV MCJ_VER 5.1.32
# Version of postgresql-connector-java to install
ENV PCJ_VER 9.4-1201

# prepare apt and system (first clean is required to prevent gpg keys errors)
RUN apt-get clean && \
	apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
	apt-get clean

## install required apackages
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends supervisor tomcat7 && \
	apt-get clean

# build and install guacamole and related components (wrapped script to minimize image commits and keep images small)
COPY build.sh /
RUN /bin/bash /build.sh
RUN rm /build.sh

# add sample configuration for no auth
COPY examples /usr/share/guacamole/examples

#######################################################################################
COPY guacamole.conf /etc/supervisor/conf.d/
COPY docker-entrypoint.sh docker-entrypoint-guacamole.sh /
RUN chmod +x /docker-entrypoint.sh /docker-entrypoint-guacamole.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/bin/supervisord -n"]
#######################################################################################
# expose volumnes
VOLUME [ "/etc/guacamole" ]
# expose ports
EXPOSE 8080
#######################################################################################

