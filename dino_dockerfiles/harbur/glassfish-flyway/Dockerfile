FROM glassfish:4.0-jdk7
RUN wget -q http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.35/mysql-connector-java-5.1.35.jar -O /usr/local/glassfish4/glassfish/domains/domain1/lib/mysql-connector-java-5.1.34.jar
RUN wget -qO- http://central.maven.org/maven2/org/flywaydb/flyway-commandline/3.2.1/flyway-commandline-3.2.1.tar.gz | tar zxv -C /opt/

ADD assets/entrypoint /.entrypoint
RUN chmod +x /.entrypoint

RUN ln -s /opt/flyway-*/flyway /usr/bin/
RUN ln -s /usr/local/glassfish4/glassfish/domains/domain1/lib/mysql-connector-java-5.1.34.jar /opt/flyway-3.2.1/drivers/

CMD /.entrypoint