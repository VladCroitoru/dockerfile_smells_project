FROM tomcat:7-jre7
RUN apt-get update -y && apt-get install -y wget curl locate
RUN apt-get install -y vim
RUN mkdir /ncwms
WORKDIR /ncwms
ADD LICENCE /
ADD tomcat-users.xml /usr/local/tomcat/conf/
RUN wget http://tenet.dl.sourceforge.net/project/ncwms/ncwms/1.2/ncWMS-1.2.war
RUN cp ncWMS-1.2.war /usr/local/tomcat/webapps/ncWMS.war
RUN updatedb
