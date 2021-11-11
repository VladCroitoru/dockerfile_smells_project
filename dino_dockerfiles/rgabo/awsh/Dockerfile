FROM python:3.5
MAINTAINER Gabor Ratky <rgabo@rgabostyle.com>

# Spark dependencies
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends openjdk-7-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
ENV APACHE_SPARK_VERSION 2.0.2
ENV HADOOP_VERSION 2.7
ENV PY4J_VERSION 0.10.3
RUN cd /tmp && \
        wget -q http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
        echo "e6349dd38ded84831e3ff7d391ae7f2525c359fb452b0fc32ee2ab637673552a *spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha256sum -c - && \
        tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /usr/local && \
        rm spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark

ENV SPARK_HOME /usr/local/spark
ENV PATH $PATH:$SPARK_HOME/bin
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-${PY4J_VERSION}-src.zip
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

# fuse & syslog-ng
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends fuse syslog-ng && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
ADD etc/syslog-ng/syslog-ng.conf /etc/syslog-ng/syslog-ng.conf

# goofys (S3)
RUN cd /usr/bin && \
        wget -q https://github.com/kahing/goofys/releases/download/v0.0.9/goofys && \
        chmod +x goofys

# useful CLI tools
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends htop nano tmux tree vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# workspaces
RUN mkdir -p /buckets

# local workspace
RUN mkdir -p /local
WORKDIR /local

# awsh
RUN mkdir -p /awsh

COPY requirements.txt /awsh/requirements.txt
RUN pip install -r /awsh/requirements.txt

COPY requirements-test.txt /awsh/requirements-test.txt
RUN pip install -r /awsh/requirements-test.txt

COPY . /awsh
RUN pip install /awsh

# entrypoint
COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
