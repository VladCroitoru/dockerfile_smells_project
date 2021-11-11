FROM wnameless/oracle-xe-11g

RUN apt-get -y install -f nano telnet curl unzip; \
    curl -LO https://github.com/liquibase/liquibase/releases/download/liquibase-parent-3.4.1/liquibase-3.4.1-bin.zip; \
    unzip liquibase-3.4.1-bin.zip -d liquibase-3.4.1-bin; \
    curl -LO 'http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.tar.gz' -H 'Cookie: oraclelicense=accept-securebackup-cookie'; \
    tar zxvf jdk-7u51-linux-x64.tar.gz
ENV JAVA_HOME /jdk1.7.0_51
ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe
ENV PATH $JAVA_HOME/bin:$ORACLE_HOME/bin:/liquibase-3.4.1-bin:$PATH
CMD /usr/sbin/startup.sh && /usr/sbin/sshd -D
