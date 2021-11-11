FROM oraclelinux:6.8

MAINTAINER Alan Peng <peng.alan@gmail.com>

USER root

ADD download_jdk6.sh /root
ADD download_weblogic1036.sh /root
ADD wls-silent.xml /root
ADD entrypoint.sh /root

RUN chmod +x /root/*.sh && \
  /root/download_jdk6.sh && \
  /root/download_weblogic1036.sh && \
  rm /root/download_jdk6.sh /root/download_weblogic1036.sh && \
  mkdir /root/jdk && \
  chmod +x jdk-6u45-linux-x64.bin && \
  ./jdk-6u45-linux-x64.bin && \
  rm jdk-6u45-linux-x64.bin && \
  mv jdk1.6.0_45 /root/jdk && \
  /root/jdk/jdk1.6.0_45/bin/java -jar wls1036_generic.jar -mode=silent -silent_xml=/root/wls-silent.xml && \ 
  rm wls1036_generic.jar /root/wls-silent.xml 

ADD create-wls-domain.py /root/Oracle
ADD create_managed_server.py /root/Oracle
ADD ManagedServer.properties /root/Oracle
ADD register_managed_server.sh /root/Oracle
RUN chmod +x /root/Oracle/*.py && chmod +x /root/Oracle/*.sh

ENV CONFIG_JVM_ARGS '-Djava.security.egd=file:/dev/./urandom'

WORKDIR /root/Oracle/Middleware

ENV PATH $PATH:/root/jdk/jdk1.6.0_45/bin:/root/Oracle/Middleware/oracle_common/common/bin:/root/Oracle/Middleware/user_projects/domains/base_domain/bin

CMD ["/root/entrypoint.sh"]
