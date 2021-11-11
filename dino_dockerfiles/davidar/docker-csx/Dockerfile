FROM centos:6

RUN yum update -y && yum install -y \
        wget tar unzip perl mysql-server mysql-devel git patch

RUN cd && wget --no-cookies --no-check-certificate --header \
        "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" \
        "http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.rpm" \
 && yum localinstall -y jdk-7u79-linux-x64.rpm \
 && rm -f jdk-7u79-linux-x64.rpm 
ENV JAVA_HOME=/usr/java/jdk1.7.0_79

RUN cd && wget https://dev.mysql.com/get/mysql57-community-release-el6-7.noarch.rpm  \
 && yum localinstall -y mysql57-community-release-el6-7.noarch.rpm \
 && rm -f mysql57-community-release-el6-7.noarch.rpm \
 && yum update -y
ADD my.cnf /etc/my.cnf

RUN cd && wget http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.65/bin/apache-tomcat-7.0.65.tar.gz \
 && mkdir -p /usr/local/tomcat \
 && tar -zxvf apache-tomcat-7.0.65.tar.gz -C /usr/local/tomcat --strip-components=1 \
 && rm -f apache-tomcat-7.0.65.tar.gz

RUN cd && wget http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.29/bin/apache-tomcat-8.0.29.tar.gz \
 && mkdir -p /usr/local/tomcat-solr \
 && tar -zxvf apache-tomcat-8.0.29.tar.gz -C /usr/local/tomcat-solr --strip-components=1 \
 && rm -f apache-tomcat-8.0.29.tar.gz

RUN cd && wget http://archive.apache.org/dist/lucene/solr/4.10.4/solr-4.10.4.tgz \
 && tar -zxvf solr-4.10.4.tgz && rm -f solr-4.10.4.tgz \
 && cp solr-4.10.4/dist/solr-4.10.4.war /usr/local/tomcat-solr/webapps/solr.war \
 && cp solr-4.10.4/example/lib/ext/*.jar /usr/local/tomcat-solr/lib/ \
 && mkdir /data && cp -Rv solr-4.10.4/example/solr /data/ \
 && rm -rf solr-4.10.4

RUN mv /data/solr/collection1 /data/solr/citeseerx \
 && echo 'name=citeseerx' > /data/solr/citeseerx/core.properties

ADD web.xml.patch /tmp/web.xml.patch
ENV CATALINA_PID=/usr/local/tomcat-solr/.pid
RUN /usr/local/tomcat-solr/bin/startup.sh && sleep 30 && /usr/local/tomcat-solr/bin/shutdown.sh -force \
 && patch /usr/local/tomcat-solr/webapps/solr/WEB-INF/web.xml /tmp/web.xml.patch \
 && rm -f /tmp/web.xml.patch

RUN groupadd solr && useradd -M -s /bin/nologin -g solr -d /usr/local/tomcat-solr solr \
 && chown -R solr:solr /usr/local/tomcat-solr \
 && chown -R solr:solr /data/solr

RUN cd && wget http://archive.apache.org/dist/ant/binaries/apache-ant-1.9.6-bin.tar.gz \
 && tar -zxvf apache-ant-1.9.6-bin.tar.gz -C /opt \
 && rm -f apache-ant-1.9.6-bin.tar.gz
ENV PATH=/opt/apache-ant-1.9.6/bin:$PATH

RUN cd && wget http://archive.apache.org/dist/axis/axis2/java/core/1.6.3/axis2-1.6.3-war.zip \
 && unzip axis2-1.6.3-war.zip && rm -f axis2-1.6.3-war.zip \
 && mv axis2.war /usr/local/tomcat/webapps/ \
 && rm -f LICENSE.txt NOTICE.txt README.txt release-notes.html

RUN cd && wget http://ftp.osuosl.org/pub/fedora-epel/epel-release-latest-6.noarch.rpm \
 && rpm -ivh epel-release-latest-6.noarch.rpm && rm -f epel-release-latest-6.noarch.rpm

RUN cd && wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm \
 && rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt \
 && rpm -K   rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm \
 && rpm -ivh rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm \
 && rm -f rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm

RUN cd /opt && git clone https://github.com/SeerLabs/CiteSeerX.git
