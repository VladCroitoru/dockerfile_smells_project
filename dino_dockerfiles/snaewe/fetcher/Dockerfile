FROM ubuntu:14.04
MAINTAINER Stefan Naewe <stefan.naewe@gmail.com>
ENV REFRESHED_AT 2015-04-11
RUN apt-get -yqq update && apt-get -yqq install wget
VOLUME [ "/var/lib/tomcat7/webapps/" ]
WORKDIR /var/lib/tomcat7/webapps/
ENTRYPOINT [ "wget" ]
CMD [ "-?" ]

