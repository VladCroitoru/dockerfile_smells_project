# This Dockerfile will build mahout
# To build this image using this Dockerfile, use:
# sudo docker build --tag="mahout:0.12.2" .

FROM google/debian:wheezy

MAINTAINER borromeotlhs@gmail.com

# this assumes running from the directory the installer is extracted to

# Need the volumes-from command in command line to ensure the code we classify is mounted as a volume

#ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q

# Don't know which ports mahout depends on, if any
#EXPOSE 9000

# from http://mahout.apache.org/developers/buildingmahout.html
# technically, mahout needs Java JDK 1.7, but this _should_ work
RUN apt-get install openjdk-7-jdk -yq
RUN echo "JAVA_HOME=/usr/bin" >> /etc/environment
# needs maven3, ironically retrieved through 'maven' package though 'maven2' exists. . .
#RUN apt-get install -y maven
#RUN apt-get install -y git
RUN apt-get install -y curl wget openssh-server openssh-client

RUN echo 'PATH=$PATH:HOME/bin:$JAVA_HOME/bin' >> /etc/profile &&\
    echo 'export JAVA_HOME' >> /etc/profile &&\
    echo 'export PATH' >> /etc/profile

RUN addgroup hadoop
RUN adduser -ingroup hadoop --gecos "" --disabled-password hduser

RUN rm -rf /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key

USER hduser

RUN ssh-keygen -q -N "" -t rsa -f /home/hduser/.ssh/id_rsa
RUN cp /home/hduser/.ssh/id_rsa.pub /home/hduser/.ssh/authorized_keys
# add localhost to hduser's list of known_hosts files without need ssh login
RUN ssh-keyscan -H localhost >> ~/.ssh/known_hosts

USER root

#WORKDIR /src/mahout
#RUN git clone https://github.com/apache/mahout.git /src/mahout

WORKDIR /tmp

RUN wget http://archive.apache.org/dist/mahout/0.12.2/apache-mahout-distribution-0.12.2.tar.gz && \
    tar -xvzf apache-mahout-distribution-0.12.2.tar.gz && \
    mv apache-mahout-distribution-0.12.2 /usr/local/mahout

RUN wget http://archive.apache.org/dist/hadoop/core/hadoop-2.7.3/hadoop-2.7.3.tar.gz && \
    tar -xvzf hadoop-2.7.3.tar.gz && \
    mv hadoop-2.7.3 /usr/local/hadoop

WORKDIR /usr/local
RUN chown -R hduser:hadoop hadoop


# ENV needs to be used, as the above doesn't seem to be visible from cli
ENV JAVA_HOME /usr
ENV HADOOP_HOME /usr/local/hadoop

# Needed to specify that we are running without a cluster
ENV MAHOUT_LOCAL true
ENV MAHOUT_HOME /usr/local/mahout

# SSH login fix so user isn't kicked after login
RUN sed 's#session\s*required\s*pam_loginuid.so#session optional pam_loginuid.so#g' -i /etc/pam.d/sshd

# so you can call 'mahout'
ENV PATH $PATH:/usr/local/mahout/bin
