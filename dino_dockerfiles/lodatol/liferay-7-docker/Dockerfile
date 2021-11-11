FROM oraclelinux:7.4

ENV TZ Europe/Rome
ENV LANG en_US.UTF-8

ENV LIFERAY_URL 'https://downloads.sourceforge.net/project/lportal/Liferay%20Portal/7.0.3%20GA4/liferay-ce-portal-tomcat-7.0-ga4-20170613175008905.zip'


ENV JAVA_HOME '/usr/java/latest'
ENV CATALINA_BASE '/srv/http/liferay/tomcat-8.0.32'
ENV CATALINA_HOME '/srv/http/liferay/tomcat-8.0.32'
ENV CATALINA_OPTS '-d64 -server -XX:NewSize=700m -XX:MaxNewSize=700m -Xms2G -Xmx2G -Dfile.encoding=UTF8 -Djava.net.preferIPv4Stack=true -Dorg.apache.catalina.loader.WebappClassLoader.ENABLE_CLEAR_REFERENCES=false -Duser.timezone=GMT'

WORKDIR /root
# install oracle java
RUN curl -LO -H "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.rpm && \
    rpm -ivh jdk-8u151-linux-x64.rpm

WORKDIR /srv/http/liferay

RUN yum install -y unzip gd
RUN export TMPDIR="$(mktemp -d ./temp.XXXXXXXX)" && \
    curl -LO $LIFERAY_URL && \
    unzip -q *zip -d $TMPDIR/ && \
    mv $TMPDIR/**/* . && \
    rm tomcat-8.0.32/bin/setenv.sh && \
    rm -rf $TMPDIR

ADD http://repo1.maven.org/maven2/de/javakaffee/msm/memcached-session-manager-tc8/2.1.1/memcached-session-manager-tc8-2.1.1.jar $CATALINA_HOME/lib/ext
ADD http://repo1.maven.org/maven2/de/javakaffee/msm/memcached-session-manager/2.1.1/memcached-session-manager-2.1.1.jar $CATALINA_HOME/lib/ext
ADD http://central.maven.org/maven2/redis/clients/jedis/2.9.0/jedis-2.9.0.jar $CATALINA_HOME/lib/ext

COPY ROOT.xml $CATALINA_HOME/conf/Catalina/localhost/
COPY portal-setup-wizard.properties .

VOLUME ["/srv/http/liferay/", "/srv/http/liferay/data/document_library", "/srv/http/liferay/deploy"]

EXPOSE 8080 8443 

CMD ["sh","-c","$CATALINA_HOME/bin/catalina.sh run"]
