FROM jupyter/pyspark-notebook

LABEL maintainer="riyad.parvez@gmail.com"

USER root

RUN apt-get -y update && \
    apt-get install --no-install-recommends -y ssh openssh-server openssh-client libblas-dev liblapack-dev gfortran && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx8192M --driver-java-options=-Dlog4j.logLevel=info

USER $NB_UID

# RUN conda config --append channels conda-forge
RUN conda install --quiet -y nltk jupyterthemes nbdime ipdb
# RUN conda install -c conda-forge jupyter-console || exit 0
RUN jt -t chesterish
EXPOSE 4040 8080
