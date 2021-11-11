# Fetch a war file and deploy to Tomcat7
FROM ubuntu:14.04
MAINTAINER Uta Kapp "uta.kapp@emooti.org"
RUN apt-get -y update
ENV REFRESHED_AT 2016-03-23
RUN apt-get -y install wget
VOLUME ["/var/lib/tomcat7/webapps/"]
WORKDIR /var/lib/tomcat7/webapps/
# docker run --name fetchtom7 emooti/emootifetcher --volumes-from tom7 -d -P /
ENTRYPOINT ["wget"] 
CMD ["-?"]
