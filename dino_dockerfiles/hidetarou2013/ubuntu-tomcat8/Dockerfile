FROM ubuntu:14.04
MAINTAINER hidetarou2013 <hidetoshi_maekawa@e-it.co.jp>

#---------------------------------------
# install java
#---------------------------------------
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \
    apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer libxext-dev libxrender-dev libxtst-dev unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

#---------------------------------------
# install tomcat8
#---------------------------------------
RUN useradd -r tomcat8 --shell /bin/false
RUN mkdir -p /usr/local/tomcat8
WORKDIR /usr/local/tomcat8
RUN wget http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.30/bin/apache-tomcat-8.0.30.tar.gz
RUN tar -xzvf apache-tomcat-8.0.30.tar.gz
RUN rm -f apache-tomcat-8.0.30.tar.gz
RUN chown -R tomcat8:tomcat8 /usr/local/tomcat8

ENV JRE_HOME=/usr/lib/jvm/java-8-oracle/jre
ENV CATALINA_HOME=/usr/local/tomcat8/apache-tomcat-8.0.30
ENV PATH=$PATH:$CATALINA_HOME/bin
RUN export JRE_HOME CATALINA_HOME PATH
RUN echo $CATALINA_HOME
RUN echo $PATH

RUN chmod -R 775 $CATALINA_HOME/conf
RUN chmod -R 775 $CATALINA_HOME/webapps
RUN chmod -R 775 $CATALINA_HOME/work
RUN chmod -R 775 $CATALINA_HOME/lib

RUN echo "JRE_HOME=/usr/lib/jvm/java-8-oracle/jre" >> /etc/profile
RUN echo "CATALINA_HOME=/usr/local/tomcat8/apache-tomcat-8.0.30" >> /etc/profile
RUN echo "export JRE_HOME CATALINA_HOME" >> /etc/profile

EXPOSE 8080

#---------------------------------------
# tag:JDBC
#---------------------------------------
ADD "$PWD"/lib/*.jar $CATALINA_HOME/lib/
#---------------------------------------
# tag:MySQL
#---------------------------------------
ADD "$PWD"/bin/catalina.sh_mysql $CATALINA_HOME/bin/catalina.sh
RUN chmod 755 $CATALINA_HOME/bin/catalina.sh
#---------------------------------------
# tag:MySQL_workbook
#---------------------------------------
ADD "$PWD"/conf/server.xml_workbook $CATALINA_HOME/conf/server.xml
ADD "$PWD"/conf/context.xml_workbook $CATALINA_HOME/conf/context.xml
#---------------------------------------
# tag:deploy_jaxrs-sample
#---------------------------------------
#ADD "$PWD"/webapps/*.war $CATALINA_HOME/webapps/

CMD ["catalina.sh", "run"]