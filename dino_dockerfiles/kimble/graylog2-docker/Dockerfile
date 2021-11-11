FROM phusion/baseimage:0.9.17
MAINTAINER Kim

ENV DEBIAN_FRONTEND noninteractive
ENV JAVA_HOME /opt/graylog/embedded/jre

RUN apt-get update && \
    apt-get install -y curl ntp ntpdate tzdata jq && \
    curl -O -L https://packages.graylog2.org/releases/graylog2-omnibus/ubuntu/graylog_latest.deb && \
    dpkg -i graylog_latest.deb && \
    rm graylog_latest.deb && \
    sed -i "0,/^\s*$/s//\/opt\/graylog\/embedded\/share\/docker\/run_graylogctl\n/" /etc/rc.local && \
    sed -i "0,/^\s*$/s//tail\ \-F\ \/var\/log\/graylog\/server\/current\ \&\n/" /etc/rc.local && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/*


# web interface
EXPOSE 9000
EXPOSE 443

# gelf tcp
EXPOSE 12201

# gelf udp
EXPOSE 12201/udp

# rest api
EXPOSE 12900

# etcd
EXPOSE 4001

# syslog
EXPOSE 514
EXPOSE 514/udp

ADD init.sh /opt/init.sh
ADD install-content-packs.sh /opt/install-content-packs.sh

RUN [ "mkdir", "/opt/content-packs" ] 
ONBUILD ADD content-packs/*.json /opt/content-packs/

CMD ["/opt/init.sh"]
