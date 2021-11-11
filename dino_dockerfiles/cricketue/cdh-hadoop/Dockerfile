FROM centos:6.6

RUN  yum update -y && \
     yum install -y wget && \
     yum install -y java-1.7.0-openjdk java-1.7.0-openjdk-devel && \
     yum -y install initscripts && \
     wget -q -O /etc/yum.repos.d/cloudera-cdh5.repo http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-cdh5.repo && \
     sed -ri 's/cdh\/5/cdh\/5.9.0/' /etc/yum.repos.d/cloudera-cdh5.repo  && \
     yum install -y hadoop-hdfs-datanode && \
     yum install -y hadoop-yarn-resourcemanager && \
     yum install -y hadoop-mapreduce && \
     yum install -y hadoop-yarn-nodemanager && \
     yum install -y hadoop-client




#yum install -y wget
# &&  \
#    wget -q -O /tmp/jdk.rpm --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/${JDK_VERSION}-${JDK_BUILD_NO}/${JDK_RPM}
#&& \
#    rpm -ivh /tmp/jdk.rpm && \
#    yum -y install initscripts && \
#    wget -q -O /etc/yum.repos.d/cloudera-cdh5.repo http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-cdh5.repo && \
#    sed -ri 's/cdh\/5/cdh\/5.9.0/' /etc/yum.repos.d/cloudera-cdh5.repo && \
#    yum install -y hadoop && \
#                   hadoop-hdfs-datanode && \
#                   hadoop-yarn-resourcemanager && \
#                   hadoop-mapreduce && \
#                   hadoop-client



CMD ["/bin/bash"]


