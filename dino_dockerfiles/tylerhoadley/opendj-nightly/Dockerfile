FROM java:8

MAINTAINER tyler.hoadley[AT]computersthatwork[DOT]ca

WORKDIR /opt

RUN curl http://maven.forgerock.org/repo/snapshots/org/forgerock/opendj/opendj3-server-dev/3.0.0-SNAPSHOT/opendj3-server-dev-3.0.0-20150211.174712-258.zip -o opendj.zip

RUN mkdir -p /opt/opendj/
ADD example.ldif /opt/opendj/example.ldif

# Overwrite below enviroment varible when launching your containers via docker run

ENV DJROOTPASSWD="changeme"                                               
ENV DJBASEDN="dc=example,dc=com"
ENV DJIMPORT="--ldifFile /opt/opendj/example.ldif"


RUN unzip opendj.zip && ./opendj/setup --cli -p 389 --ldapsPort 636 --enableStartTLS --generateSelfSignedCertificate \
    $DJIMPORT  --baseDN "$DJBASEDN" -h localhost --rootUserPassword $DJROOTPASSWD --acceptLicense --no-prompt \
    && rm opendj.zip && /opt/opendj/bin/stop-ds

ADD run.sh /opt/opendj/run.sh
RUN chmod 777 /opt/opendj/run.sh

EXPOSE 389 636 4444

CMD  ["/opt/opendj/run.sh"]
