FROM rpy2/rpy2:devel

MAINTAINER Laurent Gautier <lgautier@gmail.com>

USER root

RUN \
  apt-get update -qq && \
  apt-get install -y \
                     ed \
                     git \
		     libcairo-dev \
		     libedit-dev \
                     lsb-release \
		     llvm-3.8 \
		     scala \
		     wget &&\
  rm -rf /var/lib/apt/lists/*

RUN \
  wget --progress=bar http://mirrors.ocf.berkeley.edu/apache/spark/spark-2.1.0/spark-2.1.0-bin-hadoop2.7.tgz && \
  tar -xzf spark-2.1.0-bin-hadoop2.7.tgz && \
  mv spark-2.1.0-bin-hadoop2.7 /opt/ && \
  rm spark-2.1.0-bin-hadoop2.7.tgz
    
RUN \
  pip3 --no-cache-dir install wheel --upgrade && \
  pip3 --no-cache-dir install sqlalchemy && \
  rm -rf /root/.cache && \
  wget https://github.com/numba/llvmlite/archive/v0.15.0.zip && \
  unzip v0.15.0.zip && \
  cd llvmlite-0.15.0 && \
  LLVM_CONFIG=`which llvm-config-3.8` python3 setup.py install && \
  cd .. && rm -rf llvmlite-0.15.0 && rm v0.15.0.zip && \
  pip3 --no-cache install numba && \
  pip3 --no-cache install findspark && \
  pip3 --no-cache install jupyter_dashboards && \
  jupyter dashboards quick-setup --sys-prefix && \
  rm -rf /root/.cache

RUN \
  echo "glmnet\n\
        gridExtra\n\
        maps\n\
        mapproj\n\
        plotly\n\
        RSQLite\n\
        party\n\
        partykit\n\
        svglite" > rpacks.txt && \
  R -e 'install.packages(sub("(.+)\\\\n","\\1", scan("rpacks.txt", "character")), repos="http://cran.cnr.Berkeley.edu")' && \
  rm rpacks.txt

ENV NB_USER jupyteruser
ENV SPARK_HOME /opt/spark-2.1.0-bin-hadoop2.7 

USER $NB_USER
RUN mkdir -p /home/$NB_USER/work

WORKDIR /home/$NB_USER/work
