FROM java:8
MAINTAINER memed <gabriel.couto@memed.com.br>

RUN wget https://pilotfiber.dl.sourceforge.net/project/pentaho/Data%20Integration/7.1/pdi-ce-7.1.0.0-12.zip && unzip pdi-ce-7.1.0.0-12.zip && rm pdi-ce-7.1.0.0-12.zip

RUN wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.43.zip && unzip mysql-connector-java-5.1.43.zip && cp mysql-connector-java-5.1.43/mysql-connector-java-5.1.43-bin.jar data-integration/lib && rm -R mysql-connector-java-5.1.43 && rm mysql-connector-java-5.1.43.zip

WORKDIR /data-integration

CMD ["/data-integration/carte.sh", "0.0.0.0", "8081"]