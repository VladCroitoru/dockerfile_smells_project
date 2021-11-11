FROM jupyter/all-spark-notebook
MAINTAINER Manuel de la Peña <manuel.delapenya@liferay.com>

USER root

RUN cd /tmp && \
	rm -fr /usr/local/spark-* && \
        wget -q http://d3kbcqa49mib13.cloudfront.net/spark-2.0.1-bin-hadoop2.7.tgz && \
        tar xzf spark-2.0.1-bin-hadoop2.7.tgz -C /usr/local && \
        rm spark-2.0.1-bin-hadoop2.7.tgz
RUN cd /usr/local && rm spark && ln -s spark-2.0.1-bin-hadoop2.7 spark

ENV APACHE_SPARK_VERSION 2.0.1
ENV SPARK_HOME /usr/local/spark
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.3-src.zip

COPY KC_House_Prices.ipynb /home/jovyan/work/KC_House_Prices.ipynb

RUN chown -R jovyan:users /home/jovyan/work/
