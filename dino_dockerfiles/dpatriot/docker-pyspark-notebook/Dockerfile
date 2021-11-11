FROM webgames/spark:2.1.1

MAINTAINER Shago Vyacheslav <v.shago@corpwebgames.com>

ENV PYTHONPATH $SPARK_HOME/python/:$PYTHONPATH

RUN apt-get update \
    && apt-get install -y build-essential ca-certificates \
    python \
    python-dev \
    python-pip \
    python-zmq \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade --no-use-wheel --force-reinstall pip==9.0.3 setuptools && pip install py4j \
    ipython==5.4.1 \
    jsonschema \
    jinja2 \
    terminado \
    tornado==4.5.2

#RUN ipython profile create pyspark

#COPY pyspark-notebook.py /root/.ipython/profile_pyspark/startup/pyspark-notebook.py
COPY jupyter_notebook_config.json /root/.jupyter/jupyter_notebook_config.json
VOLUME /notebook
WORKDIR /notebook

EXPOSE 8888
ENTRYPOINT []

#add sklearn
ADD requirements.txt /opt/
ENV DEBIAN_FRONTEND noninteractive

# enable the universe
RUN sed -i 's/^#\s*\(deb.*universe\)$/\1/g' /etc/apt/sources.list
RUN apt-get -y update && apt-get install -y \
    mysql-client \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    libmysqlclient* \
    libtiff5-dev \
    libjpeg8-dev \
    zlib1g-dev \
    libfreetype6-dev \
    libpq-dev \
    libxft-dev \
    pkg-config \
    python2.7 \
    python-dev \
    python-pip \
    tmux \
    curl \
    nano \
    vim \
    git \
    htop \
    man \
    software-properties-common \
    unzip \
    wget \
    libncurses5-dev \
    readline-common

RUN apt-get build-dep -y python-matplotlib
RUN rm -rf /var/lib/apt/lists/*

RUN pip install -r /opt/requirements.txt && \
    pip install certifi==2015.04.28


ENV SPARK_CLASSPATH /usr/local/spark/jars/mysql-connector-java.jar:/usr/local/spark/jars/spark-avro.jar:/usr/local/spark/jars/spark-redshift.jar:/usr/local/spark/jars/RedshiftJDBC41-1.1.10.1010.jar:/usr/local/spark/jars/minimal-json.jar

CMD aws s3 cp s3://$S3_BUCKET_CONF/hive/config/core-site.xml /usr/local/spark/conf/core-site.xml;aws s3 cp s3://$S3_BUCKET_CONF/hive/config/hive-site.xml /usr/local/spark/conf/hive-site.xml;jupyter notebook --no-browser --allow-root --ip=*
