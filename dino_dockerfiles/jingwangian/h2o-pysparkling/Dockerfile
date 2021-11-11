FROM jupyter/pyspark-notebook

MAINTAINER jing wang <jingwangian@gmail.com>

ENV MASTER "local[*]"

USER root

# Install all OS dependencies for openai gym
RUN apt-get update && apt-get install -yq --no-install-recommends unzip

RUN echo "spark.executor.memory   50g" >>$SPARK_HOME/conf/spark-defaults.conf

# switch user
USER $NB_USER

RUN pip install --upgrade pip

# Install H2O pysparkling requirements
RUN pip install requests && \
pip install tabulate && \
pip install six && \
pip install future && \
pip install colorama && \
pip install awscli

WORKDIR /home/$NB_USER/work

RUN wget http://h2o-release.s3.amazonaws.com/h2o/rel-weierstrass/7/h2o-3.14.0.7.zip
RUN wget http://h2o-release.s3.amazonaws.com/sparkling-water/rel-2.2/2/sparkling-water-2.2.2.zip

RUN unzip h2o-3.14.0.7.zip
RUN unzip sparkling-water-2.2.2.zip

ENV H2O_PYTHON_WHEEL="/home/$NB_USER/work/h2o-3.14.0.7/python/h2o-3.14.0.7-py2.py3-none-any.whl"

EXPOSE 54321
EXPOSE 54322
EXPOSE 55555
EXPOSE 4040
EXPOSE 22

ENV PYSPARK_DRIVER_PYTHON="ipython"
ENV PYSPARK_DRIVER_PYTHON_OPTS="notebook"

ENV AWS_ACCESS_KEY_ID 1
ENV AWS_SECRET_ACCESS_KEY 2
ENV AWS_DEFAULT_REGION ap-southeast-2
ENV AWS_DEFAULT_OUTPUT json

WORKDIR sparkling-water-2.2.2

CMD ["/bin/bash", "bin/pysparkling"]
