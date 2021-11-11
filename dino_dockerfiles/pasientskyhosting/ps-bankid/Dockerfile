FROM cantara/alpine-zulu-jdk8
MAINTAINER Andreas Krüger <ak@patientsky.com>

RUN apk -Uu add bash jq supervisor tzdata

RUN ln -s /usr/local/java/bin/java /bin/java && \
    ulimit -m unlimited && \
    ulimit -v unlimited && \
    ulimit -n 65536 && \
    mkdir -p /data && \
    mkdir -p /keystore

RUN adduser -D -s /bin/sh bankid

WORKDIR /data
ADD jce/local_policy.jar /usr/local/java/jre/lib/security/
ADD jce/US_export_policy.jar /usr/local/java/jre/lib/security/
ADD jce/jce.java /data/jce.java
RUN javac jce.java && java Test_JCE && rm Test_JCE.class && rm jce.java

ADD conf/supervisord.conf /etc/supervisord.conf

ADD scripts/start.sh /start.sh
RUN chmod 755 /start.sh

EXPOSE 80
CMD ["/start.sh"]
