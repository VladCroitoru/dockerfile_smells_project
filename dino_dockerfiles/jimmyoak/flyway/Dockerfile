FROM openjdk:8-jre

MAINTAINER Adrián Robles Maiz (Jimmy K. Oak) <adrian.robles.maiz@gmail.com>

ADD https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/4.0.3/flyway-commandline-4.0.3.zip /tmp/flyway.zip
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN unzip /tmp/flyway.zip && \
    rm /tmp/flyway.zip && \
    mv /flyway-4.0.3 /flyway && \
    ln -s /flyway/flyway /usr/local/bin/flyway && \
    chmod 777 /wait-for-it.sh && \
    ln -s /wait-for-it.sh /usr/local/bin/wait-for-it

WORKDIR /flyway
ENTRYPOINT ["bash"]

