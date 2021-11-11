FROM ubuntu:trusty
MAINTAINER Mhd Sami Almouhtaseb <mssatnami@gmail.com>

ENV LICENSE_SERVER_HOME=$HOME/license
ENV USER satnami

RUN mkdir ${LICENSE_SERVER_HOME}

ADD license/ $LICENSE_SERVER_HOME
ADD docker-entrypoint.sh /

COPY docker-entrypoint.sh /usr/local/bin/

RUN chmod +x ${LICENSE_SERVER_HOME} -R 
RUN chmod +x docker-entrypoint.sh

EXPOSE 1017

WORKDIR $LICENSE_SERVER_HOME

CMD ["/docker-entrypoint.sh"]
