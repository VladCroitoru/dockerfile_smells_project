FROM charliek/openjdk-jre-7
MAINTAINER Shay Erlichmen "shay@samba.me"

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y pwgen

ENV GRAYLOG_HOME /opt/graylog2-web-interface
ENV GRAYLOG_VER graylog2-web-interface-0.92.0


WORKDIR /opt/
RUN curl -L http://packages.graylog2.org/releases/graylog2-web-interface/graylog2-web-interface-${GRAYLOG_VER}.tgz | tar zx

# web-interface
RUN ln -sf /opt/graylog2-web-interface-${GRAYLOG_VER} ${GRAYLOG_HOME}

EXPOSE 9000

CMD  ["/opt/graylog2-web-interface/bin/graylog2-web-interface"]
