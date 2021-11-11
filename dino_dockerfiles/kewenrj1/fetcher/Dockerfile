FROM ubuntu:14.04
MAINTAINER Rickie Kewene <kewenrj1@student.op.ac.nz>
ENV REFRESHED_AT 2015-08-11
RUN apt-get -yqq update
RUN apt-get -yqq install wget
VOLUME [ "/var/lib/tomcat7/webapps/" ]
WORKDIR /var/lib/tomcat7/webapps/
ENTRYPOINT [ "wget" ]
CMD [ "-?" ]
