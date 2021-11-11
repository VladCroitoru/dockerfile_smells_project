# OpenTSDB Server
#
# VERSION               0.0.1

FROM      ubuntu
MAINTAINER Binbin Zhao <bizhao@vmware.com>

RUN apt-get update && apt-get install -y openjdk-7-jdk gnuplot openssh-server supervisor adduser libfontconfig curl
RUN mkdir -p  /var/run/sshd /var/log/supervisor /data/hbase /data/zookeeper

# Install HBase
ADD http://apache.arvixe.com/hbase/hbase-0.94.27/hbase-0.94.27.tar.gz /opt/
WORKDIR /opt
RUN tar xzf /opt/hbase-*.gz && rm /opt/hbase-*.gz

ADD hbase-site.xml /opt/hbase-0.94.27/conf/
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/" >> /opt/hbase-0.94.27/conf/hbase-env.sh

# Install OpenTSDB
ADD https://github.com/OpenTSDB/opentsdb/releases/download/v2.2.0RC3/opentsdb-2.2.0RC3_all.deb /tmp/
RUN dpkg -i /tmp/opentsdb-2.2.0RC3_all.deb && rm /tmp/opentsdb-2.2.0RC3_all.deb
ADD opentsdb.sh /opt/

# Install Grafana
ADD  https://grafanarel.s3.amazonaws.com/builds/grafana-2.5.0.linux-x64.tar.gz /opt/
RUN tar xzf /opt/grafana-*.gz && rm /opt/grafana-*.gz
ADD grafana.sh /opt/

# Configure Supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

expose 22 3000 4242
CMD ["/usr/bin/supervisord"]

VOLUME /data 

