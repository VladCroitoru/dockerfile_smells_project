# ----> BUILD
FROM openjdk:8-jdk-alpine
WORKDIR /opt
RUN apk update
RUN apk add maven
RUN apk add git
WORKDIR /opt
RUN git clone https://github.com/Djbyte1977/cursos.git
WORKDIR /opt/cursos
RUN mvn package

# --> RUN
FROM openjdk:8-jre-alpine
LABEL autor = "Jose Luis Zamora Sanchez"
EXPOSE 8080 9990
WORKDIR /opt
RUN wget http://download.jboss.org/wildfly/10.1.0.Final/wildfly-10.1.0.Final.zip && \
    unzip wildfly-10.1.0.Final.zip && \
    rm wildfly-10.1.0.Final.zip && \
    ln -s wildfly-10.1.0.Final wildfly
RUN ./wildfly/bin/add-user.sh experto experto --silent

COPY --from=0 /opt/cursos/target/cursos.war ./wildfly/standalone/deployments

CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement","0.0.0.0"]
