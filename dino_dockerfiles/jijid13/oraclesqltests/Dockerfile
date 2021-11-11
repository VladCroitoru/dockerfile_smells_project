# This Dockerfile is used to build an image containing basic stuff to be used as a Jenkins slave build node.
FROM ubuntu:14.04.1

MAINTAINER Madjid Kazi Tani <jijid13@gmail.com>

ENV ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
ENV ORACLE_SID=XE
ENV PATH=$ORACLE_HOME/bin:$PATH
ENV DUMP_FILE_PATH=/home/jenkins/dump/V1.0.dmp
ENV INIT_FILES=/home/jenkins/db/init
ENV SQL_PATH=/home/jenkins/db/v2.0/alters
ENV SYSTEM_SQL_PATH=/home/jenkins/db/v2.0/admin
ENV IMPORT_SCHEMA=USER1
ENV SQLPLUS_USER=USER1
ENV SQLPLUS_PASSWORD=oracle

# In case you need proxy
#RUN echo 'Acquire::http::Proxy "http://127.0.0.1:8080";' >> /etc/apt/apt.conf

# Add locales after locale-gen as needed
# Upgrade packages on image
# Preparations for sshd
run locale-gen en_US.UTF-8 &&\
    apt-get -q update &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--force-confnew" --no-install-recommends &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends openssh-server &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends git &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends subversion &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends mercurial &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends wget &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends libaio1 &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends net-tools &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends bc &&\
    apt-get -q autoremove &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin &&\
    sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd &&\
    mkdir -p /var/run/sshd

ADD oracle-xe_11.2.0-1.0_amd64.debaa /
ADD oracle-xe_11.2.0-1.0_amd64.debab /
ADD oracle-xe_11.2.0-1.0_amd64.debac /

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install JDK 7 (latest edition)
RUN apt-get -q update &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends openjdk-7-jre-headless &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:openjdk-r/ppa
RUN apt-get update -y
RUN apt-get install -y openjdk-8-jdk

# Set user jenkins to the image
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\
    echo "jenkins:jenkins" | chpasswd &&\
    usermod -a -G sudo jenkins &&\
    echo "jenkins    ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers


RUN mkdir /home/jenkins/workspace && \
    chown jenkins:jenkins /home/jenkins/workspace && \
    mkdir /home/jenkins/log && \
    chown jenkins:jenkins /home/jenkins/log 

ADD chkconfig /sbin/
ADD init.ora /
ADD initXETemp.ora /
ADD startup.sh /
ADD createdir.sql /home/jenkins/
ADD sqltests.sh /home/jenkins/
ADD checkInvalidObjects.sql /home/jenkins/

RUN chmod u+x /home/jenkins/sqltests.sh && \
    chown jenkins:jenkins /home/jenkins/sqltests.sh && \
    chown jenkins:jenkins /startup.sh && \
    chmod 777 /home/jenkins/log

RUN ln -s /usr/bin/awk /bin/awk && \
    mkdir /var/lock/subsys && \
    chmod 755 /sbin/chkconfig && \
    chmod +x /startup.sh && \
    cat /oracle-xe_11.2.0-1.0_amd64.deba* > /oracle-xe_11.2.0-1.0_amd64.deb && \
    dpkg --install /oracle-xe_11.2.0-1.0_amd64.deb && \
    rm -rf oracle-xe* && \
    mv /init.ora /u01/app/oracle/product/11.2.0/xe/config/scripts && \
    mv /initXETemp.ora /u01/app/oracle/product/11.2.0/xe/config/scripts && \
    printf 8080\\n1521\\noracle\\noracle\\ny\\n | /etc/init.d/oracle-xe configure

RUN rm -rf /oracle-xe_11.2.0-1.0_amd64.debaa && \
    rm -rf oracle-xe_11.2.0-1.0_amd64.debab && \
    rm -rf oracle-xe_11.2.0-1.0_amd64.debac

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]

