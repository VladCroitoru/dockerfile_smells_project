FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04
LABEL maintainer="comafire@gmail.com"

USER root

# Bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
apt-utils sudo \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

# User
ARG username
ARG userid
ARG home=/home/${username}
RUN echo "username=${username}, userid=${userid}"
RUN adduser ${username} --uid ${userid} --gecos '' --disabled-password \
&& echo "${username} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${username} \
&& chmod 0440 /etc/sudoers.d/${username}


# Lang
ARG locale="ko_KR.UTF-8"
ENV LOCALE ${locale}
RUN echo "LOCALE: $LOCALE"
RUN if [[ $LOCALE = *ko* ]] \
; then \
apt-get update && apt-get install -y --no-install-recommends \
locales language-pack-ko \
; else \
apt-get update && apt-get install -y --no-install-recommends \
locales language-pack-en \
; fi
RUN echo "$LOCALE UTF-8" > /etc/locale.gen && locale-gen
ENV LC_ALL ${LOCALE}
ENV LANG ${LOCALE}
ENV LANGUAGE ${LOCALE}
ENV LC_MESSAGES POSIX

# Common
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential vim curl wget git git-flow cmake bzip2 sudo unzip net-tools \
libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm \
libfreetype6-dev libxft-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
software-properties-common libjpeg-dev libpng-dev ncurses-dev imagemagick \
libgraphicsmagick1-dev libzmq3-dev gfortran gnuplot gnuplot-x11 libsdl2-dev \
openssh-client htop iputils-ping

# Docker
RUN apt-get update && apt-get install -y --no-install-recommends \
apt-transport-https ca-certificates
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update && apt-get install -y --no-install-recommends \
docker-ce

# Python3
RUN apt-get update && apt-get install -y --no-install-recommends \
python3 python3-dev python3-pip python3-virtualenv python3-software-properties python3-gdbm
RUN pip3 install --upgrade pip
RUN pip3 install --cache-dir /tmp/pip3 --upgrade setuptools wheel

# Java
RUN apt-get update && apt-get install -y --no-install-recommends \
openjdk-8-jdk maven

# Scala
ENV SCALA_VERSION 2.12.10
ENV SCALA_HOME /usr/local/scala-${SCALA_VERSION}

ENV PATH $PATH:$SCALA_HOME/bin
RUN curl -sL --retry 3 --insecure \
"https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz" \
| gunzip | tar x -C /usr/local/ \
&& ln -s $SCALA_HOME /usr/local/scala

# Julia
ENV JULIA_VERSION=1.3.1
ENV JULIA_HOME /usr/local/julia-${JULIA_VERSION}

ENV PATH $PATH:$JULIA_HOME/bin
RUN mkdir ${JULIA_HOME} && cd /tmp && \
    wget -q https://julialang-s3.julialang.org/bin/linux/x64/`echo ${JULIA_VERSION} | cut -d. -f 1,2`/julia-${JULIA_VERSION}-linux-x86_64.tar.gz && \
    tar xzf julia-${JULIA_VERSION}-linux-x86_64.tar.gz -C ${JULIA_HOME} --strip-components=1 && \
    rm /tmp/julia-${JULIA_VERSION}-linux-x86_64.tar.gz
RUN ln -fs /usr/local/julia-*/bin/julia /usr/local/bin/julia
RUN julia -v
RUN julia -e 'using Pkg;Pkg.update()'

# R
RUN apt-get update && apt-get --allow-unauthenticated install -y --no-install-recommends \
r-base r-base-dev

# Database
RUN apt-get update && apt-get install -y --no-install-recommends \
libmysqlclient-dev libpq-dev postgresql-client python-mysqldb

# FUSE
RUN apt-get update && apt-get install -y --no-install-recommends \
automake autotools-dev g++ git libcurl4-gnutls-dev libssl-dev libxml2-dev make pkg-config \
fuse libfuse-dev

# FUSE-SSHFS
RUN apt-get update && apt-get install -y --no-install-recommends \
sshfs

# FUSE-S3
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git;cd s3fs-fuse;./autogen.sh;./configure;make;make install

# FUSE-BLOB
RUN wget https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get update
RUN apt-get update && apt-get install -y --no-install-recommends \
blobfuse

# Nginx
RUN apt-get update && apt-get install -y --no-install-recommends \
nginx

# SPARK
ENV SPARK_VERSION 2.4.5
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-hadoop2.7
ENV SPARK_HOME /usr/local/spark-${SPARK_VERSION}
ENV PYSPARK_PYTHON /usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON /usr/bin/python3
ENV PY4J_VERSION 0.10.7

