FROM openjdk:8-jdk
MAINTAINER Lucid Programmer<lucidprogrammer@hotmail.com>
# stable release of tomcat as of Sept 2017
ENV TOMCAT_VERSION 8.5.20
# Get Tomcat
RUN wget --quiet --no-cookies http://apache.rediris.es/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz && \
tar xzvf /tmp/tomcat.tgz -C /opt && \
mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat && \
rm /tmp/tomcat.tgz


ENV CATALINA_HOME /opt/tomcat
ENV PATH $PATH:$CATALINA_HOME/bin

EXPOSE 8080
EXPOSE 8009

WORKDIR /opt/tomcat

ENV AXIS2_VERSION 1.7.6
RUN wget -P /opt http://archive.apache.org/dist/axis/axis2/java/core/$AXIS2_VERSION/axis2-$AXIS2_VERSION-bin.zip && \
apt-get update && \
    apt-get install -y zip ant maven && \
    apt-get clean && \
    unzip /opt/axis2-$AXIS2_VERSION-bin.zip -d /opt && \
    rm /opt/axis2-$AXIS2_VERSION-bin.zip

ENV AXIS2_HOME /opt/axis2-$AXIS2_VERSION
ENV PATH /opt/axis2-$AXIS2_VERSION/bin:$PATH
# build the axis2 webapp and deploy to tomcat
RUN cd $AXIS2_HOME/webapp && ant create.war
# RUN cd $AXIS2_HOME/samples/soapwithattachments && ant generate.service && echo sample-swa.aar >> services.list
WORKDIR $AXIS2_HOME/samples
# RUN for d in */ ; do     cd "$d" && ant generate.service && cd ..; done


RUN cp $AXIS2_HOME/dist/axis2.war $CATALINA_HOME/webapps/axis2.war
# this is not meant for production deploymment.
COPY tomcat-users.xml $CATALINA_HOME/conf/tomcat-users.xml

COPY axis2.xml $AXIS2_HOME/conf/axis2.xml
COPY mtomfileserve $AXIS2_HOME/samples/mtomfileserve
RUN cd $AXIS2_HOME/samples/mtomfileserve && ant
# Launch Tomcat
# CMD ["/opt/tomcat/bin/catalina.sh", "run"]

CMD ["axis2server.sh"]
