FROM centos:7

ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV PYTHONIOENCODING UTF-8

RUN yum update -y
RUN yum install -y gcc wget \
    python-setuptools python-devel \
    java-1.8.0-openjdk net-tools

RUN yum autoremove -y && \
    yum clean all && \
    rm -rf /var/cache/yum

RUN easy_install pip

### Install python library
RUN pip install --no-cache-dir requests[security]
RUN pip install --no-cache-dir pandas scipy scikit-learn matplotlib jupyter pyspark
COPY jupyter_notebook_config.py /root/.jupyter/

### Install zeppelin
RUN wget -q ftp://ftp.twaren.net/Unix/Web/apache/zeppelin/zeppelin-0.7.3/zeppelin-0.7.3-bin-netinst.tgz
RUN tar zxf zeppelin-0.7.3-bin-netinst.tgz -C /opt/ && rm zeppelin-0.7.3-bin-netinst.tgz
ENV ZEPPELIN_HOME /opt/zeppelin-0.7.3-bin-netinst
COPY zeppelin-env.sh ${ZEPPELIN_HOME}/conf/
COPY zeppelin-site.xml ${ZEPPELIN_HOME}/conf/

### Install spark and hadoop-aws
RUN wget -q https://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-hadoop2.7.tgz
RUN tar zxf spark-2.2.0-bin-hadoop2.7.tgz -C /opt/ && rm spark-2.2.0-bin-hadoop2.7.tgz
ENV SPARK_HOME /opt/spark-2.2.0-bin-hadoop2.7
COPY spark-defaults.conf ${SPARK_HOME}/conf/

EXPOSE 8888 8080 4040

VOLUME [ "/data" ]

