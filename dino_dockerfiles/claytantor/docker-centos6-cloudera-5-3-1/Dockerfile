FROM centos:centos6
MAINTAINER Clay Graham <claytantor@gmail.com>

#install and start ntp
RUN yum -y install ntp ntpdate ntp-doc
RUN ntpdate pool.ntp.org

#oracle java jdk8
RUN yum update -y
RUN yum install -y wget && wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u5-b13/jdk-8u5-linux-x64.rpm
RUN rpm -ivh jdk-8u5-linux-x64.rpm && rm jdk-8u5-linux-x64.rpm

#setup the cloudera repo
RUN wget http://archive.cloudera.com/cm5/redhat/6/x86_64/cm/cloudera-manager.repo --output-document=/etc/yum.repos.d/cloudera-manager.repo
RUN yum -y install cloudera-manager-server-db-2 cloudera-manager-daemons cloudera-manager-server cloudera-manager-agent cloudera-manager-daemons

#make the directories
RUN groupadd hadoop
RUN useradd -g hadoop hdfs 

RUN mkdir /var/cm
RUN mkdir /var/cm/datanode1
RUN mkdir /var/cm/datanode2
RUN mkdir /var/cm/datanode3
RUN mkdir /var/cm/nn
RUN mkdir /var/cm/snn
RUN mkdir /var/cm/nm
RUN mkdir /var/cm/impala
RUN mkdir /var/cm/hive
RUN mkdir /var/cm/cloudera-host-monitor
RUN mkdir /var/cm/cloudera-service-monitor
RUN mkdir /var/cm/sqoop2
RUN mkdir /var/cm/zookeeper
RUN mkdir /var/cm/zookeeper/version-2
RUN chmod -R 777 /var/cm

#this needs to be tested and verified
RUN chown -R hdfs:hadoop /var/cm/datanode1
RUN chown -R hdfs:hadoop /var/cm/datanode2
RUN chown -R hdfs:hadoop /var/cm/datanode3

ADD scripts/hosts_base /root/hosts_base
ADD scripts/start.sh /root/start.sh
RUN chmod +x /root/start.sh


EXPOSE 22 2181 7180 7182 50010 50075 50020 8020 50070 50090 8032 8030 8031 8033 8088 8888 8040 8042 8041 10020 19888 41370 38319 10000 21050 25000 25010 25020 18080 18081 7077 7078 9000 9001

CMD /root/start.sh
