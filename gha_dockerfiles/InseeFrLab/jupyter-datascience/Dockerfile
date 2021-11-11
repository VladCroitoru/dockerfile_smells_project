FROM jupyter/datascience-notebook:python-3.9.7

USER root

ARG SPARK_VERSION=3.2.0
ARG HADOOP_VERSION=3.3.1
ARG HIVE_VERSION=2.3.9

ARG HADOOP_URL="https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}"
ARG HADOOP_AWS_URL="https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws"
ARG HIVE_URL="https://archive.apache.org/dist/hive/hive-${HIVE_VERSION}"
ARG SPARK_BUILD="spark-${SPARK_VERSION}-bin-hadoop-${HADOOP_VERSION}-hive-${HIVE_VERSION}"
ARG S3_BUCKET="https://minio.lab.sspcloud.fr/projet-onyxia/spark-build"

ENV HADOOP_HOME="/opt/hadoop"
ENV SPARK_HOME="/opt/spark"
ENV HIVE_HOME="/opt/hive"

RUN apt-get -y update && \
    apt-get install --no-install-recommends -y openjdk-11-jre-headless \
                                               ca-certificates-java \
                                               vim \
                                               jq \
                                               bash-completion \ 
                                               unzip && \
    rm -rf /var/lib/apt/lists/*

# Installing mc

RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc -O /usr/local/bin/mc && \
    chmod +x /usr/local/bin/mc

# Installing vault

RUN cd /usr/bin && \
    wget -O vault.zip https://releases.hashicorp.com/vault/1.8.4/vault_1.8.4_linux_amd64.zip && \
    unzip vault.zip && \
    rm vault.zip
RUN vault -autocomplete-install

# Installing kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl

RUN kubectl completion bash >/etc/bash_completion.d/kubectl

RUN mkdir -p $HADOOP_HOME $SPARK_HOME $HIVE_HOME

RUN cd /tmp \
    && wget ${HADOOP_URL}/hadoop-${HADOOP_VERSION}.tar.gz \
    && tar xzf hadoop-${HADOOP_VERSION}.tar.gz -C ${HADOOP_HOME} --owner root --group root --no-same-owner --strip-components=1 \
    && wget ${HADOOP_AWS_URL}/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar \
    && mkdir -p ${HADOOP_HOME}/share/lib/common/lib \
    && mv hadoop-aws-${HADOOP_VERSION}.jar ${HADOOP_HOME}/share/lib/common/lib \
    && wget ${S3_BUCKET}/${SPARK_BUILD}.tgz \
    && tar xzf ${SPARK_BUILD}.tgz -C $SPARK_HOME --owner root --group root --no-same-owner --strip-components=1 \
    && wget ${HIVE_URL}/apache-hive-${HIVE_VERSION}-bin.tar.gz \
    && tar xzf apache-hive-${HIVE_VERSION}-bin.tar.gz -C ${HIVE_HOME} --owner root --group root --no-same-owner --strip-components=1 \
    && wget https://jdbc.postgresql.org/download/postgresql-42.2.18.jar \
    && mv postgresql-42.2.18.jar ${HIVE_HOME}/lib/postgresql-jdbc.jar \
    && rm ${HIVE_HOME}/lib/guava-14.0.1.jar \
    && cp ${HADOOP_HOME}/share/hadoop/common/lib/guava-27.0-jre.jar ${HIVE_HOME}/lib/ \
    && wget https://repo1.maven.org/maven2/jline/jline/2.14.6/jline-2.14.6.jar \
    && mv jline-2.14.6.jar ${HIVE_HOME}/lib/ \
    && rm ${HIVE_HOME}/lib/jline-2.12.jar \
    && rm -rf /tmp/*

RUN pip install s3fs hvac boto3 pyarrow pymongo

RUN pip install jupyterlab-git

ADD spark-env.sh $SPARK_HOME/conf
ADD entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh $SPARK_HOME/conf/spark-env.sh

ENV PYTHONPATH="$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.2-src.zip"
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M
ENV JAVA_HOME "/usr/lib/jvm/java-11-openjdk-amd64"
ENV HADOOP_OPTIONAL_TOOLS "hadoop-aws"
ENV PATH="${JAVA_HOME}/bin:${SPARK_HOME}/bin:${HADOOP_HOME}/bin:${PATH}"

VOLUME ["/home/jovyan"]
ENTRYPOINT [ "/opt/entrypoint.sh" ]
