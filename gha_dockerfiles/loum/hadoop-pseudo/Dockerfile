ARG HADOOP_VERSION
ARG UBUNTU_BASE_IMAGE

FROM ubuntu:$UBUNTU_BASE_IMAGE AS downloader

RUN apt-get update && apt-get install -y --no-install-recommends \
 wget\
 ca-certificates

ARG HADOOP_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN wget -qO-\
 http://apache.mirror.serversaustralia.com.au/hadoop/core/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz |\
 tar -C /tmp -xzf - 

# AWS S3 jar.  You need to match Hadoop version with the jar files.
WORKDIR /tmp/jars
RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar

# Other jars needed for s3a connectors.
RUN wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.12.60/aws-java-sdk-1.12.60.jar &&\
 wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-core/1.12.60/aws-java-sdk-core-1.12.60.jar &&\
 wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-dynamodb/1.12.60/aws-java-sdk-dynamodb-1.12.60.jar &&\
 wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/1.12.60/aws-java-sdk-s3-1.12.60.jar &&\
 wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-s3/1.12.60/aws-java-sdk-s3-1.12.60.jar &&\
 wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-sts/1.12.60/aws-java-sdk-sts-1.12.60.jar &&\
 wget https://repo1.maven.org/maven2/joda-time/joda-time/2.10.5/joda-time-2.10.5.jar &&\
 wget https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.5.11/httpclient-4.5.11.jar

### downloader layer end

FROM ubuntu:$UBUNTU_BASE_IMAGE

ARG OPENSSH_SERVER
ARG OPENJDK_8_HEADLESS
ARG PYTHON3_VERSION
ARG PYTHON3_PIP
RUN apt-get update && apt-get install -y --no-install-recommends\
 python3.8=$PYTHON3_VERSION\
 python3-pip=$PYTHON3_PIP\
 python-is-python3\
 openssh-server=$OPENSSH_SERVER\
 openjdk-8-jdk-headless=$OPENJDK_8_HEADLESS &&\
 rm -rf /var/lib/apt/lists/*

ARG HADOOP_VERSION
ARG HADOOP_HOME=/opt/hadoop

COPY --from=downloader /tmp/hadoop-$HADOOP_VERSION /opt/hadoop-$HADOOP_VERSION
RUN ln -s /opt/hadoop-$HADOOP_VERSION $HADOOP_HOME

ARG HADOOP_LIBS=$HADOOP_HOME/share/hadoop/common/lib
# Remove dated httpclient* jars
RUN rm $HADOOP_LIBS/httpclient* 2>/dev/null

ARG HADOOP_USER=hdfs
ARG HADOOP_GROUP=hdfs
RUN addgroup $HADOOP_GROUP &&\
 useradd -m\
 --gid $HADOOP_GROUP\
 --shell /bin/bash\
 $HADOOP_USER

COPY --from=downloader --chown=$HADOOP_USER:$HADOOP_GROUP /tmp/jars/* $HADOOP_LIBS/
COPY --chown=$HADOOP_USER:$HADOOP_GROUP scripts/config-setter.py /

WORKDIR $HADOOP_HOME
RUN mv etc/hadoop/hadoop-env.sh etc/hadoop/hadoop-env.sh.orig

COPY files/hdfs-site.xml.j2 etc/hadoop/hdfs-site.xml.j2
COPY files/yarn-site.xml.j2 etc/hadoop/yarn-site.xml.j2
COPY files/mapred-site.xml.j2 etc/hadoop/mapred-site.xml.j2
COPY files/core-site.xml.j2 etc/hadoop/core-site.xml.j2
COPY files/hadoop-env.sh etc/hadoop/hadoop-env.sh

ARG object_store_endpoint=s3.amazonaws.com
ENV OBJECT_STORE_ENDPOINT=${object_store_endpoint}

# Hadoop NameNode port.
EXPOSE 9000

# Hadoop NameNode web UI.
EXPOSE 9870

# YARN ResourceManager web UI.
EXPOSE 8088

# MapReduce JobHistory Server web UI.
EXPOSE 19888

WORKDIR /home/$HADOOP_USER/var/run
WORKDIR /home/$HADOOP_USER/.ssh
COPY files/sshd_config sshd_config

WORKDIR /var/log/hadoop
RUN chown -R $HADOOP_USER:$HADOOP_GROUP . $HADOOP_HOME

WORKDIR /home/$HADOOP_USER

# Allow Setup passphraseless ssh for hadoop_user.
RUN ssh-keygen -t rsa -f .ssh/ssh_host_rsa_key -N '' &&\
 ssh-keygen -t rsa -P '' -f .ssh/id_rsa &&\
 cat .ssh/id_rsa.pub >> .ssh/authorized_keys &&\
 chmod 0600 .ssh/authorized_keys

RUN chown -R $HADOOP_USER:$HADOOP_GROUP .

USER $HADOOP_USER

# Add Hadoop executables to HADOOP_USER PATH.
RUN echo export PATH="$HADOOP_HOME/bin:$PATH" >> .bashrc

# Need Jinja2 for config JIT dynamic settings during container create.
RUN python -m pip install --user jinja2

COPY --chown=$HADOOP_USER:$HADOOP_GROUP scripts/hadoop-bootstrap.sh /hadoop-bootstrap.sh

CMD [ "/hadoop-bootstrap.sh" ]
