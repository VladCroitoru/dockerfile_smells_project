FROM arnaudhb/ubuntu-dev:browser

ENV ORACLE_JAVA_PATH b14
ENV ORACLE_JAVA_VERSION 8u102
ENV JAVA_HOME /opt/jdk
ENV PATH $PATH:$JAVA_HOME/bin


# Install Java 8
RUN  cd /opt \
&& wget -q --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
http://download.oracle.com/otn-pub/java/jdk/$ORACLE_JAVA_VERSION-$ORACLE_JAVA_PATH/jdk-$ORACLE_JAVA_VERSION-linux-x64.tar.gz \
&& tar xzf jdk-*.tar.gz \
&& rm -f jdk-*.tar.gz \
&& ln -s /opt/jdk*_*/ jdk


# Entrypoint
COPY docker-entrypoint.sh /
RUN chmod u+x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]
