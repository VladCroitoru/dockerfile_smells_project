# Dockerized LDAP authentication daemon

FROM ubuntu
MAINTAINER Andriy Tarasenko <at@eggs.de>

ENV WORKING_DIR /srv/nginx-ldap-auth-daemon

ADD nginx-ldap-auth-daemon.py $WORKING_DIR/

RUN \
  chmod +x $WORKING_DIR/nginx-ldap-auth-daemon.py && \
  apt-get update && \
  apt-get install -y python-pip python-dev libldap2-dev libsasl2-dev libssl-dev && \
  pip install python-ldap && \
  apt-get -y autoremove && apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
 
EXPOSE 8888

WORKDIR $WORKING_DIR

CMD ["./nginx-ldap-auth-daemon.py"]
