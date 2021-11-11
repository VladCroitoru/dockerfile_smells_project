FROM trueosiris/docker-baseimage:latest
MAINTAINER Tim Chaubet <tim@chaubet.be>

ADD init.ora /
ADD initXETemp.ora /

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y -q bc \
                          curl \
                          htop \
                          libaio1 \
                          net-tools \
                          rlwrap \
                          vim \
 && apt-get clean \
 && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* \
 && ln -s /usr/bin/awk /bin/awk \
 && mkdir /var/lock/subsys 
 
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

COPY runonce.sh /sbin/runonce
COPY runonce.sh /sbin/chkconfig
RUN chmod +x /sbin/runonce; sync \
    && /bin/bash -c /sbin/runonce \
    && rm /sbin/runonce
RUN chmod +X /sbin/chkconfig; sync 

ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe
ENV PATH $ORACLE_HOME/bin:$PATH
ENV ORACLE_SID=XE
ENV DEFAULT_SYS_PASS oracle
ENV PORT 1521
ENV processes 500
ENV sessions 555
ENV transactions 610

EXPOSE 1521
EXPOSE 8080
VOLUME ["/u01/app/oracle","/config"]

#ADD entrypoint.sh /
#ENTRYPOINT ["/entrypoint.sh"]
CMD ["/sbin/my_init"]
