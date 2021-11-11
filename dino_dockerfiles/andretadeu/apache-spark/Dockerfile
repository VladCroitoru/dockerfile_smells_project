FROM debian:stretch
MAINTAINER "Andre Tadeu de Carvalho <andre.tadeu.de.carvalho@gmail.com>"

ARG SCALA_VERSION=2.11.8
ARG SPARK_VERSION=2.3.2
ENV SCALA_HOME=/opt/scala-${SCALA_VERSION} \
    SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz

# Install wget, OpenJDK-8 and OpenSSH
RUN echo 'deb http://httpredir.debian.org/debian stretch-backports main' > \
    /etc/apt/sources.list.d/stretch-backports.list && \
    apt-get -qq update && \
    apt-get install -yqq wget openjdk-8-jdk openssh-server

# Install Scala
RUN wget http://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz \
    -O /tmp/scala-${SCALA_VERSION}.tgz && \
    tar xf /tmp/scala-${SCALA_VERSION}.tgz -C /opt && \
    rm -f /tmp/scala-${SCALA_VERSION}.tgz

# Install Apache Spark
RUN wget http://ftp.unicamp.br/pub/apache/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz \
    -O /tmp/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz && \
    tar xf /tmp/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz -C /opt && \
    rm -f /tmp/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz

# I'm forced to append /etc/profile due to erratic behavior of ENV with PATH
RUN echo export PATH=$PATH:$SCALA_HOME/bin:$SPARK_HOME/sbin:$SPARK_HOME/bin \
    | tee -a /etc/profile

# Setup ssh keys
COPY install/keys/* /root/.ssh/
COPY install/keys/id_rsa.pub /root/.ssh/authorized_keys
RUN chmod 0600 /root/.ssh/id_rsa && chmod 0600 /root/.ssh/id_rsa.pub

# Configure SSH
RUN echo 'root:teste' | chpasswd && \
    sed -i 's|#PubkeyAuthentication yes|PubkeyAuthentication yes|g' /etc/ssh/sshd_config && \
    sed -i 's|#StrictModes yes|StrictModes yes|g' /etc/ssh/sshd_config && \
    sed -i 's|#AuthorizedKeysFile	%h/.ssh/authorized_keys|AuthorizedKeysFile	%h/.ssh/authorized_keys|g' /etc/ssh/sshd_config && \
    sed -i 's|PermitRootLogin without-password|PermitRootLogin yes|g' /etc/ssh/sshd_config && \
    sed -i 's|#   IdentityFile ~/.ssh/id_rsa|IdentityFile ~/.ssh/id_rsa|g' /etc/ssh/ssh_config && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Spark management script
COPY spark.sh /spark.sh
RUN chmod +x /spark.sh

RUN mkdir /jobs /inputs /outputs

VOLUME ["/jobs", "/inputs", "/outputs"]
EXPOSE 22 8080 8081 7077 6066 4040
ENTRYPOINT [ "/spark.sh" ]
CMD [ "start" ]
