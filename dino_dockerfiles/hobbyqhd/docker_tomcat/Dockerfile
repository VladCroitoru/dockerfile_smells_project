FROM ubuntu
MAINTAINER hobbyqhd “liubingxin1030@outlook.com”
ENV REFRESHED_AT 2017_06_14
RUN apt-get -yqq update
RUN apt-get -yqq install wget
 
VOLUME ["/var/lib/tomcat7/webapps/"]
WORKDIR /var/lib/tomcat7/webapps/
 
ENTRYPOINT ["wget"]
CMD ["--help"]
