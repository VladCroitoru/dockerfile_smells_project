FROM qnib/dplain-jdk8

ENV HADOOP_VER=2.7.3 \
    ENTRYPOINTS_DIR=/opt/qnib/entry

RUN apt-get update \
 && apt-get install -y curl bc jq nmap \
 && curl -fsL http://apache.claz.org/hadoop/common/hadoop-${HADOOP_VER}/hadoop-${HADOOP_VER}.tar.gz | tar xzf - -C /opt && mv /opt/hadoop-${HADOOP_VER} /opt/hadoop \
 && rm -rf /tmp/* \
 && useradd --shell /bin/bash hadoop
COPY opt/qnib/entry/*.sh /opt/qnib/entry/
COPY opt/qnib/hdfs/etc/*.xml /opt/qnib/hdfs/etc/
COPY etc/bashrc.hadoop /etc/
