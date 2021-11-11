FROM phusion/baseimage
MAINTAINER Mahmood Aghapour <itismahmood@gmai.com>

RUN apt-get update \
    && apt-get install -y --auto-remove --no-install-recommends curl openjdk-8-jdk libgfortran3 python-pip net-tools iputils-ping git binutils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PIO_VERSION 0.11.0
ENV SPARK_VERSION 1.6.3
ENV ELASTICSEARCH_VERSION 1.7.6
ENV HBASE_VERSION 1.2.6

ENV PIO_HOME /PredictionIO-${PIO_VERSION}-incubating
ENV PATH=${PIO_HOME}/bin:$PATH
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

ENV MYPIO_TAR=PredictionIO-${PIO_VERSION}-incubating.tar.gz
ENV ENGINE_HOME /opt/engine

RUN mkdir -p $ENGINE_HOME

#ADD files/${MYPIO_TAR} /
#RUN mv /apache-predictionio-${PIO_VERSION}-incubating/PredictionIO-${PIO_VERSION}-incubating.tar.gz /
#RUN tar zxvf PredictionIO-${PIO_VERSION}-incubating.tar.gz -C /
#RUN rm -r /apache-predictionio-${PIO_VERSION}-incubating && 
RUN curl -O -L https://github.com/itismahmood/predictionio-base/raw/master/files/${MYPIO_TAR}
RUN tar zxvf ${MYPIO_TAR} -C /
RUN rm ${MYPIO_TAR}
RUN mkdir -p ${PIO_HOME}/vendors
COPY files/pio-env.sh ${PIO_HOME}/conf/pio-env.sh

RUN pip install --upgrade pip \
    && pip install setuptools \
    && pip install predictionio

RUN curl -O http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-hadoop2.6.tgz \
    && tar -xvzf spark-${SPARK_VERSION}-bin-hadoop2.6.tgz -C ${PIO_HOME}/vendors \
    && rm spark-${SPARK_VERSION}-bin-hadoop2.6.tgz 

RUN curl -O https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz \
    && tar -xvzf elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz -C ${PIO_HOME}/vendors \
    && rm elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz \
    && echo 'cluster.name: predictionio' >> ${PIO_HOME}/vendors/elasticsearch-${ELASTICSEARCH_VERSION}/config/elasticsearch.yml \
    && echo 'network.host: 127.0.0.1' >> ${PIO_HOME}/vendors/elasticsearch-${ELASTICSEARCH_VERSION}/config/elasticsearch.yml

RUN curl -O http://archive.apache.org/dist/hbase/stable/hbase-${HBASE_VERSION}-bin.tar.gz \
    && tar -xvzf hbase-${HBASE_VERSION}-bin.tar.gz -C ${PIO_HOME}/vendors \
    && rm hbase-${HBASE_VERSION}-bin.tar.gz

COPY files/hbase-site.xml ${PIO_HOME}/vendors/hbase-${HBASE_VERSION}/conf/hbase-site.xml
RUN sed -i "s|VAR_PIO_HOME|${PIO_HOME}|" ${PIO_HOME}/vendors/hbase-${HBASE_VERSION}/conf/hbase-site.xml \
    && sed -i "s|VAR_HBASE_VERSION|${HBASE_VERSION}|" ${PIO_HOME}/vendors/hbase-${HBASE_VERSION}/conf/hbase-site.xml    

RUN cd "$ENGINE_HOME" \
    && git clone https://github.com/apache/incubator-predictionio-template-recommender.git MyRecommendation \
    && cd MyRecommendation \
    && sed -i 's|INVALID_APP_NAME|MyApp1|' engine.json \
    && sed -i 's|\"numIterations\" ?\: ?20|"numIterations" : 10|' engine.json

RUN cd "$ENGINE_HOME" \
    && git clone https://github.com/apache/incubator-predictionio-template-similar-product.git MySimilarProduct \
    && cd MySimilarProduct \
    && sed -i 's|INVALID_APP_NAME|MyApp2|' engine.json \
    && sed -i 's|\"numIterations\" ?\: ?20|"numIterations" : 10|' engine.json

RUN cd "$ENGINE_HOME" \
    && git clone https://github.com/apache/incubator-predictionio-template-ecom-recommender.git MyECommerceRecommendation \
    && cd MyECommerceRecommendation \
    && sed -i 's|INVALID_APP_NAME|MyApp3|' engine.json \
    && sed -i 's|\"numIterations\" ?\: ?20|"numIterations" : 10|' engine.json

RUN cd "$ENGINE_HOME" \
    && git clone https://github.com/actionml/universal-recommender.git MyUniversalRecommender \
    && cd MyUniversalRecommender \
    && sed -i 's|0.13.0|0.14.0|' project/plugins.sbt

CMD ["/sbin/my_init"]

RUN mkdir -p /etc/my_init.d
ADD start-pio.sh /etc/my_init.d/start-pio.sh
RUN chmod +x /etc/my_init.d/start-pio.sh

VOLUME $ENGINE_HOME
WORKDIR $ENGINE_HOME
