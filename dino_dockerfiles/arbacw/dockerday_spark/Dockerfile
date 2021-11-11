FROM centos:7
ENV container docker
RUN yum -y install wget && yum -y install which && yum -y install java-1.8.0-openjdk-devel
RUN wget -O /etc/yum.repos.d/hdp.repo http://public-repo-1.hortonworks.com/HDP/centos7/2.x/updates/2.6.1.0/hdp.repo
RUN yum -y install hive
RUN yum -y install spark2
ENV JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk-1.8.0.151-1.b12.el7_4.x86_64
CMD ["/usr/sbin/init"]
