FROM oraclelinux:6.8

MAINTAINER Alan Peng <peng.alan@gmail.com>

USER root

# Download Oracle JDK6 jdk-6u45-linux-x64.bin and WebLogic11g version 10.3.6 and then install weblogic without domain initiation.
ADD download_jdk6.sh /root
ADD download_weblogic1036.sh /root
ADD wls-silent.xml /root
ADD entrypoint.sh /root

RUN chmod +x /root/*.sh && \
    /root/download_jdk6.sh && \
    /root/download_weblogic1036.sh && \
    rm -f /root/download_jdk6.sh /root/download_weblogic1036.sh && \
    mkdir /root/jdk && \
    chmod +x jdk-6u45-linux-x64.bin && \
    ./jdk-6u45-linux-x64.bin && \
    rm jdk-6u45-linux-x64.bin && \
    mv jdk1.6.0_45 /root/jdk && \
    /root/jdk/jdk1.6.0_45/bin/java -jar wls1036_generic.jar -mode=silent -silent_xml=/root/wls-silent.xml && \ 
    rm wls1036_generic.jar /root/wls-silent.xml 

ADD create-wls-domain.py /root/Oracle

WORKDIR /root/Oracle/Middleware

ENV PATH $PATH:/root/Oracle/Middleware/wlserver_10.3/common/bin:/root/Oracle/Middleware/user_projects/domains/base_domain/bin

ENV CONFIG_JVM_ARGS '-Djava.security.egd=file:/dev/./urandom'

# Expose Node Manager default port, and also default http/https ports for admin console
EXPOSE 7001 5556

CMD ["/root/entrypoint.sh"]