ENV PATH $PATH:${SPARK_HOME}/bin
RUN curl -sL --retry 3 \
"http://www-us.apache.org/dist/spark/spark-${SPARK_VERSION}/${SPARK_PACKAGE}.tgz" \
| gunzip | tar x -C /usr/local \
&& mv /usr/local/$SPARK_PACKAGE $SPARK_HOME \
&& ln -s $SPARK_HOME /usr/local/spark \
&& chown -R root:root $SPARK_HOME
ENV PYTHONPATH $SPARK_HOME/python/:$PYTHONPATH
ENV PYTHONPATH $SPARK_HOME/python/lib/py4j-$PY4J_VERSION-src.zip:$PYTHONPATH

RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 py4j==$PY4J_VERSION

# for Airflow (don't use GPL dependency library)
ENV SLUGIFY_USES_TEXT_UNIDECODE yes

# Python3 Deps
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 docker fabric pytest pycrypto
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 numpy>=1.11.2
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 scipy>=1.4.1 
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 scikit-learn>=0.22.2 scikit-surprise>=1.1.0
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 xgboost>=1.0.1
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 statsmodels>=0.11.1
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 imbalanced-learn>=0.6.2
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 pandas>==1.0.1 pandas_ml pandas-datareader 
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 quandl h5py pyarrow xlrd
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 matplotlib seaborn
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 mysqlclient mysql-connector-python-rf pymysql psycopg2 sqlalchemy
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 flask flask-restful flask-jwt-extended flask_bcrypt flask-sqlalchemy flask-testing
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 nose passlib pybase62 uuid0 imageio
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 ghp-import2 nikola[extras]

# DeepLearning
ARG gpu="FALSE"
ENV GPU ${gpu}
ENV TENSORFLOW_VER 2.1.0
ENV PYTORCH_VER 1.4.0
ENV PYTORCH_VISION_VER 0.5.0
ENV KERAS_VER 2.3.1
RUN echo "GPU: $GPU"
# Tensorflow
RUN if [[ $GPU = *TRUE* ]] \
; then \
apt-get update && apt-get install -y --no-install-recommends libcupti-dev nvidia-modprobe \
&& pip3 install --cache-dir /tmp/pip3 --timeout 600 tensorflow-gpu==$TENSORFLOW_VER \
; else \
pip3 install --cache-dir /tmp/pip3 --timeout 600 tensorflow==$TENSORFLOW_VER \
; fi
# PyTorch 
RUN if [[ $GPU = *TRUE* ]] \
; then \
pip3 install --cache-dir /tmp/pip3 --timeout 600 torch==$PYTORCH_VER torchvision==$PYTORCH_VISION_VER \
; else \
pip3 install --cache-dir /tmp/pip3 --timeout 600 torch==$PYTORCH_VER+cpu torchvision==$PYTORCH_VISION_VER+cpu -f https://download.pytorch.org/whl/torch_stable.html \
; fi
# Keras
RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 keras>=$KERAS_VER

# Jupyter Deps
RUN apt-get update && apt-get install -y --no-install-recommends \
texlive-xetex

# Jupyter
RUN pip3 install -v --no-cache-dir --timeout 600 jupyterlab

# Airflow (wait apache-airflow 2.0)
# RUN pip3 install --cache-dir /tmp/pip3 --timeout 600 apache-airflow
# ENV AIRFLOW_HOME /home/${username}/mnt/airflow

# Jupyter Python3 kernel
RUN python3 -m pip install ipykernel
RUN python3 -m ipykernel install 

# Jupyter Scala
RUN python3 -m pip install spylon-kernel
RUN python3 -m spylon_kernel install

# Jupyter R kernel
RUN apt-get update && apt-get install -y --no-install-recommends \
libcurl4-gnutls-dev libxml2-dev libssl-dev
RUN R -e "install.packages(c('curl', 'repr', 'httr'), repos='http://cran.rstudio.com/')"
RUN R -e "install.packages(c('pbdZMQ', 'devtools', 'IRdisplay', 'evaluate', 'crayon', 'uuid', 'digest'), repos='http://cran.rstudio.com/')"
RUN R -e "install.packages(c('SparkR'), repos='http://cran.rstudio.com/')"
RUN R -e "devtools::install_github('IRkernel/IRkernel')"
RUN R -e "IRkernel::installspec(user = FALSE)"

# Change USER
USER ${username}
WORKDIR ${home}

# Jupyter Julia Kernel
RUN julia -e 'using Pkg;Pkg.update()' && \
julia -e 'using Pkg;Pkg.add("IJulia")' && \
# Precompile Julia packages
julia -e 'using IJulia'

# Env
VOLUME /home/${username}/docker-jupyter

# for Spark
EXPOSE 4040 6066 7077 8080
# for Jupyter
EXPOSE 8888 8088
# for Flask
EXPOSE 5000
# for NGINX
EXPOSE 80
