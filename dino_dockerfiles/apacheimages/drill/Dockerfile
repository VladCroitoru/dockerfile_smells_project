FROM apacheimages/oracle-jdk

WORKDIR /usr/local/src
RUN wget "http://www.apache.org/dyn/closer.lua?filename=drill/drill-1.12.0/apache-drill-1.12.0.tar.gz&action=download"
RUN tar zxf "closer.lua?filename=drill%2Fdrill-1.12.0%2Fapache-drill-1.12.0.tar.gz&action=download"
RUN ln -s /usr/local/src/apache-drill-1.12.0 /usr/local/apache-drill
COPY apache-drill.sh /etc/profile.d/apache-drill.sh
RUN chmod +x /etc/profile.d/apache-drill.sh
