FROM benchflow/base-images:dns-envconsul-java8_dev

MAINTAINER Vincenzo FERME <info@vincenzoferme.it>

ENV SPARK_HOME /usr/spark
ENV SPARK_VERSION 1.6.2
ENV PYSPARK_PYTHON python2.7
ENV PYSPARK_CASSANDRA_VERSION 0.3.5
ENV HADOOP_VERSION 2.6
ENV GLIBC_VERSION=2.23-r3
ENV LANG=C.UTF-8
ENV MINICONDA_PYTHON_VERSION=2
ENV MINICONDA_VERSION=4.0.5
ENV DATA_ANALYSES_SCHEDULER_VERSION v-dev
ENV DATA_TRANSFORMERS_VERSION v-dev
ENV ANALYSERS_VERSION v-dev
ENV PLUGINS_VERSION v-dev

ENV REGULAR_PYTHON /usr/bin/python2.7
ENV CONDA_PYTHON /opt/conda/bin/python2.7

# Configure environment for miniconda
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

# TODO: remove python, when Spark will be used outside of the container
# TODO: Improve the following code to download only once from github and keep all the wanted files in the right directories
RUN apk --update add curl wget tar python && \
	# Get data-analyses-scheduler
    wget -q --no-check-certificate -O /app/data-analyses-scheduler https://github.com/benchflow/data-analyses-scheduler/releases/download/$DATA_ANALYSES_SCHEDULER_VERSION/data-analyses-scheduler && \
    chmod +x /app/data-analyses-scheduler && \
    # Install Spark
    curl \
	--location \
	--retry 10 \
	http://d3kbcqa49mib13.cloudfront.net/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz \
	| gunzip \
	| tar x -C /usr/ && \
    ln -s /usr/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /usr/spark && \
    mkdir -p /app/configuration && \
    mkdir -p /app/data-transformers && \
    wget -q --no-check-certificate -O - https://github.com/benchflow/data-transformers/archive/$DATA_TRANSFORMERS_VERSION.tar.gz \
    | tar xz --strip-components=2 -C /app/data-transformers data-transformers-$DATA_TRANSFORMERS_VERSION/data-transformers && \
    # Get data-transformers scheduler configuration file
    wget -q --no-check-certificate -O - https://github.com/benchflow/data-transformers/archive/$DATA_TRANSFORMERS_VERSION.tar.gz \
    | tar xz --strip-components=1 --wildcards --no-anchored '*.scheduler.configuration.yml' && \
    for f in *.scheduler.configuration.yml; do mv -i "$f" "app/configuration/$f"; done  && \
    # Get analysers
    mkdir -p /app/analysers && \
    wget -q --no-check-certificate -O - https://github.com/benchflow/analysers/archive/$ANALYSERS_VERSION.tar.gz \
    | tar xz --strip-components=2 -C /app/analysers analysers-$ANALYSERS_VERSION/analysers && \
    # Get analyser scheduler configuration file
    wget -q --no-check-certificate -O - https://github.com/benchflow/analysers/archive/$ANALYSERS_VERSION.tar.gz \
    | tar xz --strip-components=1 --wildcards --no-anchored '*.scheduler.configuration.yml' && \
    for f in *.scheduler.configuration.yml; do mv -i "$f" "app/configuration/$f"; done  && \
    # Get plugins (configuration files) TODO: do not let the following code fails if nothing is found in the .tar.gunzip
    mkdir -p /app/data-transformers/suts && \
    wget -q --no-check-certificate -O - https://github.com/benchflow/sut-plugins/archive/$PLUGINS_VERSION.tar.gz \
    | tar xz --strip-components=1 -C /app/data-transformers/suts --wildcards --no-anchored 'data-transformers.configuration.yml' && \
    # TODO: currenlty skipping analysers configuration because we don't have any
    # && \
    # mkdir -p /app/analysers/suts && \
    # wget -q --no-check-certificate -O - https://github.com/benchflow/sut-plugins/archive/$PLUGINS_VERSION.tar.gz \
    # | tar xz --strip-components=1 -C /app/analysers/suts --wildcards --no-anchored 'analysers.configuration.yml'
    # Clean up
    apk del --purge curl wget tar && \
    rm -rf /var/cache/apk/*

COPY ./configuration.yml /app/configuration.yml

COPY ./dependencies/pyspark-cassandra-assembly-$PYSPARK_CASSANDRA_VERSION.jar $SPARK_HOME/
COPY ./configuration/spark/log4j.properties $SPARK_HOME/conf/

COPY ./services/envcp/config.tpl /app/config.tpl
	
COPY ./services/300-data-analyses-scheduler.conf /apps/chaperone.d/300-data-analyses-scheduler.conf

#TODO: remove, when Spark will be used as a service outside of this container
COPY ./services/400-clean-tmp-folder.conf /apps/chaperone.d/400-clean-tmp-folder.conf

#TODO: remove, when Spark will be used as a service outside of this container
# disables the Spark UI when launching scripts (http://stackoverflow.com/questions/33774350/how-to-disable-sparkui-programmatically/33784803#33784803)
RUN cp $SPARK_HOME/conf/spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf \
    && sed -i -e '$aspark.ui.enabled false' $SPARK_HOME/conf/spark-defaults.conf

# Install miniconda and scipy though it, to solve a linking error with scipy (refer to: https://travis-ci.org/benchflow/analysers/builds/147443000#L485)
# Reference for miniconda setup: https://github.com/CognitiveScale/alpine-miniconda/blob/conda-4.0.5/Dockerfile
RUN apk upgrade --update && \
    # Install glibc and other dependencies needed by miniconda
    apk add --update curl ca-certificates bash git bzip2 unzip sudo libstdc++ glib libxext libxrender && \
    for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; do curl -sSL https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done && \
    apk add --allow-untrusted /tmp/*.apk && \
    rm -v /tmp/*.apk && \
    ( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true ) && \
    echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \
    # Install miniconda
    mkdir -p $CONDA_DIR && \
    echo export PATH=$CONDA_DIR/bin:'$PATH' > /etc/profile.d/conda.sh && \
    curl https://repo.continuum.io/miniconda/Miniconda${MINICONDA_PYTHON_VERSION}-${MINICONDA_VERSION}-Linux-x86_64.sh  -o mconda.sh && \
    /bin/bash mconda.sh -f -b -p $CONDA_DIR && \
    rm mconda.sh && \
    $CONDA_DIR/bin/conda install --yes conda==${MINICONDA_VERSION} && \
    # Install scipy using miniconda
    conda install scipy && \
    conda install pytz && \
    conda install -c anaconda dateutil=2.4.1 && \
    # TODO: evaluate if possible to remove miniconda and its dependencies (git, bzip2, unzip, sudo, libstdc++, glib, libxext, libxrender) at this point
    apk del glibc-i18n

# adds Alpine's testing repository and install scripts dependencies (py-numpy, py-yaml)
RUN sed -i -e '$a@testing http://dl-4.alpinelinux.org/alpine/edge/testing' /etc/apk/repositories \    
    && apk --update add py-yaml py-dateutil

# adds pip and install scripts dependencies (future)
RUN apk --update add py-pip \
    && pip install --upgrade pip \
    && ${REGULAR_PYTHON} /usr/bin/pip install future \
    && ${REGULAR_PYTHON} /usr/bin/pip install minio \
    && apk del --purge py-pip \
    && rm -rf /var/cache/apk/*
 
EXPOSE 8080
