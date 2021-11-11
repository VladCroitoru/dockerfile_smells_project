FROM ubuntu:16.04

MAINTAINER Wei-Ming Wu <wnameless@gmail.com>

ADD assets /assets
RUN /assets/setup.sh

ENV ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
ENV PATH=$ORACLE_HOME/bin:$PATH
ENV ORACLE_SID=XE
ENV ORACLE_ALLOW_REMOTE=true
ENV LISTENER_ORA=/u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora
ENV TNSNAMES_ORA=/u01/app/oracle/product/11.2.0/xe/network/admin/tnsnames.ora

EXPOSE 22
EXPOSE 1521
EXPOSE 8080

CMD /usr/sbin/startup.sh && /usr/sbin/sshd -D
