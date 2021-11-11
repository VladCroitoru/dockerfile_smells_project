#  Single-user image for Rice DataSci Club's JupyterHub
FROM jupyter/scipy-notebook

MAINTAINER Gabe Vacaliuc <gv8@rice.edu>

USER root
COPY files/fix-permissions /usr/local/bin/fix-permissions
#COPY files/start-singleuser.sh /usr/local/bin/start-singleuser.sh
#RUN chmod 775 /usr/local/bin/start-singleuser.sh

#   Add some nbconvert templates from the repo.
RUN mkdir -p /home/$NB_USER/.jupyter/nbconvert-templates 
COPY files/nbconvert-templates /home/jovyan/.jupyter/nbconvert-templates

#   fix permissions for jupyter directory
RUN fix-permissions /home/$NB_USER/.jupyter

RUN mkdir -p /opt/conda/environment-specs
#   Add more environments here

#   End add environments

#   Fix permissions for environment spec
RUN fix-permissions /opt/conda/environment-specs


# Spark dependencies
ENV APACHE_SPARK_VERSION 2.2.0
ENV HADOOP_VERSION 2.7

#   Install 
RUN apt-get -y update && \
    apt-get install --no-install-recommends -y openjdk-8-jre-headless ca-certificates-java && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN cd /tmp && \
        wget -q http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
        echo "7a186a2a007b2dfd880571f7214a7d329c972510a460a8bdbef9f7f2a891019343c020f74b496a61e5aa42bc9e9a79cc99defe5cb3bf8b6f49c07e01b259bc6b *spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c - && \
        tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /usr/local && \
        rm spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark

# Spark and config
ENV SPARK_HOME /usr/local/spark
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

#   Back to Notebook User
USER $NB_USER

#   Just going to drop this here for now since we need it asap
RUN conda install -y tensorflow keras

RUN mkdir -p /home/$NB_USER/.bash
COPY files/bash /home/$NB_USER/.bash
RUN /bin/bash -c "pushd /home/$NB_USER/; rm .bashrc; ln -s .bash/.bashrc .bashrc; popd"
