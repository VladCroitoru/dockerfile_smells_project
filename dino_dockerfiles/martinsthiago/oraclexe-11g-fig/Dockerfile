FROM ubuntu:14.04.1

MAINTAINER Martins Thiago <rogue.thiago@gmail.com>

ENV ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
ENV ORACLE_SID=XE
ENV PATH=$ORACLE_HOME/bin:$PATH

ADD chkconfig /sbin/
ADD init.ora /
ADD initXETemp.ora /
ADD startup.sh /

# Install Oracle dependencies
RUN apt-get install wget -y && \
    wget https://github.com/MartinsThiago/oraclexe-11g-fig/raw/master/oracle-xe_11.2.0-1.0_amd64.debaa && \
    wget https://github.com/MartinsThiago/oraclexe-11g-fig/raw/master/oracle-xe_11.2.0-1.0_amd64.debab && \
    wget https://github.com/MartinsThiago/oraclexe-11g-fig/raw/master/oracle-xe_11.2.0-1.0_amd64.debac && \
    apt-get install -y libaio1 net-tools bc && \
    ln -s /usr/bin/awk /bin/awk && \
    mkdir /var/lock/subsys && \
    chmod 755 /sbin/chkconfig && \
    chmod +x /startup.sh && \
    cat /oracle-xe_11.2.0-1.0_amd64.deba* > /oracle-xe_11.2.0-1.0_amd64.deb && \
    dpkg --install /oracle-xe_11.2.0-1.0_amd64.deb && \
    rm -rf oracle-xe* && \
    mv /init.ora /u01/app/oracle/product/11.2.0/xe/config/scripts && \
    mv /initXETemp.ora /u01/app/oracle/product/11.2.0/xe/config/scripts && \
    printf 8080\\n1521\\noracle\\noracle\\ny\\n | /etc/init.d/oracle-xe configure

EXPOSE 1521
EXPOSE 8080

ENTRYPOINT ["/startup.sh"]
