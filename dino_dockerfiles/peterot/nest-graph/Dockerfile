# Nest Data Collector
#
# VERSION               0.0.1

FROM      ubuntu
LABEL maintainer="Peter Ottery"

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk gnuplot openssh-server supervisor adduser libfontconfig curl && \
    apt-get install -y python python-setuptools python-pip
RUN mkdir -p  /var/run/sshd /var/log/supervisor /data/hbase /data/zookeeper

# Install HBase
WORKDIR /opt
RUN wget http://archive.apache.org/dist/hbase/hbase-1.1.0/hbase-1.1.0-bin.tar.gz && tar xzf hbase-1.1.0-bin.tar.gz && rm hbase-*.gz

ADD hbase-site.xml /opt/hbase-1.1.0/conf/
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/" >> /opt/hbase-1.1.0/conf/hbase-env.sh

# Install OpenTSDB
ADD https://github.com/OpenTSDB/opentsdb/releases/download/v2.3.0/opentsdb-2.3.0_all.deb /tmp/
RUN dpkg -i /tmp/opentsdb-2.3.0_all.deb && rm /tmp/opentsdb-2.3.0_all.deb
ADD opentsdb.sh /opt/

# Install Grafana
ADD https://dl.grafana.com/oss/release/grafana_5.4.2_amd64.deb /tmp/
RUN apt-get install -y adduser libfontconfig
RUN dpkg -i /tmp/grafana_5.4.2_amd64.deb && rm /tmp/grafana_5.4.2_amd64.deb
ADD grafana.sh /opt/
ADD dashboards /opt/dashboards

# Install tCollector
RUN wget https://github.com/OpenTSDB/tcollector/archive/v1.3.2.tar.gz && tar xzf v1.3.2.tar.gz && rm v1.3.2.tar.gz
ADD home_collectors /opt/home_collectors

RUN pip install python-nest
ADD tCollector.sh /opt/

ADD nest-auth.py /opt/

# Configure Supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

expose 22 3000 4242
CMD ["/usr/bin/supervisord"]

VOLUME /data 

