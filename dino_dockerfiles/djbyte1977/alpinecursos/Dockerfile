FROM openjdk:alpine
MAINTAINER José Luis Zamora Sánchez joseluiszamora@jlz.gmail.com
ARG WF_IMG_VER
ENV WF_IMG_VER ${WF_IMG_VER:-10.1.0.Final}
RUN echo $WF_IMG_VER
###
EXPOSE 8080 9990
WORKDIR /opt
RUN wget http://download.jboss.org/wildfly/${WF_IMG_VER}/wildfly-${WF_IMG_VER}.zip && \
    unzip wildfly-${WF_IMG_VER}.zip && \
    rm wildfly-${WF_IMG_VER}.zip && \
    ln -s wildfly-${WF_IMG_VER} wildfly
RUN ./wildfly/bin/add-user.sh expertojava expertojava --silent
VOLUME /opt/wildfly-${WF_IMG_VER}/standalone/deployments
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement","0.0.0.0"]


