FROM maven:3.3.9-jdk-8

RUN git clone https://github.com/estatio/estatio.git /opt/estatio

WORKDIR /opt/estatio

CMD mvn clean install -Pjetty-console

VOLUME /config

RUN ln -sf /config/persistor.properties /opt/estatio/estatioapp/webapp/src/main/webapp/WEB-INF/persistor.properties

WORKDIR /opt/estatio/estatioapp/webapp

EXPOSE 8080

CMD ["mvn", "jetty:run"]