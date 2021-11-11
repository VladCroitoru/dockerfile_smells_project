FROM btooncall/centos7

RUN mkdir -p /opt/ 2>/dev/null; 
WORKDIR /opt/
RUN wget -q http://www.mirrorservice.org/sites/ftp.apache.org/tomcat/tomcat-7/v7.0.69/bin/apache-tomcat-7.0.69.tar.gz; tar xzf /opt/apache-tomcat-7.0.69.tar.gz && rm -f /opt/apache-tomcat-7.0.69.tar.gz
RUN ln -s /opt/apache-tomcat-7.0.69 /opt/tomcat

# fusionreactor
RUN mkdir -p /opt/fusionreactor/ && wget -q https://intergral-dl.s3.amazonaws.com/FR/FusionReactor-6.1.2/fusionreactor.jar --output-document=/opt/fusionreactor/fusionreactor.jar 

RUN mkdir -p /opt/tomcat/endorsed
# logstash gelf log4j modification (http://logging.paluch.biz/examples/jul.html)
# RUN wget -q https://repo1.maven.org/maven2/biz/paluch/logging/logstash-gelf/1.9.0/logstash-gelf-1.9.0.jar --output-document=/opt/tomcat/lib/logstash-gelf-1.9.0.jar
ADD jars/logstash-gelf-1.9.0.jar /opt/tomcat/endorsed/logstash-gelf-1.9.0.jar
# RUN wget -q http://central.maven.org/maven2/com/googlecode/json-simple/json-simple/1.1.1/json-simple-1.1.1.jar --output-document=/opt/tomcat/lib/json-simple-1.1.1.jar
ADD jars/json-simple-1.1.1.jar /opt/tomcat/endorsed/json-simple-1.1.1.jar
# RUN wget -q http://central.maven.org/maven2/redis/clients/jedis/2.8.0/jedis-2.8.0.jar --output-document=/opt/tomcat/lib/jedis-2.8.0.jar
ADD jars/jedis-2.8.0.jar /opt/tomcat/endorsed/jedis-2.8.0.jar
# RUN wget -q http://apache.mirror.anlx.net//commons/pool/binaries/commons-pool2-2.4.2-bin.tar.gz \
#      && tar xvzf /opt/commons-pool2-2.4.2-bin.tar.gz commons-pool2-2.4.2/commons-pool2-2.4.2.jar \
#      && mv /opt/commons-pool2-2.4.2/commons-pool2-2.4.2.jar /opt/tomcat/lib/ \
#      && rmdir -f /opt/commons-pool2-2.4.2
ADD jars/commons-pool2-2.4.2.jar /opt/tomcat/endorsed/commons-pool2-2.4.2.jar

RUN rm -f /opt/tomcat/conf/logging.properties
ADD logging.properties /opt/tomcat/conf/logging.properties

# some basic defaults to be used in setenv.sh
ENV XMX 2560m 
ENV XMS 2560m 
ENV MaxPermSize 256m
ENV JavaBullhornOptions ""

# add environmental variables, startup for fusion reactor and additional modifications.
# setenv.sh is automatically executed by catalina.sh
ADD setenv.sh /opt/tomcat/bin/setenv.sh
RUN chmod 755 /opt/tomcat/bin/setenv.sh

# internal ports 8080 is tomcat port, 8088 is default fusion-reactor port
EXPOSE 8080 8088

ENTRYPOINT [ "/opt/tomcat/bin/catalina.sh", "run" ]
