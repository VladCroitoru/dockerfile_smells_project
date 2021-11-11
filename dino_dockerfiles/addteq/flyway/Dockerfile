FROM java:8

ADD https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/4.0.3/flyway-commandline-4.0.3.zip /flyway.zip

RUN unzip /flyway.zip && rm /flyway.zip && mv /flyway* /flyway && ln -s /flyway/flyway /usr/local/bin/flyway

COPY ./flyway.conf /flyway/conf

WORKDIR /flyway
ENTRYPOINT ["flyway"]
CMD ["--help"]
